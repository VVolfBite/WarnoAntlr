"""路径解析器模块
提供统一的路径解析和数据管理功能

主要功能:
1. 路径解析 - 处理不同格式的路径（绝对路径、相对路径、命名空间路径）
2. 数据管理 - 基于路径的数据存储和访问
3. 序列化 - 数据的保存和加载
"""

from pathlib import Path
from typing import List, Dict, Any, Union, Optional
import pickle

class PathResolver:
    """路径解析与数据管理器"""
    def __init__(self):
        self.data_dict = {}   # 统一的数据存储

    def _get_nested_value(self, obj: Any, keys: List[str]) -> Any:
        """获取嵌套对象中的值
        Args:
            obj: 要访问的对象
            keys: 键路径列表
        Returns:
            找到的值或None
        """
        current = obj
        for key in keys:
            if current is None:
                return None
                
            # 处理列表/元组索引
            if isinstance(current, (list, tuple)) and key.isdigit():
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return None
            # 处理字典
            elif isinstance(current, dict):
                current = current.get(key)
            # 处理对象属性
            elif hasattr(current, key):
                current = getattr(current, key)
            else:
                return None
        return current

    def _set_nested_value(self, keys: List[str], value: Any) -> None:
        """设置嵌套字典中的值
        Args:
            keys: 键路径列表
            value: 要设置的值
        """
        current = self.data_dict
        for i, key in enumerate(keys[:-1]):
            if key not in current:
                current[key] = {}
            current = current[key]
            
        current[keys[-1]] = value

    def resolve_path(self, path: Union[str, List[str]], namespace: Optional[str] = None) -> List[str]:
        """解析路径为标准格式
        Args:
            path: 路径（字符串或列表）
            namespace: 命名空间
        Returns:
            标准化的路径键列表
        """
        if isinstance(path, list):
            path = '/' + '/'.join(str(p) for p in path)
        elif not isinstance(path, str):
            raise TypeError("路径必须是字符串或列表")
            
        path = path.strip()
        
        # 处理不同类型的路径
        if path.startswith('$'):
            result = path.lstrip('$/').strip('/')
        elif path.startswith('~/'):
            if not namespace:
                raise ValueError("相对路径必须提供命名空间")
            if namespace.startswith('$'):
                namespace = namespace.lstrip('$/')
            elif not namespace.startswith('/'):
                raise ValueError(f"命名空间 '{namespace}' 必须以 '/' 或 '$' 开头")
            result = f"{namespace.rstrip('/')}/{path[2:].strip('/')}"
        else:
            result = path.strip('/')
            
        # 返回路径键列表
        return result.split('/') if result else []

    def set(self, path: str, value: Any, namespace: Optional[str] = None):
        """设置路径对应的值
        Args:
            path: 路径
            value: 值
            namespace: 命名空间
        """
        keys = self.resolve_path(path, namespace)
        if not keys:
            return
        self._set_nested_value(keys, value)

    def get(self, path: str, namespace: Optional[str] = None) -> Any:
        """获取路径对应的值
        Args:
            path: 路径
            namespace: 命名空间
        Returns:
            存储的值
        """
        keys = self.resolve_path(path, namespace)
        if not keys:
            return None
        return self._get_nested_value(self.data_dict, keys)

    def merge(self, other_dict: Dict[str, Any], namespace: Optional[str] = None):
        """合并其他字典
        Args:
            other_dict: 要合并的字典
            namespace: 命名空间
        """
        for path, value in other_dict.items():
            self.set(path, value, namespace)

    def to_dict(self) -> Dict[str, Any]:
        """返回原始字典形式
        Returns:
            完整的数据字典
        """
        return self.data_dict.copy()

    def clear(self):
        """清除所有数据"""
        self.data_dict.clear()

    def save(self, file_path: Path):
        """保存到文件
        Args:
            file_path: 保存路径
        """
        with open(file_path, 'wb') as f:
            pickle.dump(self.data_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, file_path: Path):
        """从文件加载
        Args:
            file_path: 文件路径
        """
        with open(file_path, 'rb') as f:
            self.data_dict = pickle.load(f)

def test_path_resolver():
    """测试PathResolver的功能"""
    resolver = PathResolver()
    
    # 测试1: 基本的字典嵌套
    print("\n=== 测试1: 基本的字典嵌套 ===")
    resolver.set("$/A/B/C", "value1")
    print("设置 $/A/B/C = value1")
    print("获取 $/A/B/C =", resolver.get("$/A/B/C"))
    print("完整数据字典:", resolver.data_dict)
    
    # 测试2: 对象属性访问
    print("\n=== 测试2: 对象属性访问 ===")
    class TestObj:
        def __init__(self):
            self.x = 100
            self.y = {"z": 200}
    
    resolver.set("$/test", TestObj())
    print("设置 $/test = TestObj()")
    print("获取 $/test/x =", resolver.get("$/test/x"))
    print("获取 $/test/y/z =", resolver.get("$/test/y/z"))
    
    # 测试3: 列表访问
    print("\n=== 测试3: 列表访问 ===")
    resolver.set("$/list", [1, 2, {"key": "value"}])
    print("设置 $/list = [1, 2, {'key': 'value'}]")
    print("获取 $/list/0 =", resolver.get("$/list/0"))
    print("获取 $/list/2/key =", resolver.get("$/list/2/key"))
    
    # 测试4: 相对路径
    print("\n=== 测试4: 相对路径 ===")
    resolver.set("$/namespace/data", {"value": 300})
    print("设置 $/namespace/data = {'value': 300}")
    print("获取 ~/data/value (namespace=$/namespace) =", 
          resolver.get("~/data/value", namespace="$/namespace"))
    
    # 测试5: 错误处理
    print("\n=== 测试5: 错误处理 ===")
    print("获取不存在的路径 $/nonexist =", resolver.get("$/nonexist"))
    print("获取不存在的属性 $/test/nonexist =", resolver.get("$/test/nonexist"))
    print("获取越界的列表索引 $/list/99 =", resolver.get("$/list/99"))

if __name__ == "__main__":
    test_path_resolver()

