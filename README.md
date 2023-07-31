# pymax
A py script collection for 3dsmax

# debug from vs code
### you should know in 3dsmax the pip tool is not installed,so before you do any thing, you should install the pip tool first.  
the run means you should start CMD from there then input your command.

## 1. install pip
1. got to: https://github.com/pypa/get-pip find the right version of get-pip.py.  
   put it in <3ds Max Install>\scripts\Python\.
2. go to: <3ds Max Install> then run:
    >.\3dsmaxpy.exe scripts\\Python\\get-pip.py
## 2. install the ptvsd. goto "<3ds Max Install>\python\Scripts" start CMD then  run:
1. >.\pip2 install --no-cache-dir --no-binary ptvsd ptvsd
## 3. test if the module installed right. 
1. start 3dsmax
2. open the listinger
3. type:  
   > import ptvsd  
   > ptvsd.enable_attach()
4. if you see something like below, that means you work is correct.
   > ('0.0.0.0', 5678)
# try debug from max2020 fail becauseof it has no python interpreter
