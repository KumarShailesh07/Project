class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum/len(self.marks)
        print(f'Hii {self.name} , your avg marks is: {avg}')

s1 = Students('Shailesh',[99,98,97,96])
s2 = Students('Ravi',[65,9,8,65,48,98])
s1.get_avg()
s2.get_avg()