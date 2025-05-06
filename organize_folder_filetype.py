import os 
import shutil 

path = 'D:\Downloads'

list_ = os.listdir(path)  
for file_ in list_: 
    name, ext = os.path.splitext(file_) 
  
    # This is going to store the extension type 
    ext = ext[1:] 

    if ext == '': 
        continue

    if os.path.exists(path+'/'+ext): 
       shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 

    else: 
        os.makedirs(path+'/'+ext) 
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 