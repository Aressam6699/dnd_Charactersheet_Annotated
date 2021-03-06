import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('imagesize')[0].text),
                     int(root.find('imagesize')[1].text),
                     member[0].text,
                     member[3].text,
                     int(member[9][1][0].text),
                     int(member[9][1][1].text),
                     int(member[9][3][0].text),
                     int(member[9][3][1].text),
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'occluded', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train']:
        image_path = os.path.join(os.getcwd(), 'collection/{}'.format(directory))
        print(image_path)
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/{}_dnd_anotated.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')


main()