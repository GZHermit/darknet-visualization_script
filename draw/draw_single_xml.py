# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from PIL import Image, ImageDraw
import global_variables as gv

cfg_fp = gv.get_value('cfg_fp')
data_fp = gv.get_value('data_fp')
cls_fp = gv.get_value('cls_fp')
result_p = gv.get_value('result_p')
weight_p = gv.get_value('weight_p')
dataset_p = gv.get_value('dataset_p')
train_fn = gv.get_value('train_fn')
valid_fn = gv.get_value('valid_fn')



def draw(args):
    with open(cls_fp, 'r') as f:
        classes = f.readlines()
        classes = [cls.strip('\n') for cls in classes]
    if len(classes) > 5:
        print("The number of the class is too large!")
        exit()
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255), (0, 0, 0)]
    xmldir = '/home/anngic/dataset/data_coco/val2014/Annotations/'
    imgdir = '/home/anngic/dataset/data_coco/val2014/JPEGImages/'
    image_id = 'COCO_val2014_000000000872'
    in_xmlfile = open(xmldir + '%s.xml' % (image_id))
    tree = ET.parse(in_xmlfile)
    root = tree.getroot()
    img = Image.open(imgdir + '%s.jpg' % (image_id))
    print(image_id)

    for obj in root.iter('object'):
        try:
            cls = obj.find('name').text
        except:
            continue
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text), float(xmlbox.find('xmax').text),float(xmlbox.find('ymax').text))
        print(b)
        draw = ImageDraw.Draw(img)
        if cls_id == 0:
            draw.rectangle(b, outline=(255, 0, 0))
        if cls_id == 1:
            draw.rectangle(b, outline=(0, 255, 0))
        if cls_id == 2:
            draw.rectangle(b, outline=(0, 0, 255))
        if cls_id == 3:
            draw.rectangle(b, outline=(255, 255, 255))
        if cls_id == 4:
            draw.rectangle(b, outline=(0, 0, 0))
    img.save('./%s_draw_new.jpg' % (image_id))

