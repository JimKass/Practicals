
import os
import shutil

def main():
    os.chdir("./FilesToSort")
    for file in os.listdir("."):
        file_extenstion = file.split(".")[1]
        if file_extenstion not in os.listdir("."):
            os.mkdir(file_extenstion)
        shutil.move(file, file_extenstion)


main()