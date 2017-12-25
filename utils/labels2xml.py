import os
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np

img_path = '/home/anngic/dataset/data_coco/val2014/JPEGImages/'
labels_path = '/home/anngic/dataset/data_coco/val2014/labels/'
annotations_path = '/home/anngic/dataset/data_coco/val2014/Annotations/'
labels = os.listdir(labels_path)
classes = ['person', 'car', 'car_night', 'electric bicycle', 'bicycle']


def write_xml(filepath, labeldicts):
    root = ET.Element('annotations')
    for labeldict in labeldicts:
        objects = ET.SubElement(root, 'object')
        ET.SubElement(objects, 'name').text = labeldict['name']
        ET.SubElement(objects, 'pose').text = 'Unspecified'
        ET.SubElement(objects, 'truncated').text = '0'
        ET.SubElement(objects, 'difficult').text = '0'
        bndbox = ET.SubElement(objects, 'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(int(labeldict['xmin']))
        ET.SubElement(bndbox, 'ymin').text = str(int(labeldict['ymin']))
        ET.SubElement(bndbox, 'xmax').text = str(int(labeldict['xmax']))
        ET.SubElement(bndbox, 'ymax').text = str(int(labeldict['ymax']))
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8')


for label in labels:
    with open(labels_path + label, 'r') as f:
        contents = f.readlines()
        labeldicts = []
        for content in contents:
            img = np.array(Image.open(img_path + label.strip('.txt') + '.jpg'))
            sh, sw = img.shape[0], img.shape[1]
            content = content.strip('\n').split()
            x = float(content[1]) * sw
            y = float(content[2]) * sh
            w = float(content[3]) * sw
            h = float(content[4]) * sh
            new_dict = {'name': classes[int(content[0])],
                        'difficult': '0',
                        'xmin': x + 1 - w / 2,
                        'ymin': y + 1 - h / 2,
                        'xmax': x + 1 + w / 2,
                        'ymax': y + 1 + h / 2
                        }
            labeldicts.append(new_dict)
        write_xml(annotations_path + label.strip('.txt') + '.xml', labeldicts)
