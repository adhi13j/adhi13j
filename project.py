class atm:
    def __init__(self):
        self.money = 200
        self.inbank = 150
    def status(self):
        status = "inbank =="+str(self.inbank)
        return status 
    def withdraw(self,sum):
        self.money = self.money + sum
        self.inbank -= sum 
        print("withdrawn::"+str(sum)+"balance"+str(self.inbank))
        print(self.status())
    def deposit(self,sum):
        self.inbank += sum
        self.money -= sum
        print("deposited" + str(sum))
p1 = atm()
p1.deposit(10)
p1.withdraw(20)