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
    # classes = ['person', 'car', 'car_night', 'electric bicycle', 'bicycle']
    with open(cls_fp, 'r') as f:
        classes = f.readlines()
        classes = [cls.strip('\n') for cls in classes]
    if len(classes) > 5:
        print("The number of the class is too large!")
        exit()
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255), (0, 0, 0)]
    valid_fp = dataset_p + 'ImageSets/Main/' + valid_fn
    image_ids = open(valid_fp, 'r').read().strip().split()
    xml_p = dataset_p + '/Annotations'
    img_p = dataset_p + '/JPEGImages'
    if not os.path.exists(result_p + '/%s/imgdrawed' % args.key_name):
        os.makedirs(result_p + '/%s/imgdrawed' % args.key_name)

    for image_id in image_ids:
        # 加载xml文件中的w,h,classe
        in_xmlfile = open(xml_p + '%s.xml' % (image_id))
        tree = ET.parse(in_xmlfile)
        root = tree.getroot()
        img = Image.open(img_p + '%s.jpg' % (image_id))
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
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymax').text))

            draw = ImageDraw.Draw(img)
            try:
                draw.rectangle(b, outline=colors[cls_id])
            except:
                draw.rectangle(b, outline=(cls_id * 51))
        img.save(result_p + '/%s/imgdrawed/%s.jpg' % (args.key_name, image_id))
