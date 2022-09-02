class Plans:
    """@author:Madhesh Kumar V J
    NAME: 
        Plans
    DESCRIPTION:
        Shedules your plans for the week days
        this module simply uses (init,getPlan(Generator))
        overrides this methods
    METHODS:
        Object.getPlan()
        Object.PrintPlans()
    """
    def __init__(self):
        self.max=4
        self.week =["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.plans=[]
    #using generator (get rid of iter and next)
    def getPlans(self):
        self.count = 0
        while (self.count<=self.max):
            plan = input("What is your plan for {} : ".format(self.week[self.count]))
            self.plans.append(plan)
            self.count+=1
            yield plan
    # def __iter__(self):
    #     self.count =0
    #     return self
    # def __next__(self):
    #     if (self.count<=self.max):
    #         plan = input("What is your plan for {} : ".format(self.week[self.count]))
    #         self.plans.append(plan)
    #         self.count+=1
    #         return plan
    #     else:
    #         raise StopIteration
    def printPlan(self):
        for i in range(self.max+1):
            print("your plan for {} is to {}".format(self.week[i],self.plans[i]))
    def doc(self):
        print(Plans.__doc__)
Madhesh_plans = Plans()
Madhesh_plans.doc()
#planIterator = iter(Madhesh_plans)
for plan in Madhesh_plans.getPlans():
    print(plan)
Madhesh_plans.printPlan()