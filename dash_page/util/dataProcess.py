import sys
import pickle
WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

class Suffix:
    Distance = "m"  # 距离
    Area = "m^2"  # 面积
    Speed = "m/s"  # 速度
    Angle = "deg"  # 角度
    Percentage = "%"  # 百分比
    Duration = "s"  # 时间
    Mass = "kg"  # 质量
    Force = "N"  # 力
    Energy = "J"  # 能量
    Pressure = "Pa"  # 压力
    Length = "km"  # 长度
    LengthCm = "cm"  # 长度（厘米）
    TimeMs = "ms"  # 时间（毫秒）
    TimeMin = "min"  # 时间（分钟）
    TimeHr = "h"  # 时间（小时）
    Rotation = "rpm"  # 转速
    Frequency = "hz"  # 频率
    AngleRad = "rad"  # 弧度
    ElectricCurrent = "A"  # 电流
    Voltage = "V"  # 电压
    Power = "W"  # 功率

class DataManager:
    def __init__(self, pkl_path):
        self.pkl_path = pkl_path
        self.data = None

        try:
            # 从pkl文件中加载数据
            with open(self.pkl_path, "rb") as f:
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

    def get_data_by_class(self, class_name: str | list[str]):
        if isinstance(class_name, str):
            class_name = [class_name]
        result = {}
        for key, instance in self.data.items():
            instance_class_name = type(instance).__name__
            if instance_class_name in class_name:
                result[key] = instance
        return result

class DataFormatter:
    translation_dict = {
        "MinMaxCategory": "所属类型",
        "TraitsToken": "特性词条",
        "IsSubAmmunition": "描述对象为子武器",
        "AffecteParNombre": "描述对象因数量属性倍增",
        "Arme.Family": "伤害所属族",
        "Arme.Index": "伤害索引号",
        "PhysicalDamages": "基底伤害",
        "RadiusSplashPhysicalDamagesGRU": "基底伤害溅射半径",
        "SuppressDamages": "压制伤害",
        "RadiusSplashSuppressDamagesGRU": "压制伤害溅射半径",
        "AllowSuppressDamageWhenNoImpact": "允许未命中造成压制",
        "ForceHitTopArmor": "强制攻顶",
        "TargetOnlyOneUnitInDistrict": "仅针对城区中的单一单位",
        "PorteeMaximaleGRU": "对地最大射程",
        "PorteeMaximaleTBAGRU": "对直升机最大射程",
        "PorteeMaximaleHAGRU": "对空最大射程",
        "PorteeMinimaleGRU": "对地最小射程",
        "PorteeMinimaleTBAGRU": "对直升机最小射程",
        "PorteeMinimaleHAGRU": "对空最小射程",
        "Base": "基础准度",
        "Idling": "静止准度",
        "Moving": "移动准度",
        "Targeted": "被瞄准度",
        "BaseCriticModifier": "基础暴击效果概率",
        "DistanceToTarget": "准度随距离修正",
        "MaxSuccessiveHitCount": "最大连射长度",
        "CanShootWhileMoving": "允许移动攻击",
        "DispersionAtMaxRangeGRU": "最大射程下散布",
        "DispersionAtMinRangeGRU": "最小射程下散布",
        "CorrectedShotDispersionMultiplier": "校正散布修正",
        "DispersionWithoutSorting": "乱序射击",
        "AngleDispersion": "散布角度",
        "TempsDeVisee": "瞄准时间",
        "TempsEntreDeuxSalves": "装填时间",
        "TempsEntreDeuxTirs": "射击间隔",
        "NbTirParSalves": "装填前发射次数",
        "CorrectedShotAimtimeMultiplier": "校正射击瞄准时间修正",
        "TempsEntreDeuxSalves_Min": "最小射击间隔",
        "TempsEntreDeuxSalves_Max": "最大射击间隔",
        "CanShootOnPosition": "允许强制攻击",
        "NbSalvosShootOnPosition": "强制攻击装填次数",
        "TirIndirect": "仅能直射",
        "TirReflexe": "无法追踪目标",
        "InterdireTirReflexe": "允许追踪目标",
        "TargetUnitCenter": "瞄准目标中心",
        "PiercingWeapon": "为穿甲武器",
        "IsHarmlessForAllies": "无友军伤害",
        "CanHarmAirplanes": "可对飞机造成伤害",
        "Guidance": "引导方式",
        "IsFireAndForget": "射后不理",
        "MissileDescriptor": "挂载导弹",
        "TandemCharge": "串联弹头",
        "MissileTimeBetweenCorrections": "导弹射击时间修正",
        "SupplyCost": "补给消耗",
        "SmokeDescriptor": "烟雾类型",
        "FireDescriptor": "火焰类型",
        "FireTriggeringProbability": "引火概率",
        "IgnoreInflammabilityConditions": "忽视不可引火条件"
    }
    @classmethod
    def set_dict(cls, dict: dict):
        cls.translation_dict = dict

    @staticmethod
    def _trans(key):
        if key in DataFormatter.translation_dict:
            return DataFormatter.translation_dict[key]
        else:
            return key

    def __init__(self, key, value, suffix, caption: str = "", show: bool = True):
        self.key = key
        self.value = value
        self.caption = caption
        self.suffix = suffix
        self.show = show

    def Key(self):
        return DataFormatter._trans(self.key)

    def Value(self):
        value = self.value
        suffix = self.suffix if self.suffix else ""
        if self.value is None:
            value = "未设置"
        elif isinstance(self.value, bool):
            value = "是" if self.value else "否"
        elif isinstance(self.value, (int, float)):
            value = "默认" if self.value == -1 or self.value == -1.0 else str(self.value)
        elif isinstance(self.value, (list, tuple)):
            value = f"[ {' , '.join(DataFormatter._trans(repr(item)) for item in self.value)} ]"
        else:
            value = DataFormatter._trans(str(self.value))
        return value + suffix

    def Caption(self):
        return DataFormatter._trans(self.caption)



if __name__ == "__main__":
    # 假设我们有一个.pkl文件路径
    data_manager = DataManager("./global.pkl")

    # 获取加载的数据
    data = data_manager.get_data_by_class("TAmmunitionDescriptor")

    print(data)
