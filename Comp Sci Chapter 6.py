def sing():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

    
def farm(animal):
    print("And on that farm he had a", animal+ ", Ee-igh, Ee-igh, Oh!")

    
def sound_1(noise):
    print("With a", noise+ ",", noise+ " here and a", noise+ ",", noise+ " there.")
    print("Here a", noise+ ", there a", noise+ ", everywhere a", noise+ ",", noise+ ".")

    
def sing_OldMcDonald():
    sing()
    farm("cow")
    sound_1("moo")
    sing()
sing_OldMcDonald()
def sing_OldMcDonald():
    sing()
    animals=[("cow", "moo"),("duck", "quack"), ("pig", "oink"), ("sheep", "bah"),("dog", "bark")]
    for animal, sound in animals:
        farm(animal)
        sound_1(sound)
        sing()
sing_OldMcDonald()
def find_average(n):
    total_sum= 0
    for i in range(n):
        num= float(input("Enter your number: "))
        total_sum= total_sum + num
    return total_sum/n

def main():
    print("This program will find the average of your numbers.")
    n = int(input("Enter how many numbers you would like to have averaged: "))
    average = find_average(n)
    print("The average of your numbers is:", average)
main()
import math
from graphics import*
def find_slope(dx,dy):
    return dy/dx
def find_length(dx,dy):
    return math.sqrt(dx**2+dy**2)
def main():
    win=GraphWin("Line Segment Information")
    point1=win.getMouse()
    point2=win.getMouse()
    line=Line(point1,point2)
    line.draw(win)
    midpointx=(point1.getX()+point2.getX())/2
    midpointy=(point1.getY()+point2.getY())/2
    midpoint=Point(midpointx, midpointy)
    midpoint.setFill("cyan")
    midpoint.draw(win)
    dx=point2.getX()-point1.getX()
    dy=point2.getY()-point1.getY()
    slope=find_slope(dx,dy)
    length=find_length(dx,dy)
    ltext=Text(Point(50,50),f"Length is:{length:.2f}")
    ltext.draw(win)
    stext=Text(Point(50,60),f"Slope is:{slope:.2f}")
    stext.draw(win)
    win.getMouse()
    win.close()
main()
def sumList(nums):
    total_sum= 0
    for i in range (nums):
        num= int(input("Enter your number: "))
        total_sum= total_sum + num
    return total_sum
def main():
    print("This program will find the sum of your numbers")
    num = int(input("Enter how many numbers are to be summed: "))
    total_sum = sumList(num)
    print("The sum of your numbers is:", total_sum)
main()
def sumList(nums):
    total_sum= sum(nums)
    return total_sum
def main():
    print("This program will find the sum of your numbers")
    num = int(input("Enter how many numbers are to be summed: "))
    nums=[]
    for i in range (num):
        num_get= int(input("Enter your number:"))
        nums.append(num_get)
        total_sum= sumList(nums)
    print("The sum of your numbers is:",total_sum)
main()
def get_some_strings(num):
    string_list=[]
    for i in range(num):
        strings=input("Enter String: ")
        string_list.append(strings)
    return string_list
def main():
    number_strings=int(input("Enter the number of strings there will there be: "))
    string=get_some_strings(number_strings)
    print("Here are your strings:")
    print(string)
main()
