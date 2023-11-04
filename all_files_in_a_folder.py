import os
# import pandas as pd

start_directory = r"C:\Users\ASUS\Desktop\EDUCATION\BIG DATA"
l=[]

for root, dirs, files in os.walk(start_directory):
  for file_name in files:
    full_path = os.path.join(root, file_name)
    l.append(full_path[len(start_directory):])
    print(full_path[len(start_directory):])

# df=pd.DataFrame(l, columns=['file_name'])
# df.to_csv('A:/file.csv', index=False, header=True)
# print(df)