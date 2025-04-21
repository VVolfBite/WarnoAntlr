"""NDF文件解析和处理系统入口模块
主要功能:
1. 命令行参数处理
2. 批次处理流程控制
3. 错误处理和恢复
"""

import argparse
import logging
from pathlib import Path
try:
    from src.core.path_resolver import PathResolver
    from src.core.config_manager import ConfigManager
    from src.core.parse_manager import ParseManager
except ImportError:
    from core.path_resolver import PathResolver
    from core.config_manager import ConfigManager
    from core.parse_manager import ParseManager
from datetime import datetime
import shutil
import time
import msvcrt
import pickle
import sys

sys.setrecursionlimit(10000) 

def setup_logging(log_level=logging.INFO):
    """配置日志"""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('parse.log', encoding='utf-8'),  # 文件处理器
            logging.StreamHandler()  # 控制台处理器
        ]
    )

def wait_for_input(prompt: str, timeout: int = 1200) -> bool:
    """等待用户输入,超时自动返回True"""
    print(f"\n{prompt} (等待{timeout}秒后自动继续)")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if msvcrt.kbhit():  # Windows下检测键盘输入
            key = input().lower()
            if key == 'n':
                return False
            elif key == 'y':
                return True
        time.sleep(0.1)
        remaining = int(timeout - (time.time() - start_time))
        print(f"\r等待继续... {remaining}秒  ", end='')
    
    print("\r自动选择继续...")
    return True

def process_batch(manager: ParseManager, batch_name: str, stage: str, chunk_size: int = 5000):
    """处理单个批次"""
    try:
        # 获取处理函数
        if stage == "register":
            process_func = manager.register_objects
        elif stage == "template":
            process_func = manager.register_templates
        elif stage == "generate":
            process_func = manager.generate_objects
        else:
            raise ValueError(f"Unknown stage: {stage}")
        
        # 执行处理
        process_func(
            file_list=manager.config.get_batch_files(batch_name),
            batch_name=batch_name,
            chunk_size=chunk_size
        )
        
        # 保存状态
        data_path = manager.config.version_output_dir / stage / batch_name / "data.pkl"
        class_path = manager.config.version_output_dir / stage / batch_name / "classes.py"
        data_path.parent.mkdir(parents=True, exist_ok=True)
        
        if stage == "generate":
            manager.path_resolver.save(data_path)
        else:
            with open(data_path, 'wb') as f:
                pickle.dump(manager.register_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
                
        manager.export(file_path=class_path)
        
        # 在注册阶段后更新提取类
        if stage in {"template","register"}:
            # 备份当前extract_class
            backup_dir = manager.config.version_output_dir / "backup"
            backup_dir.mkdir(exist_ok=True)
            backup_path = backup_dir / f"extract_class_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
            if manager.config.extract_class_path.exists():
                shutil.copy2(manager.config.extract_class_path, backup_path)
            
            # 更新extract_class
            shutil.copy2(class_path, manager.config.extract_class_path)
            logging.info(f"Updated extract_class from {class_path}")
    except Exception as e:
        logging.error(f"Batch {batch_name} {stage} failed: {e}")
        return False
    return True

def main(version: str, load: bool):
    """主函数"""
    # 1. 初始化日志
    setup_logging(logging.INFO)
    
    # 2. 初始化管理器
    config = ConfigManager(version)

    manager = ParseManager(config)  # 传入PathResolver实例
    
    # 定义批次处理顺序
    batch_order = [
        "effects",      # 效果系统
        "unit_consts",  # 单位常量
        "weapons",      # 武器系统
        "units",        # 单位系统
        "decks"         # 卡组系统
    ]
    
    try:
        if load:
            # 加载之前生成的数据
            data_path = manager.config.version_output_dir / "final" / "generate.pkl"
            if data_path.exists():
                manager.path_resolver.load(data_path)
                logging.info("Loaded previously stored parsing results.")
            else:
                logging.error("No stored parsing results found.")
                return
        else:
            # 3. 对象注册阶段
            print("\n=== Starting Object Registration ===")
            for batch_name in batch_order:
                if not process_batch(manager, batch_name, "register", chunk_size=500):
                    if not wait_for_input("Continue with next batch? (y/n):"): 
                        return
            
            # 4. 模板注册阶段
            print("\n=== Starting Template Registration ===")
            for batch_name in batch_order:
                if not process_batch(manager, batch_name, "template", chunk_size=500):
                    if not wait_for_input("Continue with next batch? (y/n):"): 
                        return
            
            # 5. 对象生成阶段
            print("\n=== Starting Object Generation ===")
            for batch_name in batch_order:
                if not process_batch(manager, batch_name, "generate", chunk_size=5):
                    if not wait_for_input("Continue with next batch? (y/n):"): 
                        return
            
            # 6. 建立索引
            print("\n=== Building References ===")
            manager.refer()
            
            # 7. 保存最终状态
            final_dir = manager.config.version_output_dir / "final"
            final_dir.mkdir(parents=True, exist_ok=True)
            
            # 保存注册字典
            with open(final_dir / "register.pkl", 'wb') as f:
                pickle.dump(manager.register_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
                
            # 保存生成的对象
            manager.path_resolver.save(final_dir / "generate.pkl")
            
            # 导出类定义
            manager.export(file_path=final_dir / "classes.py")
            
            logging.info("\nAll stages completed successfully!")
            
    except Exception as e:
        logging.error(f"\nError during processing: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NDF Parser Tool')
    parser.add_argument('--version', type=str, default="M20250403",
                      help='Game version directory (e.g.: M20250403)')
    parser.add_argument('--load', action='store_true', default=False,
                      help='Load previously stored parsing results')
    
    args = parser.parse_args()
    
    try:
        main(args.version, args.load)
    except Exception as e:
        logging.error(f"Error: {e}")
        logging.info("Available versions:")
        for version_dir in Path(__file__).parent / "data":
            if version_dir.is_dir():
                logging.info(f"  - {version_dir.name}")