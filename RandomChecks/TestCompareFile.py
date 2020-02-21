import sys


with open('C:\ProgramData\PaloDEx Group\Binary_file.txt', 'r') as file1:
    with open('C:\Program Files (x86)\PaloDEx Group\Manifest.csv', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('C:\ProgramData\PaloDEx Group\ComPareFile.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)