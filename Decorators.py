def kid(human):
    def inner(res):
        print("1.health is imporatant(if not god is the reason)")
        human(res)
        print("7.anwer it your self?")
    return inner
def man(human):
    def inner(res):
        print("2.wealth and your responsbilties are important(if not god had witten a bad fate for you)")
        human(res)
        print("6.but is this crt is god have this much simple logic less plans for us")
    return inner
def oldman(human):
    def inner(res):
        print("3.what we have done to this life is important(contribution(if there is nothing again we can blame god)")
        human(res)
        print("5.this is how normal people organize life")
    return inner
@kid
@man
@oldman
def normalHuman(life):
    print(life)

normalHuman("4.You are going to die one day")


def begin(human):
    def inner(hypothesis):
        print("1.disipline is important")
        human(hypothesis)
        print("7.Even a pragram is considered good if it is running perfect in worst conditions(O(n) we simple humans expect this then why don't god? here bad times are our test cases")
    return inner
def intermediate(human):
    def inner(hypothesis):
        print("2.The present state and how much effort we are giving to it is important(if it went wrong god has better plans for us)")
        human(hypothesis)
        print("6.The universe is getting bigger than you think we are something like bateria on earth when compared ")
    return inner

def end(human):
    def inner(hypothesis):
        print("3.Scientifically our body may die but the impact we have created(our actions) will lasts forever")
        human(hypothesis)
        print("5.Every action we do will randomly connected to each other(be more aware and be disipline on what ever things you do)")
    return inner

@begin
@intermediate
@end
def MyLife(myHypothesis):
    print(myHypothesis)
    
MyLife("4. I Belive in god and I give my best on what I'm working(without expecting the results)")