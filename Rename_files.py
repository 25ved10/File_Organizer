import os
 
def main():
   
    folder = 'D:\Downloads\img'
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"img {str(count)}.jpg"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()