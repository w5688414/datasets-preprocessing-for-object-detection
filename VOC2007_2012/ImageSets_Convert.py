
import os
import random
import time

xmlfilepath=r'./VOC2007/Annotations'
saveBasePath=r"./"

trainval_percent=0.8
train_percent=0.85
total_xml = os.listdir(xmlfilepath)
num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

print("train and val size",tv)
print("traub suze",tr)
ftrainval = open(os.path.join(saveBasePath,'VOC2007/ImageSets/Main/trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath,'VOC2007/ImageSets/Main/test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath,'VOC2007/ImageSets/Main/train.txt'), 'w')
fval = open(os.path.join(saveBasePath,'VOC2007/ImageSets/Main/val.txt'), 'w')
# Start time
start = time.time()
for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
# End time
end = time.time()
seconds=end-start
print( "Time taken : {0} seconds".format(seconds))

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
