#rename file to contain only letters and no numbers from 0-9.
#replace "alphabet" with the folder name and make sure it is in the same directory as of this script.
import os
def rename_files():
    file_list = os.listdir("alphabet")
    saved_path = os.getcwd()
    os.chdir("alphabet")
    for file in file_list:
        print "Old Name - "+file
        print "New Name - "+file.translate(None, "0123456789")
        print ""
        os.rename(file,file.translate(None, "0123456789"))    
    os.chdir(saved_path)
rename_files()    
