
import os
import xml.etree.ElementTree as ET
from xml.dom.minidom import Document
import time
import sys
from tqdm import tqdm 

def ConvertVOCXml(file_path="",file_name=""):

     # 创建dom文档
    doc = Document()
    # 创建根节点
    annotation = doc.createElement('annotation')
    # 根节点插入dom树
    doc.appendChild(annotation)

    tree = ET.parse(file_name)
    root = tree.getroot()

    #读xml操作
    object_lists=[]
    for child in root:
        if(child.tag=="folder"):
            #print(child.tag, child.text)
            folder = doc.createElement("folder")
            #  folder.appendChild(doc.createTextNode(child.text))
            folder.appendChild(doc.createTextNode("VOC2007"))
            annotation.appendChild(folder)
        elif (child.tag == "filename"):
            #print(child.tag, child.text)
            filename = doc.createElement("filename")
            filename.appendChild(doc.createTextNode(child.text))
            annotation.appendChild(filename)
        elif (child.tag == "size"):  #解析size
            sizeimage = doc.createElement("size")
            imagewidth = doc.createElement("width")
            imageheight = doc.createElement("height")
            imagedepth = doc.createElement("depth")
            for size_child in child:
                if(size_child.tag=="width"):
                    # print(size_child.tag,size_child.text)
                    imagewidth.appendChild(doc.createTextNode(size_child.text))
                elif (size_child.tag == "height"):
                    # print(size_child.tag, size_child.text)
                    # height_value = int(size_child.text)
                    #print("图片的高度", height_value)
                    imageheight.appendChild(doc.createTextNode(size_child.text))
                elif (size_child.tag == "depth"):
                #print(size_child.tag, size_child.text)
                    imagedepth.appendChild(doc.createTextNode(size_child.text))
            
            sizeimage.appendChild(imagewidth)
            sizeimage.appendChild(imageheight)
            sizeimage.appendChild(imagedepth)
            annotation.appendChild(sizeimage)

        elif (child.tag == "object"):  #解析object
            singleObject={}
            for object_child in child:
                if (object_child.tag == "name"):
                    if(object_child.text=="person"):
                        singleObject["name"] = "person"
                    elif object_child.text=="car":
                        singleObject["name"] = "car"
                    elif object_child.text=="bus":
                        singleObject["name"] = "car"
                    elif object_child.text=="motorcycle":
                        singleObject["name"] = "car"
                    elif object_child.text=="train":
                        singleObject["name"] = "car"
                    elif object_child.text=="truck":
                        singleObject["name"] = "car"
                    else:
                        # print(file_name)
                        # print(object_child.text)
                        #singleObject["name"] = object_child.text
                        singleObject={}
                        break
                #singleObject["name"] = object_child.text
                elif(object_child.tag == "pose"):
                    singleObject["pose"] = object_child.text
                    # print(object_child.text)
                elif(object_child.tag == "truncated"):
                    singleObject["truncated"] = object_child.text
                    # print(object_child.text)
                elif(object_child.tag == "difficult"):
                    singleObject["difficult"] = object_child.text
                    # print(object_child.text)
                elif (object_child.tag == "bndbox"):
                    for bndbox_child in object_child:
                        if (bndbox_child.tag == "xmin"):
                            singleObject["xmin"] = bndbox_child.text
                            # print(bndbox_child.tag, bndbox_child.text)
                        elif (bndbox_child.tag == "ymin"):
                            # print(bndbox_child.tag, bndbox_child.text)
                            singleObject["ymin"] = bndbox_child.text
                        elif (bndbox_child.tag == "xmax"):
                            singleObject["xmax"] = bndbox_child.text
                        elif (bndbox_child.tag == "ymax"):
                            singleObject["ymax"] = bndbox_child.text
            object_length=len(singleObject)
            if(object_length>0):
                object_lists.append(singleObject)
    # print(object_lists)
    if(len(object_lists)==0):  #如果解析出来没有所需要的car person目标，则直接舍弃，不保留
        return False

    '''
    写入xml操作
    '''
    for singleObject in object_lists:
        object = doc.createElement('object')
        
        name = doc.createElement('name')

        truncated=doc.createElement('truncated')
        difficult=doc.createElement('difficult')
        pose=doc.createElement('pose')


        name.appendChild(doc.createTextNode(singleObject['name']))
    
        if(truncated in singleObject):
            truncated.appendChild(doc.createTextNode(singleObject['truncated']))
        else:
            truncated.appendChild(doc.createTextNode("0"))

        if(difficult in singleObject):
            difficult.appendChild(doc.createTextNode(singleObject['difficult']))
        else:
            difficult.appendChild(doc.createTextNode("0"))

        if(pose in singleObject):
            pose.appendChild(doc.createTextNode(singleObject['pose']))
        else:
            pose.appendChild(doc.createTextNode("Unspecified"))
   

        object.appendChild(name)
        object.appendChild(pose)
        object.appendChild(truncated)
        object.appendChild(difficult)
        
        bndbox = doc.createElement("bndbox")
        xmin = doc.createElement("xmin")
        ymin = doc.createElement("ymin")
        xmax = doc.createElement("xmax")
        ymax = doc.createElement("ymax")

        xmin.appendChild(doc.createTextNode(singleObject['xmin']))
        ymin.appendChild(doc.createTextNode(singleObject['ymin']))
        xmax.appendChild(doc.createTextNode(singleObject['xmax']))
        ymax.appendChild(doc.createTextNode(singleObject['ymax']))

        bndbox.appendChild(xmin)
        bndbox.appendChild(ymin)
        bndbox.appendChild(xmax)
        bndbox.appendChild(ymax)
        object.appendChild(bndbox)
        annotation.appendChild(object)
                    #print(bndbox_child.tag, bndbox_child.text)
    file_name=file_name.split("/")[-1]
    output_file=os.path.join(file_path,file_name)
    #file_path=os.path.join(file_path,file_name)

    #print(file_path)
    f = open(output_file, 'w')
    f.write(doc.toprettyxml(indent=' ' * 4))
    f.close()
    return True

def main():
    
    #train    
    # basePath="COCO/instance_train_annotation"
    # saveBasePath="COCO/coco_train_xml"
    #val
    # basePath="COCO/instance_val_annotation"
    # saveBasePath="COCO/coco_val_xml"
    basePath=sys.argv[1]
    saveBasePath=sys.argv[2]

    xml_base_paths=os.listdir(basePath)
    total_num=0
    flag=False
    print("正在转换")
    if os.path.exists(saveBasePath)==False: #判断文件夹是否存在
            os.makedirs(saveBasePath)

    # ConvertVOCXml(file_path=saveBasePath,file_name="COCO_train2014_000000000036.xml")
    # Start time
    start = time.time()

    log=open("xml_statistical.txt","w") #分析日志，进行排错
    for xml_base_path in tqdm(xml_base_paths):
        xml_path=os.path.join(basePath,xml_base_path)
        #    print(xml_path)
        list_xml=os.listdir(xml_path)
        for xml_file in list_xml:
            xml_file_path=os.path.join(xml_path,xml_file)
            #    print(xml_file_path)
            _file_name=xml_file_path.split("/")[-1]
            _output_file=os.path.join(saveBasePath,_file_name)
            if os.path.exists(_output_file)==True: 
                # print(_output_file)
                continue            #判断文件夹是否存在
            flag=ConvertVOCXml(file_path=saveBasePath,file_name=xml_file_path)
            if flag:
                total_num+=1
                if(total_num%10000==0):
                    print(total_num)
            else:
                log.write(xml_file_path+" "+str(total_num)+"\n")

                
    # End time
    end = time.time()
    seconds=end-start
    print( "Time taken : {0} seconds".format(seconds))
    print(total_num)
    log.write(str(total_num)+"\n")

if __name__ == '__main__':
    main()  