print("Hello, world!")
print("Hello","world!")
print(3)
print(3.0)
print(2+3)
print(2.0+3.0)
print("2"+"3")
print(2*3)
print(2**3)
print(7/3)
print(2//3)
def main():
    print("This program illustates a chaoticfunction")
    x=eval(input("Enter a number between 0 and 1:"))
    n=eval(input("How many numbers should I print?:"))
    for i in range (n):
        x=3.9*x*(1-x)
        print(x)
main()
def main():
    print("This program converts kilometers to milels")
    kilometers=eval(input("How many kilometers?:"))
    miles=.62*kilometers
    print("The distance is",miles,"miles")
main()
def main():
     print("This program computes compound interest")
     t=eval(input("How many years?"))
     P=10000
     n=12
     r=.08
     A=P*(1+(r/n))**(n*t)
     print("your compound interest is",A,"dollars after",t,"years")
main()
