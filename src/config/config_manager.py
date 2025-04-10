import os
from pathlib import Path
import sys
from typing import Dict, List, Tuple, Optional

class ConfigManager:
    """配置管理类
    
    负责:
    1. 项目路径管理
    2. 文件列表管理
    3. 输出配置管理
    """
    _instance = None
    
    def __init__(self):
        # 基础路径配置
        self.project_root = Path(__file__).parent.parent.parent
        self.src_path = self.project_root / "src"
        self.data_path = self.project_root / "data"
        self.output_path = self.project_root / "src/extractor"
        
        # 确保必要目录存在
        self.output_path.mkdir(exist_ok=True)
        
        # 文件配置
        self.process_file_list: List[Tuple[str, str]] = []
        self.register_file = self.output_path / "register.pkl"
        self.generate_file = self.output_path / "generate.pkl"
        self.log_file = self.output_path / "log.txt"
        self.class_file = self.output_path / "extract_class.py"
        
        # 版本路径
        self.version = self.data_path / "M20250403"
        
        # 类定义文件配置
        self.class_file_names = [
            "test_class.py",
            "refined_class.py",
            "extract_class.py",
            "backup_class.py"
        ]
        
        # Python路径配置
        if str(self.project_root) not in sys.path:
            sys.path.append(str(self.project_root))
    
    @classmethod
    def get_instance(cls) -> 'ConfigManager':
        """获取单例实例"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def add_file(self, file_path: str, namespace: str = "/") -> None:
        """添加要处理的文件
        
        Args:
            file_path: 相对于data目录的文件路径
            namespace: 命名空间
        """
        self.process_file_list.append((file_path, namespace))
    
    def get_full_path(self, file_path: str) -> Path:
        """获取文件完整路径"""
        return self.data_path / file_path
    
    def get_class_paths(self) -> List[Path]:
        """获取类定义文件路径列表"""
        return [
            self.src_path / "extractor" / file_name
            for file_name in self.class_file_names
        ]
        
    def get_output_path(self, file_name: str) -> Path:
        """获取输出文件路径"""
        return self.output_path / file_name