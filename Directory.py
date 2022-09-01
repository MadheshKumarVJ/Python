import os

current = os.getcwd()
print(current)

os.chdir("\home\maddy\Python\Python\SubPython")
changed_dir = os.getcwd()
print(changed_dir)

with  open("sub1.txt","w") as f:
    f.write("I am a new file in the sub folder of python")