import os
import shutil

def arrange_files_as_per_extension_name(location):
    files_list=os.listdir(location)
    folders_list=[]
    flag=0
    for i in files_list:
        if os.path.isfile(location+'\\'+i) and i.split('.')[1] not in folders_list:
            try:
                os.mkdir(location+'\\'+i.split('.')[1])
            except:
                print('Folder ['+i.split('.')[1]+'] already exists')
            shutil.move(location+'\\'+i, location+'\\'+i.split('.')[1]+'\\'+i)
            folders_list.append(i.split('.')[1])
            flag=1
        elif os.path.isfile(location+'\\'+i) and i.split('.')[1] in folders_list:
            shutil.move(location+'\\'+i, location+'\\'+i.split('.')[1]+'\\'+i)
            flag=1
    if flag==0:
        print('No files here ['+location+']')

def arrange_files_as_per_common_text_in_each_file_name(location):
    uniqueness_list=set()
    choice=int(input("""MENU
          PRESS [1] - IF YOU WANT TO GIVE THE COMMON TEXTS MANUALLY ONE BY ONE
          PRESS [2] - IF YOU WANT TO GIVE A STARTING AND ENDING INDEX TO FETCH THE COMMON TEXTS FROM THE FILE NAMES AUTOMATICALLY
ENTER - """))
    match choice:
        case 1:
            print("Enter ['quit'] to quit")
            count=0
            while True:
                count+=1
                name=input("Enter the {}th common text in some file name(s) / ['quit'] - ".format(count))
                if name.upper().strip() == 'QUIT':
                    break
                uniqueness_list.add(name.upper())
        case 2:
            print('Indexes are starting from [1]')
            start=int(input('Enter the starting index - '))-1
            end=int(input('Enter the ending index - '))
            for i in os.listdir(location):
                if os.path.isfile(location+'\\'+i):
                    uniqueness_list.add(i[start:end].upper())
        case _:
            print('Not a correct input')
    folders_list=list(uniqueness_list)
    for i in folders_list:
        try:
            os.mkdir(location+'\\'+i)
        except:
            print('Folder ['+i+'] already exists')
    files_list=os.listdir(location)
    flag=0
    for i in files_list:
        if os.path.isfile(location+'\\'+i):
            for j in folders_list:
                if j in i.upper():
                    shutil.move(location+'\\'+i, location+'\\'+j+'\\'+i)
                    break
            flag=1
    if flag==0:
        print('No files here ['+location+']')

def rename_file_names_to_numbers(location):
    files_list=os.listdir(location)
    flag=0
    count=int(input('Enter starting number - '))
    for i in files_list:
        if os.path.isfile(location+'\\'+i):
            os.rename(location+'\\'+i, location+'\\'+str(count)+'.'+i.split('.')[1])
            count+=1
            flag=1
    if flag==0:
        print('No files here ['+location+']')

# location1=r'C:\Users\ASUS\Desktop\ANU'

# arrange_files_as_per_extension_name(location1)

# location2=r'C:\Users\ASUS\Desktop\PURI\mp4'

# arrange_files_as_per_common_text_in_each_file_name(location2)

location3=r'C:\Users\ASUS\Pictures\A\Arranged Final\Travelling Videos\SIKKIM\VIDEOS\EDITED\TIMELAPSES'

rename_file_names_to_numbers(location3)