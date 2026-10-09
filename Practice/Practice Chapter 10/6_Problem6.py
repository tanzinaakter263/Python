#Can you change  the self parameter inside a class to something else(say "tanzina").Try changing to "slf" or "tanzina" and see the effects.

from random import randint



class train:
  def __init__(slf,trainNo):
    slf.trainNo=trainNo
  def book(self,fro,to):
    print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

  def getStatus(self):
    print(f" train no: {self.trainNo} is running on time")
    

  def getFare(self,fro,to):
    print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t=train(12399)
t.book("Dhaka","Cumilla")
t.getStatus()
t.getFare("Dhaka","Cumilla")