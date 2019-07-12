#!/usr/bin/env python
# coding: utf-8

# In[2]:


def createfilename(filename):
    f=open(filename,'w')
    for i in range(10):
        f.write('this is %d line\n'%i)
    print('file is written and data has been written')
    return
createfilename("file1.txt")
    


# In[3]:


ls


# In[4]:


cat file1.txt


# ### File Handling in Python
# * File:-Document containing information resides on the permanent storage
# * Different types of files:-txt,doc,pdf,csv and etc
# * Input; Keyboard
# * Output -- File
# ### Modes of the File I/O
# * "w"-- This mode is used to file writing
# 
#     -- If the file is not present it creates and writes        some data to it
#     
#     -- If the file is already present then it will            rewrite the previous content

# In[ ]:


def createfilename(filename):
    f=open(filename,'w')
    f.write("Testing....\n")
    print('file is written and data has been written')
    return
createfilename("file1.txt")


# In[ ]:


cat file1.txt


# In[ ]:


def appenddata(filename):
    f=open(filename,'a')
    for i in range(10):
        f.write('this is %d line\n'%i)
    print('file is written and data has been written')
    return
appenddata("file2.txt")
    


# In[ ]:


def appenddata(filename):
    f=open(filename,'a')
    f.write("New line 1\n")
    f.write("New line 2\n")
    f.close()
    print('file is written and data has been written')
    return
appenddata("file2.txt")
    


# In[ ]:


# FUnction to read the file data
def readdata(filename):
    f= open(filename,"r")
    if f.mode == 'r':
        x=f.read()
        print(x)
    f.close()
    return 
readdata('file3.txt')


# In[ ]:


# FUnction to read the file data
def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode=='r':
            data=f.read()
            prinr(data)
        elif f.mode=='a':
            f.write('Data to the file')
            print('The data succesfully written')
    f.close()
    return
filename=input("Enter the file name")
mode=input("Enter the mode of the file")
fileoperations(filename,mode)


# In[ ]:


# Data Analysis
#  Word Count Program
def wordcount(filename,word):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=x.split()
    cnt=li.count(word)
    return cnt
filename=input('Enter the filename: ')
word=input('enter the word: ')
wordcount(filename,word)


# In[ ]:


#character count from the given file
def charcount(filename):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
    return len(li)
filename = input('enter the filename: ')
charcount(filename)


# In[ ]:


# Function to find the no. of lines in the input file
def linecount(filename):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=x.split("\n")
    return len(li)
filename = input('enter the filename: ')
linecount(filename)


# In[ ]:


# Function to print the Upper and lower characters
def casecount(filename):
    cntupper=0
    cntlower=0
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
    for i in li:
        if i.isupper():
            cntupper+=1
        elif i.islower():
            cntlower+=1
    output='upper case = {0}, lower case = {1}'.format(cntupper,cntlower)
    return output
filename=input("Enter filename: ")
casecount(filename)
    


# In[ ]:


import os


# In[20]:


ls


# In[14]:


cd desktop


# In[ ]:


cd python


# In[ ]:


cd ..


# In[ ]:


import os
os.listdir('python/')


# In[27]:


from pathlib import path
li=path('python/')
for i in li.iyerdir():
    print(i.name)


# In[15]:


import os
dirPath = "python/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)


# In[16]:


pwd


# In[18]:


import os
dirPath = "python/"
with os.scandir(dirPath) as f:
    for i in f:
        if i.is_file():
            print(i.name)


# ### Listing of Subdirectories

# In[22]:


dirPath = "python/"
for i in os.listdir(dirPath):
    if os.path.isdir(os.path.join(dirPath,i)):
        print(i)


# In[23]:


from pathlib import Path
dirPath=Path('python/')
for i in dirPath.iterdir():
    if i.is_dir():
        print(i.name)


# ### Creating a single Directory

# In[24]:


import os
os.mkdir('single directory')


# In[25]:


import pathlib
p=pathlib.Path('TestFolder')
p.mkdir()


# In[26]:


ls


# ### Creating Multiple Directories

# In[29]:


import os 
os.makedirs('2019/July/11')


# In[30]:


ls


# ### FileName Pattern 

# In[33]:


cd desktop


# In[34]:


import os
dirpath='python/'
for f_name in os.listdir(dirpath):
    if f_name.endswith('.ipynb'):
        print(f_name)


# In[40]:


import os
dirpath='python/'
for f_name in os.listdir(dirpath):
    if f_name.startswith('0'):
        print(f_name)


# ### Deleting files and directories

# In[42]:


cd python


# In[43]:


import os
data_file='file1.txt'
os.remove(data_file)


# In[44]:


ls


# In[45]:


cd ..


# In[48]:


data_dir='single directory'
os.rmdir(data_dir)


# In[47]:


import shutil
data_dir='2019'
shutil.rmtree(data_dir)


# In[ ]:




