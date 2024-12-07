for i in range(5):
    print(i*i)
for d in [3,1,4,1,5]:
    print(d,end="")
for i in range(4):
    print("Hello")
for i in range(5):
    print(i,2**i)
type(7.4)
abs(4-20//3)**3
type(8)
3*10//3+10%3
type(11)
def main():
    print("This program find the solution to the sum of natural numbers")
    print()
    n=float(input("Enter value of n:"))
    sum=(n*(n-1))//2
    print()
    print("The solution is:",sum)
main()
import math
def main():
    print("This program find the solution for the surface area of a sphere")
    print()
    r=float(input("Enter the readius, r, of the sphere:"))
    sum=(4*math.pi*(r**2))
    print()
    print("The surfcae area of your sphere is:",sum)
main()
for i in [1,3,5,7,9]:
    print(i,":",i**3)
    print(i)
x=2
y=10
for j in range(0, y, x):
    print(j, end+"")
    print(x+y)
    print("done")
def main():
    print("This program finds the slope of a line through the coordinates (x1,y1) and (x2,y2)")
    print()
    x1=float(input("Enter value of x1:"))
    y1=float(input("Enter value of y1:"))
    x2=float(input("Enter value of x2:"))
    y2=float(input("Enter value of y2:"))
    sum=(y2-y1)/(x2-x1)
    print()
    print("The slope is:",sum) 
main()
def main():
    print("This program finds the distance of a line between the coordinates (x1,y1) and (x2,y2)")
    print()
    x1=float(input("Enter value of x1:"))
    y1=float(input("Enter value of y1:"))
    x2=float(input("Enter value of x2:"))
    y2=float(input("Enter value of y2:"))
    distance=math.sqrt(((x2-x2)**2)+((y2-y1)**2))
    print()
    print("The distance is:",distance)
main()
def main():
     print("This program finds the distance of a line between the coordinates (x1,y1) and (x2,y2)")
     print()
     x1=float(input("Enter value of x1:"))
     y1=float(input("Enter value of y1:"))
     x2=float(input("Enter value of x2:"))
     y2=float(input("Enter value of y2:"))
     distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
     print()
     print("The distance is:",distance)
main()
