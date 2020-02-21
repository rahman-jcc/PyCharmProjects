# Installed IAM binaries informaiton with version info

import fnmatch
import os,sys
import win32api
import win32com.client

#from win32api import GetFileVersionInfo,

# Function to get file version information 
def get_version_number (filename_path):
    from win32api import GetFileVersionInfo, LOWORD, HIWORD
    try:
        info = GetFileVersionInfo (filename_path, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms),LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return None 

# logging binaries name and version information 
rootPath = 'C:\Program Files (x86)\PaloDEx Group\IAM'
pattern = ('*.*')
#file_version = win32api.GetFileVersionInfo(filename,rootPath)
sys.stdout = open ("C:\ProgramData\PaloDEx Group\Binary_file.txt", "w")

for root, dirs, files in os.walk(rootPath):
    for filename_path in fnmatch.filter(files, pattern):
        #print( os.path.join(root, filename))
        #s=win32com.client.gencache.EnsureDispatch('capicom.signedcode',0)
        #s.filename = filename_path
        #signer = s.signature()        

        file_version = get_version_number (filename_path)

        # getting file information using command like tool    
            
        #file_signature_command = os.system ("sigcheck.exe -a -u -e "%~1"1>nul 2>nul") 
        #file_signature_command_typed = str(file_signature_command)
        #parsed_file_signature = ",".join([str(i) for i in file_signature_command_typed]) #------
        # end of getting file information using command like tool

        parsed_fileversion = ".".join([str(i) for i in file_version])
        #file_size = os.path.getsize (rootPath)
        print(filename_path, "->", parsed_fileversion)
        #print ('filename', file= f)
sys.stdout.close()