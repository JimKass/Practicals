"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os
import string


# TODO: Fix this


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())
    os.chdir('Lyrics/Lyrics')

    for dir_name, dir_list, file_list in os.walk("."):
        for filename in file_list:
            file_path = dir_name + "\\" + filename
            new_name = get_fixed_filename(file_path)
            os.rename(file_path, new_name)


def get_fixed_filename(filename):
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for i, letter in enumerate(filename):
        if filename[i -1] == "_":
            letter = letter.upper()
        if letter.isupper() and filename[i - 1] != "_" and i != 0 and filename[i -1] not in string.punctuation:
            letter = "_{}".format(letter)
        new_name += letter
    return new_name


main()
