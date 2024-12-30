file1=input("enter the source file to be copied:")
file2=input("enter the destination file:")
try :
    with open(file1,"r") as fr:
        with open(file2,"w")as fw:
            for line in fr:
                fw.write(line)
    print("file copied successfully")
except FileNotFoundError:
    print("Source file not found .please check the file name or path")
except Exception as e:
    print(f"An error occurred:{e}")