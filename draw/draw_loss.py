import commands

import matplotlib.pyplot as plt
import numpy as np
import global_variables as gv

cfg_fp = gv.get_value('cfg_fp')
data_fp = gv.get_value('data_fp')
cls_fp = gv.get_value('cls_fp')
result_p = gv.get_value('result_p')
dataset_p = gv.get_value('dataset_p')
train_fn = gv.get_value('train_fn')
valid_fn = gv.get_value('valid_fn')
key_name = gv.get_value('key_name')

def draw(args):
    loss_fp = result_p + '/cache/' + 'avgloss.log'
    # mAP_fp = result_fp + '/'  + 'mAP.log'

    display = 10  # solver
    test_interval = 100  # solver

    train_output = commands.getoutput(
        "cat " + loss_fp + " | grep 'avg,' | awk '{print $3}'")  # train loss

    train_loss = train_output.split("\n")
    for i in range(len(train_loss)):
        if float(train_loss[i]) > 16 :
            train_loss[i] = str(16.0)

    train_output = commands.getoutput(
        "cat " + loss_fp + " | grep 'avg,' | awk '{print $1}'")  # train loss

    train_batch = train_output.split("\n")
    train_batch = [i.strip(":") for i in train_batch]

    # with open(cls_fp, 'r') as f:
    #     content = f.readlines()
    #     classes = [i.strip('\n') for i in content]
    # with open(mAP_fp, 'r') as f:
    #     content = f.readlines()
    #     mAP_value = [[float(i.split()[1]) for i in content]]
    # plt.table(cellText=mAP_value, colWidths=[0.18] * len(classes), colLabels=classes, loc='best')
    # my_table = plt.table(cellText=mAP_value, colWidths=[0.1] * len(classes), rowLabels=classes, loc='best')
    plt.plot(train_batch, train_loss, label="avgloss")

    plt.xlabel('Iteration')
    plt.ylabel('Train Loss')

    # plt.legend([l1], [''], loc='upper right')
    plt.title(key_name)
    plt.savefig(result_p + '/cache/avgloss.png', bbox_inches='tight')
    plt.show()

