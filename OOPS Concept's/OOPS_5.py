# Static Method

class Math:

    # Static method do not change anything. Do not require an instance to be called. Do not require paramters as well.
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")
    
print(Math.add5(5))
Math.pr()