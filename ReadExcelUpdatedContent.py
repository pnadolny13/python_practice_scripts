# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import pydicom
import os
os.chdir("C:\TESTPy")
f=open(file,'r')
lines=f.readlines()
f.close()
f=open(file,'w')
   for line in lines:
       file.write("2?")
#############OPENS Text FILE, Reads, then updates to next sequence############################

import os
os.chdir("C:\TESTPy")
fileO = open("Pat2.txt","r")
print ('The orginal line is: ')
for line in fileO:
    print (line)
newnum = line[7:]
fileO.close()
newnum = int(newnum)+1   
      
print ('The new sequenced file says: ')
fileN = open("Pat2.txt","w")
fileN.write('Updated'+str(newnum))
fileN.close()

fileO = open("Pat2.txt","r")
for line in fileO:
    print (line)
fileO.close()


#########################################
directory = "C:\TESTPy"
import os
os.chdir(directory)
list = os.listdir(directory)
for file in list:
    content = open(file,"r")
    print ('The orginal content of '+file + ' is: ') 
    for line in content:
        print (line)
    content.close()
    content = open (file, "w")
    content.write(line+"1")
    content.close()
    print (file + ' now says says:')
    content = open (file, "r")
    for line in content:
        print (line)
    content.close()
    
    
    
    
    
    
   
    
    
    
    
    
    
    