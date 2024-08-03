import random
class Train:
    def __init__(self,train_no):
        self.train_no = train_no
        self.total_no_of_seats = 500
    def booking(self):
        if(self.total_no_of_seats > 0):
            self.ticket_No = random.randint(1001,9999)
            print(f"Booking is successfull with ticket no : {self.ticket_No} and train no : {self.train_no}")
            self.total_no_of_seats -= 1
        else:
            print("seats are not availabal in this date")
    def status(self):
        print("Train running on time..")
        print(f"Tatal availabal seats are : {self.total_no_of_seats}")

    def getInfo(self):
        print("Happy journey")

obj = Train(12455)
obj.booking()
obj.status()
obj.getInfo()