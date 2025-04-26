class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def meters(self):
        if self.unit == 'inches':
            return self.length * 0.0254
        elif self.unit == 'feet':
            return self.length * 0.3048
        elif self.unit == 'yards':
            return self.length * 0.9144
        elif self.unit == 'miles':
            return self.length * 1609.34
        elif self.unit == 'kilometers':
            return self.length * 1000
        elif self.unit == 'meters':
            return self.length
        elif self.unit == 'centimeters':
            return self.length * 0.01
        elif self.unit == 'millimeters':
            return self.length * 0.001
        else:
            return "OUT OF RANGE"

    def inches(self):
        
        meters = self.meters()
        return meters / 0.0254

    def feet(self):
        
        meters = self.meters()
        return meters / 0.3048

    def yards(self):
        
        meters = self.meters()
        return meters / 0.9144

    def miles(self):
        
        meters = self.meters()
        return meters / 1609.34

    def kilometers(self):
        
        meters = self.meters()
        return meters / 1000

    def centimeters(self):
        
        meters = self.meters()
        return meters / 0.01

    def millimeters(self):

        meters = self.meters()
        return meters / 0.001


c = Converter(9, 'inches')
print("To meters",c.meters())     
print("To feet",c.feet())       
print("To centimeters",c.centimeters())  
print("To kilometers",c.kilometers())
print("To miles",c.miles())
print("To millimeters",c.millimeters())
print("To yards",c.yards())