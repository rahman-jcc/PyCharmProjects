'''
- Asked user to input something
- User input will be saved to a file.
- User input saved in a file shall be copied to another file
- Will compare the file contents.
'''

import sys
import os
import shutil
import filecmp


def copyContentsofFile(stringprints):
    file_one = open("writeTest_1", "w+")
    file_one.write(str(stringprints))
    file_one = open("writeTest_1", "w+")
    str1 = file_one.read()

    file_three = open("writeTest_3", "w+")
    file_three.write("Python....")
    file_three = open("writeTest_3", "w+")
    str3 = file_three.read()

    # Copying the contents of one file to another
    file_two = open("writeTest_2", "w+")
    shutil.copyfile("writeTest_1", "writeTest_2")
    file_two_contents = open("writeTest_2", "r+")
    str2 = file_two_contents.read()

    # file_two.write(str1)
    print("File 1 includes:  ", str1)
    print("File 2 includes:  ", str2)
    print("File 3 includes:  ", str3)
    file_one.close()
    file_two.close()
    file_three.close()


# Getting user input and passig to the function
stringprints = input(" ")
# userInput= stringprints.split()
# copyContentsofFile(userInput)
copyContentsofFile(stringprints)
IsFilesSame = filecmp.cmp("writeTest_1", "writeTest_2")
if IsFilesSame:
    print("Both files are same")
else:
    print("Hey, stop these files are not same!!!")
