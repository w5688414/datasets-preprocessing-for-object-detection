import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # print(root)
        print(root.find('filename').text)
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[1].text),   #width
                     int(root.find('size')[2].text),   #height
                     member[0].text,
                     int(member[4][0].text),
                     int(float(member[4][1].text)),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train','test','validation']:
        xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
    # image_path = os.path.join(os.getcwd(), 'merged_xml')
        xml_df = xml_to_csv(xml_path)
        # xml_df.to_csv('whsyxt.csv', index=None)
        xml_df.to_csv('data/DETRAC_{}_labels.csv'.format(directory), index=None)
    print('Successfully converted xml to csv.')


main()
