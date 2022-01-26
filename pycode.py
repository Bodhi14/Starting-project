class cred:
       def __init__(self,name,age,occu):
               self.name = name
               self.age = age
               self.occu = occu
       def out(self):
               print("Your name is : " + self.name)
               print("Your age is : " + str(self.age))
               print("Your occupation is : " + self.occu)
n=int(input("Enter no. of entries "))
for i in range(0,n):
 naam=input("Your name is : " )
 umar=int(input("Your age is : "))
 kaam=input("Your profession is : ")
 individual = cred(naam, umar, kaam)
 individual.out()
