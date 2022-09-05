def kadavul_kaila(ask:str):
    def outer (mrg):
        def inner(decision):
            if(input(ask).lower()!='y'):
                print("You have been saved in the climax (peace)")
                return
            print("welcome to the unwanted complicated valkai")
            return mrg(decision)
        return inner
    return outer

@kadavul_kaila("are you sure of getting married? if yes  press y else please press any key other than y ")
def marrriage(decision):
    print(decision)
marrriage("I am ready to get married")