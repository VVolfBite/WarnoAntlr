import pickle
import sys
WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
import config

class DataManager:
    def __init__(self, pkl_path):
        self.pkl_path = pkl_path
        self.data = None

        try:
            # 从pkl文件中加载数据
            with open(self.pkl_path, 'rb') as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            print(f"Error: The file {self.pkl_path} does not exist.")
        except pickle.UnpicklingError:
            print(f"Error: Failed to unpickle data from {self.pkl_path}.")

    def get_data_by_key(self, key):
        if self.data and key in self.data:
            return self.data[key]
        else:
            return None

    def get_data_by_class(self, class_name : str | list[str]):
        if isinstance(class_name,str):
            class_name = [class_name]
        result = {}
        for key, instance in self.data.items():
            instance_class_name = type(instance).__name__
            if instance_class_name in class_name:
                result[key] = instance
        return result
    

    
# 测试代码
if __name__ == "__main__":
    # 假设我们有一个.pkl文件路径
    data_manager = DataManager('./global.pkl')

    # 获取加载的数据
    data = data_manager.get_data_by_class("TCapaciteDescriptor")
    print(data)
