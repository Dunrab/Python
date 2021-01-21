''' CFRS 510
	Script to find files that have the jpg magic number even if they do not have the .jpg file extension

	Author name: James
	Assignment #: HW3

	Description:  This program will request the user to provide an input directory and will return all files that have a jpg magic number in
	              an output file named Output.txt. The output file will provide the directory and file name of the file, as well as
	              the MAC times and the SHA256 hash of the file.
	Usage: python.exe cmd.exe magicNumberChecker.py

    '''

import os, hashlib, os.path, glob, time

# Global variables
sha256hashList = []
timeCreatedList = []
timeModifiedList = []
timeLastAcessedList = []
jpgMagicNumber = 'ffd8' #magic number for jpg/jpeg files

def sha256HashFunc(filename):
    '''This takes in the directory where the file is located
        and hashes it into SHA256 and then addes it to a
        global variable list called sha256hashList'''

    with open(filename, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        sha256hashList.append(str(readable_hash))
    return readable_hash

def creationTime(filename):
    '''Takes the given file and returns its creation time'''
    creationtime = str(time.ctime(os.path.getctime(filename)))
    return creationtime

def modifiedTime(filename):
    '''Takes the given file and returns the last time it was modified'''
    modifiedtime = str(time.ctime(os.path.getmtime(filename)))
    return modifiedtime

def acessTime(filename):
    '''Takes the given file and returns the last time it was accessed'''
    acesstime = str(time.ctime(os.path.getatime(filename)))
    return acesstime

# Main function
def main():
    '''This is your main function. In Python, this will always be executed first and must located
	below any additional functions you may use in your program. Logistically, main should be the
	only function to call another function. '''

    start_time = time.time() #used to calculate the time that the script takes to exectute
    path = input("Enter the directory you would like to investigate (it will automatically look at its sub-folders): ")

    text_files = glob.glob(path + "/*/*", recursive=True) #do not do: text_files = glob.glob(path + "/**/*[!.pdf][!.txt]", recursive=True) WITH THE DOUBLE **
    i = 0

    writepath = path + r"\\Output.txt"
    f = open(writepath, "w")
    c = 0

    while i < 8: #keep as 8
        with open(text_files[i], 'rb') as fd7:
            file_head = fd7.read(2).hex()
            if (file_head == "ffd8" or file_head == jpgMagicNumber):
                f.write("Directory" + text_files[i])
                f.write("\n")
                f.write("Sha 256 Hash: " + sha256HashFunc(text_files[i]))
                f.write("\n")
                f.write("Creation Time:" + creationTime(text_files[i]))
                f.write("\n")
                f.write("Modified Time: " + modifiedTime(text_files[i]))
                f.write("\n")
                f.write("Last Access? Time" + acessTime(text_files[i]))
                f.write("\n")
                f.write("\n")
        i = i + 1
    f = open(writepath, "a")
    text_files2 = glob.glob(path + r"\*", recursive=True)
    i = 0
    #have to have to writes due to the way the the professor created the folders
    #I do not have proper permissions to read one of the folders and this is a work around
    while i < 4:
        with open(text_files2[i], 'rb') as fd7:
            file_head = fd7.read(2).hex()
            if (file_head == "ffd8" or file_head == jpgMagicNumber):
                f.write("Directory" + text_files2[i])
                f.write("\n")
                f.write("Sha 256 Hash: " + sha256HashFunc(text_files2[i]))
                f.write("\n")
                f.write("Creation Time:" + creationTime(text_files2[i]))
                f.write("\n")
                f.write("Modified Time: " + modifiedTime(text_files2[i]))
                f.write("\n")
                f.write("Last Access Time" + acessTime(text_files2[i]))
                f.write("\n")
                f.write("\n")
        i = i + 1

    #printing to the terminal/cmd prompt stating where the output file is located and giving a timestamp of how long it took
    print("\n")
    print("Files with the magic number for JPG/JPEG where found in the directory or sub-folders.")
    print("\n")
    print("The output file is named Output.txt and is stored in: ")
    print(path)
    print("\n")
    print("This script took %s seconds to run." % (time.time() - start_time))

if __name__ == '__main__':
#runs the script
    main()