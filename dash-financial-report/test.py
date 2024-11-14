import pickle
import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
import config
from antlr4 import *
from src.parsers.parser_interface import ParserInterface
from src.parsers.register_class.RClass import *

with open("global.pkl",'rb') as f:
    global_dict  = pickle.load(f)
global_dict = ParserInterface.refer_class(global_dict,global_dict)

ammo_object = global_dict['Ammo_Canon_AP_105mm_L7A3_Leo1V']
weapon_object = global_dict['WeaponDescriptor_Su_25_he_SOV']

def get_key_by_value( target_value):
    for key, value in global_dict.items():
        if value == target_value:
            return key
    return None 

print(get_key_by_value(weapon_object))