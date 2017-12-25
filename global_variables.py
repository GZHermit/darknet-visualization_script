# coding:utf-8
def _init():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    _global_dict[key] = value


def get_value(key, defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue


def get_all_value():
    try:
        return _global_dict
    except KeyError:
        return None


class Args:
    def __init__(self):
        self.darknet_p = ''
        self.cfg_fn = ''
        self.data_fn = ''
        self.gpus = ''
        self.order = ''
        self.draw_option = None
        self.compute_step = None
        self.valid_step = None
