
import os
import random
import time
import shutil

xmlfilepath=r'xml_test'
saveBasePath=r"./annotations"

trainval_percent=0.9
train_percent=0.85
total_xml = os.listdir(xmlfilepath)
num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

print("train and val size",tv)
print("train size",tr)
# print(total_xml[1])
start = time.time()

# print(trainval)
# print(train)

test_num=0
val_num=0
train_num=0
# for directory in ['train','test',"val"]:
#         xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
#         if(not os.path.exists(xml_path)):
#             os.mkdir(xml_path)
#         # shutil.copyfile(filePath, newfile)
#         print(xml_path)
for i  in list:
    name=total_xml[i]
            # print(i)
    if i in trainval:  #train and val set
    # ftrainval.write(name)
        if i in train:
            # ftrain.write(name)
            # print("train")
            # print(name)
            # print("train: "+name+" "+str(train_num))
            directory="train"
            train_num+=1
            if(train_num%1000==0):
                print("train: "+name+" "+str(train_num))
            xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
            if(not os.path.exists(xml_path)):
                os.mkdir(xml_path)
            filePath=os.path.join(xmlfilepath,name)
            newfile=os.path.join(saveBasePath,os.path.join(directory,name))
            shutil.copyfile(filePath, newfile)

        else:
            # fval.write(name)
            # print("val")
            # print("val: "+name+" "+str(val_num))
            directory="validation"
            if(val_num%1000==0):
                print("val: "+name+" "+str(val_num))
            xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
            if(not os.path.exists(xml_path)):
                os.mkdir(xml_path)
            val_num+=1
            filePath=os.path.join(xmlfilepath,name)
            newfile=os.path.join(saveBasePath,os.path.join(directory,name))
            shutil.copyfile(filePath, newfile)
            # print(name)
    else:  #test set
        # ftest.write(name)
        # print("test")
        # print("test: "+name+" "+str(test_num))
        directory="test"
        if(test_num%1000==0):
            print("test: "+name+" "+str(test_num))
        xml_path = os.path.join(os.getcwd(), 'annotations/{}'.format(directory))
        if(not os.path.exists(xml_path)):
            os.mkdir(xml_path)
        test_num+=1
        filePath=os.path.join(xmlfilepath,name)
        newfile=os.path.join(saveBasePath,os.path.join(directory,name))
        shutil.copyfile(filePath, newfile)
            # print(name)

# End time
end = time.time()
seconds=end-start
print("train total : "+str(train_num))
print("validation total : "+str(val_num))
print("test total : "+str(test_num))
total_num=train_num+val_num+test_num
print("total number : "+str(total_num))
print( "Time taken : {0} seconds".format(seconds))
