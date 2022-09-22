import re 

doc = """this isa nothing \n but a simple text"""

pattern = r"\bis"

x = re.sub(pattern,"was",doc)
print(x)