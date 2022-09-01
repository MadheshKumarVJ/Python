class Plans:
    """@author:Madhesh Kumar V J
    NAME: 
        Plans
    DESCRIPTION:
        Shedules your plans for the week days
        this module simply uses (init,iter,next)
        overrides this methods
    METHODS:
        next(Object)
        iter(Object)
        PrintPlans(Object)
    """
    def __init__(self):
        self.max=4
        self.week =["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.plans=[]
    def __iter__(self):
        self.count =0
        return self
    def __next__(self):
        if (self.count<=self.max):
            plan = input("What is your plan for {} : ".format(self.week[self.count]))
            self.plans.append(plan)
            self.count+=1
            return plan
        else:
            raise StopIteration
    def printPlan(self):
        for i in range(self.max+1):
            print("your plan for {} is to {}".format(self.week[i],self.plans[i]))
    def doc(self):
        print(Plans.__doc__)
Madhesh_plans = Plans()
Madhesh_plans.doc()
planIterator = iter(Madhesh_plans)
for i in range(5):
    print(next(Madhesh_plans))
Madhesh_plans.printPlan()