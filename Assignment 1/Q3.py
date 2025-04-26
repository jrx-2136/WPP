Units=['1.inches','2.yards','3.miles','4.millimeters','5.centimeters','6.meters','7.kilometers']
convert=[12,0.3,0.0001,304.8,30.48,0.3048,0.0003]
a=int(input("Enter length in feet:"))
print(Units)
b=int(input("Enter option to convert to:"))
result=a*convert[b-1]
print(result)