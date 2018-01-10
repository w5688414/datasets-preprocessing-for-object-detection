
import os
import random
import shutil
import sys

#xml路径的地址 train
# XmlPath=r'./COCO/coco_xml'
#原图片的地址 train
# pictureBathPath=r"./COCO/train2014"
#保存图片的地址
#train
# saveBasePath=r"./COCO/coco_train_images" 
#val
# XmlPath=r'./COCO/coco_val_xml'
# #原图片的地址 train
# pictureBathPath=r"./COCO/val2014"
# saveBasePath=r"./COCO/coco_val_images" 
XmlPath=sys.argv[1]
val_pictureBasePath=sys.argv[2]
train_pictureBasePath=sys.argv[3]
saveBasePath=sys.argv[4]

total_xml = os.listdir(XmlPath)
num=len(total_xml)
list=range(num)
print("xml file total number",num)

count=0
for xml in total_xml:
    filename=xml.split(".")[0]
    filename=filename+".jpg"
   # print(filename)
    val_filePath=os.path.join(val_pictureBasePath,filename)
    train_filePath=os.path.join(train_pictureBasePath,filename)
    # print(filePath)
    if os.path.exists(val_filePath):
        # print(filePath+" not exists")
        filePath=val_filePath
    elif os.path.exists(train_filePath):
        filePath=train_filePath
    else:
        print(filename+" not exists")
        continue

    newfile=os.path.join(saveBasePath,filename)
    shutil.copyfile(filePath, newfile)
    count+=1
    if(count%1000==0):
        print(count)