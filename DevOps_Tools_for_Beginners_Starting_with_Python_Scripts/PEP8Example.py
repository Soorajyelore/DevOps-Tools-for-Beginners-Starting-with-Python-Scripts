import datetime

MAX_BUDGET=1000.00

class Expance:
 def __init__(self,name,amount):
    self.name=name
    self.amount=amount
    self.date=datetime.datetime.now()