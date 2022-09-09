from ast import pattern
import re 
"""Write a Python program to check that a string contains 
only a certain set of characters (in this case a-z, A-Z and 0-9)"""

def check(sentance):
    pattern=re.compile(r"[a-zA-Z0-9]")
    ans = pattern.findall(sentance)
    return bool(ans)

print(check("this is maddy"))
print(check("!@#$%^&*("))