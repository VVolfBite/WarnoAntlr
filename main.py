"""NDF文件解析和处理系统入口模块"""

import argparse
from pathlib import Path
from src.core.config_manager import ConfigManager
from src.core.parse_manager import ParseManager

def main():
    """主函数"""
    # 1. 获取配置实例
    config = ConfigManager().get_instance()
    
    # 2. 创建管理器
    manager = ParseManager()
    
    try:
        # # 3. 第一阶段: 所有批次的对象注册
        # print("\n=== 开始对象注册阶段 ===")
        # for batch_name in config.get_batch_names():
        #     try:
        #         manager.register_objects(
        #             file_list=config.get_batch_files(batch_name),
        #             batch_name=batch_name
        #         )
        #         # 保存该批次的注册状态
        #         register_data = manager.base_dir / "register" / batch_name / "data.dill"
        #         register_class = manager.base_dir / "register" / batch_name / "classes.py"
        #         manager.save(mode="register", file_path=register_data)
        #         manager.export(file_path=register_class)
        #     except Exception as e:
        #         print(f"批次 {batch_name} 对象注册失败: {e}")
        #         if input("是否继续处理下一批次? (y/n): ").lower() != 'y':
        #             return
        
        # 4. 第二阶段: 所有批次的模板注册
        # print("\n=== 开始模板注册阶段 ===")
        # manager.load(mode="register",file_path=manager.base_dir / "register" / "decks" / "data.dill")
        # for batch_name in config.get_batch_names():
        #     try:
        #         manager.register_templates(
        #             file_list=config.get_batch_files(batch_name),
        #             batch_name=batch_name
        #         )
        #         # 保存该批次的模板注册状态
        #         template_data = manager.base_dir / "template" / batch_name / "data.dill"
        #         template_class = manager.base_dir / "template" / batch_name / "classes.py"
        #         manager.save(mode="register", file_path=template_data)
        #         manager.export(file_path=template_class)
        #     except Exception as e:
        #         print(f"批次 {batch_name} 模板注册失败: {e}")
        #         if input("是否继续处理下一批次? (y/n): ").lower() != 'y':
        #             return

        # 5. 第三阶段: 所有批次的对象生成
        print("\n=== 开始对象生成阶段 ===")
        for batch_name in config.get_batch_names():
            try:
                manager.generate_objects(
                    file_list=config.get_batch_files(batch_name),
                    batch_name=batch_name
                )
                # 保存该批次的生成状态
                generate_data = manager.base_dir / "generate" / batch_name / "data.dill"
                generate_class = manager.base_dir / "generate" / batch_name / "classes.py"
                manager.save(mode="generate", file_path=generate_data)
                manager.export(file_path=generate_class)
            except Exception as e:
                print(f"批次 {batch_name} 对象生成失败: {e}")
                if input("是否继续处理下一批次? (y/n): ").lower() != 'y':
                    return
        
        # 6. 保存最终的完整状态
        final_register = manager.base_dir / "final" / "register.dill"
        final_generate = manager.base_dir / "final" / "generate.dill"
        final_class = manager.base_dir / "final" / "classes.py"
        manager.save(mode="register", file_path=final_register)
        manager.save(mode="generate", file_path=final_generate)
        manager.export(file_path=final_class)
        
        print("\n所有阶段处理完成!")
        
    except Exception as e:
        print(f"\n处理过程中出现错误: {e}")

if __name__ == "__main__":
    # 命令行参数解析
    parser = argparse.ArgumentParser(description='NDF文件解析工具')
    parser.add_argument('--version', type=str, default="M20250403",
                      help='游戏版本目录名 (例如: M20250403)')
    
    args = parser.parse_args()
    
    # 设置版本并运行
    config = ConfigManager().get_instance()
    try:
        config.set_version(args.version)
        main()
    except ValueError as e:
        print(f"错误: {e}")
        print("可用版本:")
        for version_dir in config.data_dir.iterdir():
            if version_dir.is_dir():
                print(f"  - {version_dir.name}")