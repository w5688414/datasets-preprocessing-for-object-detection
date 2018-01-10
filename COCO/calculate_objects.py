import os
import xml.etree.ElementTree as ET
from xml.dom.minidom import Document
import time
import sys


def total_objects(file_name=""):
    tree = ET.parse(file_name)
    root = tree.getroot()
    count=0
    person_count=0
    car_count=0
     #读xml操作
    for child in root:   
        if (child.tag == "object"):  #解析object
            count+=1
            for object_child in child:
                if (object_child.tag == "name"):
                    if(object_child.text=="person"):
                        person_count+=1
                    elif object_child.text=="car":
                        car_count+=1
    # print(count)
    return count,person_count,car_count

def main():
    basePath=sys.argv[1]
    xml_base_paths=os.listdir(basePath)
    # print(xml_base_paths)
    objects_count=0
    persons_count=0
    cars_count=0
    total_count=0
    for xml_file in xml_base_paths:
        xml_file_path=os.path.join(basePath,xml_file)
        object_value,person_value,car_value=total_objects(xml_file_path)

        objects_count+=object_value   
        persons_count+=person_value
        cars_count+=car_value
        total_count=total_count+1
        # print(objects_count)
        if(total_count%1000==0):
            print(total_count)
    print("total xml files: "+str(total_count))
    print("total objects: "+str(objects_count))
    print("total persons: "+str(persons_count))
    print("total cars: "+str(cars_count))
    print("average objects per file: "+str(objects_count/float(total_count)))
    print("average persons per file: "+str(persons_count/float(total_count)))
    print("average cars per file: "+str(cars_count/float(total_count)))
    

if __name__ == '__main__':
    main()