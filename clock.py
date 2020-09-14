#current date and time in European format
from datetime import datetime
class clock():
    #formats for date and time 
    date_format="%d.%m.%Y"
    time_format="%H:%M:%S"
    dateTime_format="%H:%M:%S %d.%m.%Y"
    def __init__(self):
        self.update()
    def update(self): #time update
         self.now=t=datetime.now()
    def time(self): #returns time
        self.update()
        return self.now.strftime(self.time_format)
    def date(self): ¸#returns date
        self.update()
        return self.now.strftime(self.date_format)
    def dateTime(self): #returns date and time
        self.update()
        return self.now.strftime(self.dateTime_format)
