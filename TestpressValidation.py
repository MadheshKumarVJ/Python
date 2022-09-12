import re
import sys
def selector(pattern,search,replace):
    def validator(word):
        return re.search(pattern,word)
    def publisher(word):
        return re.sub(search,replace,word)
    return[validator,publisher]

class TestPressSelection:
    rule_book='Selection.txt'

    def __init__(self):
        self.check=open(self.rule_book,encoding='utf-8')
        self.cache = []
    def __iter__(self):
        self.cache_index=0
        return self
    def __next__(self):
        self.cache_index+=1
        if len(self.cache)>=self.cache_index:
            return self.cache[self.cache_index-1]
        
        if self.check.closed:
            raise StopIteration
        
        line = self.check.readline()
        if not line:
            self.check.close()
            raise StopIteration
        pattern, search, replace=line.split(None,3)
        rules = selector(pattern,search,replace)
        self.cache.append(rules)
        return rules
rules = TestPressSelection()

def interview(mark):
    for validator, publisher in rules:
        if validator(mark):
            return publisher(mark)


flag = True
print("press ! to Quit!")
while(flag):
    name = input("Enter the name of the candidate:")
    if (name=='!') :
        sys.exit()
    score = input("Enter the score of the candidate:").strip()
    if (score=='!') :
        sys.exit()
    
    result = interview(score)

    if (name=='!') or (score=='!'):
        sys.exit()
    
    with open("interview_results.txt","a") as r:
        r.write(name+" "+result+"\n")
    