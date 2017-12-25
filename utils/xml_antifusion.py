# coding:utf-8
import os
import xml.etree.ElementTree as ET


def createElem(root, obj):
    print ("create:{}", obj)
    newObj = ET.Element('object')
    root.append(newObj)
    ET.SubElement(newObj, 'name').text = obj[0]
    ET.SubElement(newObj, 'pose').text = 'Unspecified'
    ET.SubElement(newObj, 'truncated').text = '0'
    ET.SubElement(newObj, 'difficult').text = '0'
    bndbox = ET.SubElement(newObj, 'bndbox')
    ET.SubElement(bndbox, 'xmin').text = obj[1][0]
    ET.SubElement(bndbox, 'ymin').text = obj[1][1]
    ET.SubElement(bndbox, 'xmax').text = obj[1][2]
    ET.SubElement(bndbox, 'ymax').text = obj[1][3]


def deleteElem(root, obj):
    for c in root.findall('object'):
        if c.find('name').text != obj[0]: continue
        xmin = c.findall('./bndbox/xmin')[0].text
        ymin = c.findall('./bndbox/ymin')[0].text
        xmax = c.findall('./bndbox/xmax')[0].text
        ymax = c.findall('./bndbox/ymax')[0].text
        if obj[1][0] == xmin and obj[1][1] == ymin and obj[1][2] == xmax and obj[1][3] == ymax:
            root.remove(c)
            # if obj[0] == xmin and obj[1] == ymin and obj[2] == xmax and obj[3] == ymax:
            #     print ("hehe")
            #     root.remove(c)


def resolve_object(xml_path, xml_name, keys):
    tree = ET.parse(xml_path + xml_name)
    root = tree.getroot()
    objs = []

    for c in root.findall('object'):
        name = c.find('name').text
        if name not in keys: continue
        xmin = c.findall('./bndbox/xmin')[0].text
        ymin = c.findall('./bndbox/ymin')[0].text
        xmax = c.findall('./bndbox/xmax')[0].text
        ymax = c.findall('./bndbox/ymax')[0].text
        objs.append((name, (xmin, ymin, xmax, ymax)))
    return tree, root, objs


def check(src_coord, dest_coord):
    # src 被包含在 dest 之内
    src_xmin, src_ymin, src_xmax, src_ymax = src_coord
    dest_xmin, dest_ymin, dest_xmax, dest_ymax = dest_coord
    # if src_xmin >= dest_xmin and src_ymin >= dest_ymin and src_xmax <= dest_xmax and src_ymax <= dest_ymax:
    #     return True
    # else:
    #     return False
    if src_ymax <= dest_ymin or dest_ymax <= src_ymin:
        return False
    if src_xmax <= dest_xmin or dest_xmax <= src_xmin:
        return False
    return True


def antifusion(origin_xml, reference_xml, new_xml):
    xmls = os.listdir(origin_xml)

    for xml in xmls:
        # if xml != '0094394.xml': continue
        if not os.path.exists(reference_xml + xml): continue
        origin_tree, origin_root, origin_objs = resolve_object(origin_xml, xml, ['rider', ])
        _, _, reference_objs = resolve_object(reference_xml, xml, ['person', 'bicycle', 'electric bicycle'])
        # print (origin_objs)
        for oobj in origin_objs:
            for robj in reference_objs:
                if check(robj[1], oobj[1]):
                    createElem(origin_root, robj)
            deleteElem(origin_root, oobj)
        flag = 0
        for c in origin_root.findall('object'):
            c_name = c.find('name').text
            if c_name not in ['person', 'bicycle', 'electric bicycle']: continue
            c_xmin = c.findall('./bndbox/xmin')[0].text
            c_ymin = c.findall('./bndbox/ymin')[0].text
            c_xmax = c.findall('./bndbox/xmax')[0].text
            c_ymax = c.findall('./bndbox/ymax')[0].text
            sflag = 0
            for cc in origin_root.findall('object'):
                if sflag <= flag: continue
                sflag += 1
                cc_name = cc.find('name').text
                if cc_name not in ['person', 'bicycle', 'electric bicycle'] or c_name != cc_name: continue
                cc_xmin = c.findall('./bndbox/xmin')[0].text
                cc_ymin = c.findall('./bndbox/ymin')[0].text
                cc_xmax = c.findall('./bndbox/xmax')[0].text
                cc_ymax = c.findall('./bndbox/ymax')[0].text
                if c_xmin == cc_xmin and c_ymin == cc_ymin and c_xmax == cc_xmax and c_ymax == cc_ymax:
                    origin_root.remove(cc)
            flag += 1
        # for c in origin_root.findall('object'):
        #     print(c.find('name').text)
        origin_tree.write(new_xml + xml, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    origin_xml = '/home/gzh/Workspace/Dataset/new_xml_yanminjia/rider_check1/'  # 含有rider的xml
    reference_xml = '/home/gzh/Workspace/Dataset/anngic_20171207.backup/xmlbefore1206/'
    new_xml = '/home/gzh/Workspace/Dataset/new_xml_yanminjia/final/'
    antifusion(origin_xml, reference_xml, new_xml)
