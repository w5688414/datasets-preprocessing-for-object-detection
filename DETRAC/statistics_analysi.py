
import os

#原图片的地址
pictureBasePath=r"Insight-MVT_Annotation_Train"
picturefolder = os.listdir(pictureBasePath)

num=0
log=open("picture_statistical.txt","w")
for pic_folder_item in picturefolder:
    pic_file_path=os.path.join(pictureBasePath,pic_folder_item)
    print(pic_file_path)
    file_lists=os.listdir(pic_file_path)
    num=num+len(file_lists)
    print(len(file_lists))
    log.write(pic_file_path+" "+str(len(file_lists))+"\n")
print(num)
log.write(str(num)+"\n")
