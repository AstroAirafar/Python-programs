class Student:
    """Academic record of students"""
    global percentage, grade, division
    percentage = 0
    grade = ''
    division = ''
    def __init__(self,name, rollNo, stream) -> None:
        self.name = name
        self.rollNo = rollNo
        

    def stuData(self):
        print(f"Name : {self.name}")
        print(f"Roll NO : {self.rollNo}")
        print(f"Stream : {self.stream}")

        
    def setMarks(self,mList):
        self.mList = mList

    def getStream(self):
        print(f"{self.name}'s Stream is {self.stream}")

    def percentageCalc(self):
        mySum = sum(self.mList)
        perct = (mySum * 100)/500
        percentage = perct
        print(f"{self.name} percentage is {percentage}%")

    def gradenGen(self):
        if(percentage >= 90):
            grade = 'A'
        elif(percentage < 90 and percentage >=80):
            grade = 'B'
        elif(percentage < 80 and percentage >=65):
            grade = 'C'
        elif(percentage < 65 and percentage >=40):
            grade = 'D'
        else:
            grade = 'E'

        print(f"{self.name}'s Grade is {grade}")

    def divsionGen(self):
        if(percentage >=60  ):
            division = 'I'
        elif(percentage < 60 and percentage >=50):
            division = 'II'
        elif(percentage < 50 and percentage >=35):
            division = 'II'
        else:
            division = 'Fail'


        print(f"{self.name}'s Division is {division}")




radhika = Student("Radhika", "121", "S")
myMarkList  = []
for i in range(1, 6):
    m1 = int(input(f"Enter mark {i} : "))
    myMarkList.append(m1)

radhika.stuData()
radhika.setMarks(myMarkList)
radhika.getStream()
radhika.percentageCalc()
