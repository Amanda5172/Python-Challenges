#Exercise 1
for i in range(1000):
    print("We like Python's turtles!")

#Exercise 2
Attributes: brand, serial number, price
Method: input, process, output
  
#Exercise 3
months=['January','February','March','April','May','June','July','August','September','October','November','December']

for i in months:
    print("One of the months of the year is %s." %i)

#Exercise 4
import turtle

t=turtle.Turtle()
t.lt(3645)

#rotates left, faces north east

#Exercise 5
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#a
for i in xs:
    print(i)
#b
for u in xs:
    print(u)
    print(u**2)
#c
total=0
for k in xs:
    total=total+k
print(total)
#d
product=1
for k in xs:
    product=product*k
print(product)

#Exercise 6
import turtle
t=turtle.Turtle()

def sh(s):
    for i in range(s):
        t.fd(50)
        t.lt(360/s)


t.pu()
t.goto(-200,0)
t.pd()

sh(3)

t.pu()
t.goto(-130,0)
t.pd()

sh(4)

t.pu()
t.goto(-30,0)
t.pd()

sh(6)

t.pu()
t.goto(100,0)
t.pd()

sh(8)
