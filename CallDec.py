def first(runner):
    def inner(sprint):
        print("1.valkaila first yaru first la varananu mukkiyam illa")
        runner(sprint)
        print("1.2nd price")
    return inner
def second(runner):
    def inner(sprint):
        print("2.Last la yaru first vara kirathu tha mukkiyam")
        runner(sprint)
        print("2.1st price")
    return inner

@first
@second
def run(winningStatement):
    print(winningStatement)

run("You won the race")