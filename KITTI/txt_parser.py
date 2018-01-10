

import os
'''
KITTI_LABELS = {
    'none': (0, 'Background'),
    'Car': (1, 'Vehicle'),
    'Van': (2, 'Vehicle'),
    'Truck': (3, 'Vehicle'),
    'Cyclist': (4, 'Vehicle'),
    'Pedestrian': (5, 'Person'),
    'Person_sitting': (6, 'Person'),
    'Tram': (7, 'Vehicle'),
    'Misc': (8, 'Misc'),
    'DontCare': (9, 'DontCare'),
}
'''

def filter_KITTI_Data(txt_file_path,output_file_base_path):
    file = open(txt_file_path)
    #results/****.txt
    # print(txt_file_path)
    txt_name=txt_file_path.split("/")[1]
    output_file_path=os.path.join(output_file_base_path,txt_name)
    print(output_file_path)
    output_object = open(output_file_path, 'w')

    file_lines=file.readlines()
    for line in file_lines:
        # print(line)
        line_array=line.split(" ")
        # print(line_array)
        if(line_array[0]=="Truck"):
            line=str(line).replace("Truck", "Car")
        elif(line_array[0]=="Van"):
            line=str(line).replace("Van", "Car")
            # print(line)
        elif(line_array[0]=="Car"):
            line_array[0]="Car"
        elif(line_array[0]=="Cyclist"):
            # line_array[0]="Cyclist"
            line=str(line).replace("Cyclist", "Car")
        elif(line_array[0]=="Person_sitting"):
            # line_array[0]="Person"
            line=str(line).replace("Person_sitting", "Person")
        elif(line_array[0]=="Pedestrian"):
            line_array[0]="Person"
            line=str(line).replace("Pedestrian", "Person")
        elif(line_array[0]=="Tram"):
            # line_array[0]="Car"
            line=str(line).replace("Tram", "Car")
        elif(line_array[0]=="none"):
            line_array[0]="none"
        else:
            continue
        output_object.write(line)
    output_object.close( )
if __name__ == '__main__':
    base_path=r"label_2"
    file_lists=os.listdir(base_path)
    output_path="results"
    num=0
    for single_file in file_lists:
        single_file_path=os.path.join(base_path,single_file)
        # print(single_file_path,output_path)
        filter_KITTI_Data(single_file_path,output_path)
        num=num+1
    print("total num of files %s" %(num))
    print("already finished")
    # print(file_lists)
    # filter_KITTI_Data()
