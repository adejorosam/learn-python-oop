
'''Write a class called Time whose only field is a time in seconds. It should have a method called
convert_to_minutes that returns a string of minutes and seconds formatted as in the following example:
if seconds is 230, the method should return '5:50'. It should also have
a method called convert_to_hours that returns a string of hours, minutes, and seconds
formatted analogously to the previous method.'''

class Time:
    def __init__(self,seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        return str(self.seconds//60)

    def convert_to_hours(self):
        return f'{self.seconds//3600}:{self.seconds//60}:{self.seconds}'

a = Time(500)
print(a.convert_to_minutes())
print(a.convert_to_hours())

