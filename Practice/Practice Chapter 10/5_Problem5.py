# Wrute a class train which has method to book  a ticket ,get status (no of seats) and get fare information of train running under Indian Railways.


from random import randint



class train:
  def __init__(self,trainNo):
    self.trainNo=trainNo
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