# -*- coding: utf-8 -*-
import os


def check_makedir(p):
    if not os.path.exists(p):
        os.makedirs(p)
