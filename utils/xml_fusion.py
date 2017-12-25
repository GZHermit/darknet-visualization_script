import os

import xml.etree.ElementTree as ET


def check(obj1, obj2):
    if int(obj1[0]) > int(obj2[2]):
        return False
    if int(obj1[1]) > int(obj2[3]):
        return False
    if int(obj2[0]) > int(obj1[2]):
        return False
    if int(obj2[1]) > int(obj1[3]):
        return False
    if int(obj1[0]) >= (int(obj2[0]) + int(obj2[2])) / 2:
        return False
    if int(obj2[0]) >= (int(obj1[0]) + int(obj1[2])) / 2:
        return False

    return True


def createElem(root, obj1, obj2):
    newObj = ET.Element('object')
    root.append(newObj)
    ET.SubElement(newObj, 'name').text = 'rider'
    ET.SubElement(newObj, 'pose').text = 'Unspecified'
    ET.SubElement(newObj, 'truncated').text = '0'
    ET.SubElement(newObj, 'difficult').text = '0'
    bndbox = ET.SubElement(newObj, 'bndbox')
    ET.SubElement(bndbox, 'xmin').text = min(obj1[0], obj2[0])
    ET.SubElement(bndbox, 'ymin').text = min(obj1[1], obj2[1])
    ET.SubElement(bndbox, 'xmax').text = max(obj1[2], obj2[2])
    ET.SubElement(bndbox, 'ymax').text = max(obj1[3], obj2[3])


def deleteElem(root, obj1, obj2):
    for c in root.findall('object'):
        xmin = c.findall('./bndbox/xmin')[0].text
        ymin = c.findall('./bndbox/ymin')[0].text
        xmax = c.findall('./bndbox/xmax')[0].text
        ymax = c.findall('./bndbox/ymax')[0].text
        if obj1[0] == xmin and obj1[1] == ymin and obj1[2] == xmax and obj1[3] == ymax:
            print("OK!")
            root.remove(c)
        elif obj2[0] == xmin and obj2[1] == ymin and obj2[2] == xmax and obj2[3] == ymax:
            print("OK!")
            root.remove(c)

xmls = os.listdir('./xmlbefore1206/')
for xml in xmls:
    tree = ET.parse('./xmlbefore1206/' + xml)
    root = tree.getroot()
    objs = []

    for c in root.findall('object'):
        name = c.find('name').text
        xmin = c.findall('./bndbox/xmin')[0].text
        ymin = c.findall('./bndbox/ymin')[0].text
        xmax = c.findall('./bndbox/xmax')[0].text
        ymax = c.findall('./bndbox/ymax')[0].text
        objs.append((name, (xmin, ymin, xmax, ymax)))
    print(objs)
    lens = len(objs)
    flags = [False for i in range(lens)]
    for i in range(lens):
        if objs[i][0] == 'person' and not flags[i]:
            for j in range(i + 1, lens):
                if objs[j][0] == 'electric bicycle' and not flags[j] and check(objs[i][1], objs[j][1]):
                    print("person:", i, j)
                    createElem(root, objs[i][1], objs[j][1])
                    deleteElem(root, objs[i][1], objs[j][1])
                    flags[i] = flags[j] = True
                    break
                if objs[j][0] == 'bicycle' and not flags[j] and check(objs[i][1], objs[j][1]):
                    print("person:", i, j)
                    createElem(root, objs[i][1], objs[j][1])
                    deleteElem(root, objs[i][1], objs[j][1])
                    flags[i] = flags[j] = True
                    break
        elif objs[i][0] == 'electric bicycle' and not flags[i]:
            for j in range(i + 1, lens):
                if objs[j][0] == 'person' and not flags[j] and check(objs[i][1], objs[j][1]):
                    print("bicycle:", i, j)
                    createElem(root, objs[i][1], objs[j][1])
                    deleteElem(root, objs[i][1], objs[j][1])
                    flags[i] = flags[j] = True
                    break
        elif objs[i][0] == 'bicycle' and not flags[i]:
            for j in range(i + 1, lens):
                if objs[j][0] == 'person' and not flags[j] and check(objs[i][1], objs[j][1]):
                    print("bicycle:", i, j)
                    createElem(root, objs[i][1], objs[j][1])
                    deleteElem(root, objs[i][1], objs[j][1])
                    flags[i] = flags[j] = True
                    break
    tree.write('./xmlbefore1206/' + xml, encoding='utf-8', xml_declaration=True)

