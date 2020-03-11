#PROGRAM FOR GENERATING RANDOM NAMES AND MAILS
import csv
import os
import random
firstname=[]
lastname=[]
#Reading the text file
with open("names.txt","r") as file:
    reader =file.read()
    #Spliting first name and Last name
    names= reader.split()
    i = 0
    while i<len(names):
        firstname.append(names[i])
        lastname.append(names[i+1])
        i+=2
    #writning names to a csv file
with open("names.csv","w") as file:
    writer=csv.writer(file)
    header = "First Name","Last Name","Mail ID","Phone Number"
    writer.writerow(header)
    for j in range(len(firstname)) :
        line=firstname[j],lastname[j],firstname[j]+lastname[j]+str(random.randint(1,99))+"@dummymail.com",str(random.randint(100,999))+"555"+str(random.randint(1111,9999))
        writer.writerow(line)
