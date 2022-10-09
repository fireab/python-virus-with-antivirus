import glob, re
#virus scan program
#scan for signature just like semantec or other anti virus software

def CheckForSegnatures():
    print('##checking for virus segnatures.......')
    #get all program in the directory
    programs=glob.glob("../*.py")
    for p in programs:
        thisFileInfected=False
        file=open(p,"r")
        lines=file.readlines()
        file.close()

        for line in lines:
            if(re.search("^#starting of  virus code",line)):
               #found a virus
                print("!!!!!!virus is found in the file  " + p)            
                thisFileInfected=True
        if(thisFileInfected==False and p!="antivirus.py"):
            print( p + " appears to be clean " )
    print('##########################')  

CheckForSegnatures()    
 
