import os
import shutil

location=r'C:\Users\ASUS\Desktop\New folder'
files_list=os.listdir(location)
folders_list=[]

for i in files_list:
    if os.path.isfile(location+'\\'+i) and i.split('.')[1] not in folders_list:
        try:
            os.mkdir(location+'\\'+i.split('.')[1])
        except:
            print('Folder already exists - '+i.split('.')[1])
        shutil.move(location+'\\'+i, location+'\\'+i.split('.')[1]+'\\'+i)
        folders_list.append(i.split('.')[1])
    elif os.path.isfile(location+'\\'+i) and i.split('.')[1] in folders_list:
        shutil.move(location+'\\'+i, location+'\\'+i.split('.')[1]+'\\'+i)