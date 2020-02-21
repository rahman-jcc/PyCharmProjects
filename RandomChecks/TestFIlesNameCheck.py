import os
print ("root prints out directories only from what you specified")
print ("dirs prints out sub-directories from root")
print ("files prints out all files from root and directories")
print ("*" * 20)
rootPath = 'C:\Program Files (x86)\PaloDEx Group\IAM'
for root, dirs, files in os.walk(rootPath):
    #print(root) 
    #print(dirs)
    print (os.path.join(dirs,files))