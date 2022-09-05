def Check(ask:str):
    def outer (deletion):
        def inner(decision):
            if(input(ask).lower()!='y'):
                print("File is not deleted")
                return
            print("Deletion confirmed")
            return deletion(decision)
        return inner
    return outer

@Check("are you sure ? if yes  press y else please press any key other than y ")
def Deletion(decision):
    print(decision)
Deletion("File deleted")