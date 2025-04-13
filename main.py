"""NDF文件解析和处理系统入口模块
主要功能:
1. 命令行参数处理
2. 批次处理流程控制
3. 错误处理和恢复
"""

import argparse
import logging
from pathlib import Path
from src.core.config_manager import ConfigManager
from src.core.parse_manager import ParseManager
from datetime import datetime
import shutil
import time
import msvcrt

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

def process_batch(manager: ParseManager, batch_name: str, stage: str, chunk_size: int = 500):
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
        data_path = manager.base_dir / stage / batch_name / "data.dill"
        class_path = manager.base_dir / stage / batch_name / "classes.py"
        manager.save(mode="register" if stage != "generate" else "generate", 
                    file_path=data_path)
        manager.export(file_path=class_path)
        
        # 在模板注册阶段后更新提取类
        if stage == "template":
            config = ConfigManager.get_instance()
            # 备份当前extract_class
            backup_dir = config.base_dir / "backup"
            backup_dir.mkdir(exist_ok=True)
            backup_path = backup_dir / f"extract_class_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
            if config.extract_class_path.exists():
                shutil.copy2(config.extract_class_path, backup_path)
            
            # 更新extract_class
            shutil.copy2(class_path, config.extract_class_path)
            logging.info(f"Updated extract_class from {class_path}")
        
    except Exception as e:
        logging.error(f"Batch {batch_name} {stage} failed: {e}")
        return False
    return True

def main():
    """主函数"""
    # 1. 初始化日志
    setup_logging(logging.INFO)
    
    # 2. 初始化管理器
    config = ConfigManager.get_instance()
    manager = ParseManager()
    
    try:
        # 3. 对象注册阶段
        print("\n=== Starting Object Registration ===")
        for batch_name in config.get_batch_names():
            if not process_batch(manager, batch_name, "register", chunk_size=500):
                if not wait_for_input("Continue with next batch? (y/n):"): 
                    return
        
        # 4. 模板注册阶段
        print("\n=== Starting Template Registration ===")
        for batch_name in config.get_batch_names():
            if not process_batch(manager, batch_name, "template", chunk_size=500):
                if not wait_for_input("Continue with next batch? (y/n):"): 
                    return
        
        # 5. 对象生成阶段
        manager.load(mode="generate", file_path=manager.base_dir / "generate" / "decks" / "data.dill")
        logging.info("\n=== Starting Object Generation ===")
        for batch_name in config.get_batch_names():
            if not process_batch(manager, batch_name, "generate", chunk_size=5):
                if not wait_for_input("Continue with next batch? (y/n):"): 
                    return
        
        # 6. 建立索引
        logging.info("\n=== Building References ===")
        manager.refer()  # 在此处添加索引建立
        
        # 7. 保存最终状态
        final_dir = manager.base_dir / "final"
        manager.save(mode="register", file_path=final_dir / "register.dill")
        manager.save(mode="generate", file_path=final_dir / "generate.dill")
        manager.export(file_path=final_dir / "classes.py")
        
        logging.info("\nAll stages completed successfully!")
        
    except Exception as e:
        logging.error(f"\nError during processing: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NDF Parser Tool')
    parser.add_argument('--version', type=str, default="M20250403",
                      help='Game version directory (e.g.: M20250403)')
    
    args = parser.parse_args()
    
    try:
        ConfigManager.get_instance().set_version(args.version)
        main()
    except ValueError as e:
        logging.error(f"Error: {e}")
        logging.info("Available versions:")
        for version_dir in ConfigManager.get_instance().data_dir.iterdir():
            if version_dir.is_dir():
                logging.info(f"  - {version_dir.name}")