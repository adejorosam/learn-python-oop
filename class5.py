'''Write a class called Converter. The user will pass a length and a unit when declaring an
object from the class—for example, c = Converter(9,'inches'). The possible units are
inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. For each of these
units there should be a method that returns the length converted into those units.
For example, using the Converter object created above, the user could call c.feet() and should get
0.75 as the result.'''

class Converter:
    def __init__(self,length,unit):
        self.length = length
        self.unit = unit

    def inches(self):   
        conv_list = {'conv_feet':self.length*12,'conv_yards':self.length*36,'conv_miles':self.length*63360,
                     'conv_kmeters':self.length*39370.079,'conv_meters':self.length*39.37,'conv_centimeters':self.length/2.54,
                     'conv_millimeters':self.length*25.4}
        
        if self.unit == 'feet':
            return conv_list['conv_feet']
        elif self.unit == 'yards':
            return conv_list['conv_yards']
        elif self.unit == 'miles':
            return conv_list['conv_miles']
        elif self.unit == 'kilometers':
            return conv_list['conv_kmeters']
        elif self.unit == 'meters':
            return conv_list['conv_meters']
        elif self.unit == 'centimeters':
            return conv_list['conv_centimeters']
        elif self.unit == 'millimeters':
            return conv_list['conv_millimeters']
            
      
    def feet(self):
       conv_list = {'conv_inches' :self.length/12,'conv_yards':self.length*3,'conv_miles':self.length*5280,
                    'conv_kmeters':self.length*3280.84,'conv_meters':self.length*3.281,
                    'conv_centimeters':self.length/30.48,'conv_millimeters':self.length/304.8}
   
        if self.unit == 'inches':
            return conv_list['conv_inches']
        elif self.unit == 'yards':
            return conv_list['conv_yards']
        elif self.unit == 'miles':
            return conv_list['conv_miles']
        elif self.unit == 'kilometers':
            return conv_list['conv_kmeters']
        elif self.unit == 'meters':
            return conv_list['conv_meters']
        elif self.unit == 'centimeters':
            return conv_list['conv_centimeters']
        elif self.unit == 'millimeters':
            return conv_list['conv_millimeters']
    def yards(self):
        conv_list = {'conv_feet':self.length/3,'conv_inches':self.length/36,'conv_miles':self.length*1760,
                     'conv_kmeters':self.length*1093.613,'conv_meters':self.length*1.094,'conv_centimeters':self.length*91.44,
                     'conv_millimeters':self.length*914.4}
        
        if self.unit == 'inches':
            return conv_list['conv_inches']
        elif self.unit == 'feet':
            return conv_list['conv_feet']
        elif self.unit == 'miles':
            return conv_list['conv_miles']
        elif self.unit == 'kilometers':
            return conv_list['conv_kmeters']
        elif self.unit == 'meters':
            return conv_list['conv_meters']
        elif self.unit == 'centimeters':
            return conv_list['conv_centimeters']
        elif self.unit == 'millimeters':
            return conv_list['conv_millimeters']

    def miles(self):
        conv_list = {'conv_feet':self.length/5280,'conv_yards':self.length/1760,'conv_inches':self.length/63360,
                     'conv_kmeters' = self.length/1.609,'conv_meters' = self.length/1609.344,
                     'conv_centimeters' = self.length/160934.4,'conv_millimeters' = self.length*1.609e+6}

        if self.unit == 'inches':
            return conv_list['conv_inches']
        elif self.unit == 'feet':
            return conv_list['conv_feet']
        elif self.unit == 'yards':
            return conv_list['yards']
        elif self.unit == 'kilometers':
            return conv_list['conv_kmeters']
        elif self.unit == 'meters':
            return conv_list['conv_meters']
        elif self.unit == 'centimeters':
            return conv_list['conv_centimeters']
        elif self.unit == 'millimeters':
            return conv_list['conv_millimeters']


    def kilometers(self):
       conv_list = {'conv_feet':self.length/3280.84,'conv_yards':self.length/1093.613,'conv_miles':self.length*1.609,
                    'conv_meters':self.length/1000,'conv_centimeters':self.length/100000,'conv_millimeters':self.length/1e+6,
                    'conv_inches':self.length/39370.079}
       
        if self.unit == 'inches':
            return conv_list['conv_inches']
        elif self.unit == 'feet':
            return conv_list['conv_feet']
        elif self.unit == 'yards':
            return conv_list['yards']
        elif self.unit == 'miles':
            return conv_list['miles']
        elif self.unit == 'meters':
            return conv_list['conv_meters']
        elif self.unit == 'centimeters':
            return conv_list['conv_centimeters']
        elif self.unit == 'millimeters':
            return conv_list['conv_millimeters']


    def meters(self):
        conv_list = {'conv_feet':self.length/3.281,'conv_yards':self.length/1.094,'conv_miles':self.length*1609.344,
        'conv_kmeters':self.length/1000,'conv_inches':self.length/39.37,'conv_centimeters':self.length/100
        'conv_millimeters':self.length/1000}

        if self.unit == 'inches':
            return conv_list['conv_inches']
        elif self.unit == 'feet':
            return conv_list['conv_feet']
        elif self.unit == 'yards':
            return conv_list['yards']
        elif self.unit == 'miles':
            return conv_list['miles']
        elif self.unit == 'kilometers':
            return conv_list['conv_kmeters']
        elif self.unit == 'centimeters':
            return conv_list['conv_centimeters']
        elif self.unit == 'millimeters':
            return conv_list['conv_millimeters']

    def centimeters(self):
        conv_list = {'conv_feet':self.length*30.48,'conv_yards':self.length*91.44,'conv_miles':self.length*160934.4,
                     'conv_inches':self.length*2.54,'conv_meters':self.length*100,'conv_kmeters':self.length*100000,
                    'conv_millimeters':self.length/10}

        if self.unit == 'inches':
            return conv_list['conv_inches']
        elif self.unit == 'feet':
            return conv_list['conv_feet']
        elif self.unit == 'yards':
            return conv_list['yards']
        elif self.unit == 'miles':
            return conv_list['miles']
        elif self.unit == 'kilometers':
            return conv_list['conv_kmeters']
        elif self.unit == 'meters':
            return conv_list['conv_meters']
        elif self.unit == 'millimeters':
            return conv_list['conv_millimeters'] 
    
    def millimeters(self):
        conv_list = {'conv_feet':self.length*304.8,'conv_yards':self.length*914.4,'conv_miles':self.length*1.609e+6,
        'conv_kmeters':self.length*1e+6,'conv_inches':self.length*25.4,'conv_centimeters' = self.length*10,
        'conv_meters' = self.length*1000}
        
        if self.unit == 'inches':
            return conv_list['conv_inches']
        elif self.unit == 'feet':
            return conv_list['conv_feet']
        elif self.unit == 'yards':
            return conv_list['yards']
        elif self.unit == 'miles':
            return conv_list['miles']
        elif self.unit == 'kilometers':
            return conv_list['conv_kmeters']
        elif self.unit == 'meters':
            return conv_list['conv_meters']
        elif self.unit == 'centimeters':
            return conv_list['conv_centimeters']


user_input = eval(input('Enter an integer: '))
unit = input('Enter a unit ')
a = Converter(user_input,unit)
print(a.inches())

        
        
