

xml_file=open("xml_statistical.txt","r")
pic_lines=open("picture_statistical.txt","r")

xml_lines=xml_file.readlines()
xml_dict={}
xml_total_num=len(xml_lines)
for j in range(0,xml_total_num-1):
    # print(xml_lines[j])
    folder=xml_lines[j].split(".")[0].split("/")[1]
    # print(folder)
    xml_dict[folder]=xml_lines[j].split(" ")[1]

# print(xml_dict)

pic_lines=pic_lines.readlines()
num=len(pic_lines)
num_of_gap=0
for i in range(0,num-1):
    folder=pic_lines[i].split(" ")[0].split("/")[1]
    xml_num=int(xml_dict[folder])
    picture_num=int(pic_lines[i].split(" ")[1])
    if(xml_num!=picture_num):
        print(pic_lines[i])
        print(xml_num)
        num_of_gap=num_of_gap+(picture_num-xml_num)
        print(picture_num)
print(num_of_gap)
# def migrate_xml():
