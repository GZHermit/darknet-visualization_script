# -*- coding: utf-8 -*-
import subprocess

import matplotlib.pyplot as plt
import numpy as np
import global_variables as gv
import os

cfg_fp = gv.get_value('cfg_fp')
data_fp = gv.get_value('data_fp')
cls_fp = gv.get_value('cls_fp')
result_p = gv.get_value('result_p')
dataset_p = gv.get_value('dataset_p')
train_fn = gv.get_value('train_fn')
valid_fn = gv.get_value('valid_fn')
key_name = gv.get_value('key_name')


def draw():
    print("#------Start to draw mAP process!------#")
    steps = []
    mAP_value = []
    train_steps = os.listdir(result_p + '/')
    train_steps = [int(i) for i in train_steps if i != 'cache']
    train_steps.sort()
    plt.figure(figsize=(16,9))
    plt1 = plt.subplot(212)
    plt2 = plt.subplot(222)
    plt1.set_xticks([])
    plt1.set_yticks([])
    plt1.spines['right'].set_color('none')
    plt1.spines['top'].set_color('none')
    plt1.spines['bottom'].set_color('none')
    plt1.spines['left'].set_color('none')
    for train_step in train_steps:
        train_step = str(train_step)
        if 'cache' in train_step:
            continue
        mAP_log_fp = result_p + '/' + train_step + '/' + 'mAP.log'
        with open(cls_fp, 'r') as f:
            content = f.readlines()
            classes = [i.strip('\n') for i in content]
        classes.append('Mean AP')
        with open(mAP_log_fp, 'r') as f:
            content = f.readlines()
            mAP_value.append([float(i.split()[1]) for i in content])
            steps.append(train_step)
        plt1.table(cellText=mAP_value, colWidths=[0.18] * len(classes), colLabels=classes, rowLabels=steps, loc='best')
        plt2.set_xlabel("train_steps")
        plt2.set_ylabel("mAP")
        plt2.grid(True)
        plt2.set_title(key_name + '/' + str(train_step))
        for i in range(len(classes)):
            plt2.plot(steps, mAP_value, label="%s" % classes[i])
    plt.savefig(result_p + '/cache/mAP.png', bbox_inches='tight',dpi=200)
    plt.show()
    plt.close()
