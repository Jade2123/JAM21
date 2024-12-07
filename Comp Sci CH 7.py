def main():
    print("This program will give you the letter value for your grade")
    score=eval(input("Please enter the exam score(0-100): "))
    if score>=90:
        if score<=100:
            grade="A"
    if score<=89:
        if score>=80:
            grade="B"
    if score<=79:
        if score>=70:
            grade="C"
    if score<=69:
        if score>=60:
            grade="D"
    if score<=59:
        if score>=0:
            grade="F"
    print("Your grade is:",grade)
main()
def main():
    start_hour=eval(input("Please enter the start hour (1-24): "))
    start_minute=eval(input("Please enter the start minute (0-59): "))
    end_hour=eval(input("Please enter the end hour (1-24): "))
    end_minute=eval(input("Please enter the end minute (0-59): "))
    start_total_minutes= (start_hour-1)*60+start_minute
    end_total_minutes= (end_hour-1)*60+end_minute
    total_bill=0
    before_9PM=2.50
    after_9PM=1.75
    change_time=21*60
    if end_total_minutes<=change_time:
        total_bill= ((end_total_minutes-start_total_minutes)/60)*before_9PM
    else:
        bill_before_9PM=((change_time-start_total_minutes)/60)*before_9PM
        bill_after_9PM=((end_total_minutes-change_time)/60)*after_9PM
        total_bill= bill_before_9PM+bill_after_9PM
    print(f"The total babbysitting bill is: ${ total_bill:.2f}")
main()
def main():
    age=eval(input("Please enter your age: "))
    citizen_time=eval(input("Please enter how long you have been a citizen for: "))
    if age<25:
        if citizen_time<7:
            senate=print("You are inelgible for Senate.")
            house=print("You are inelgible to be a US House representative.")
        else:
            senate=print("You are inelgible for Senate.")
            house=print("You are inelgible to be a US House representative.")
    if 30>age>=25:
        if citizen_time<7:
            senate=print("You are inelgible for Senate.")
            house=print("You are inelgible to be a US House representative.")
        else:
            senate=print("You are inelgible for Senate.")
            house=print("You are elgible to be a US House representative.")
    if age>=30:
        if citizen_time<7:
            senate=print("You are inelgible for Senate.")
            house=print("You are inelgible to be a US House representative.")
        if 7<=citizen_time<9:
            senate=print("You are inelgible for Senate.")
            house=print("You are elgible to be a US House representative.")
        else:
            senate=print("You are elgible for Senate.")
            house=print("You are elgible to be a US House representative.")
main()
def main():
    print("Grade String\n")
    print('Please enter the count of each grade: ',end='')
    print()
    try:
        a=int(input("A's: "))
        b=int(input("B's: "))
        c=int(input("C's: "))
        d=int(input("D's: "))
        f=int(input("F's: "))
        print("Your grade string is:")
        for i in range(a):
            print('A',end='')
        for i in range(b):
            print('B',end='')
        for i in range(c):
            print('C',end='')
        for i in range(d):
            print('D',end='')
        for i in range(f):
            print('F',end='')
        print("")
    except ValueError:
        print("Invalid input")
    except:
        print("\nSomething went wrong, sorry!")
main()
def main():
    print("This program gives you your letter grade")
    #score is a list as a look up table
    score=['F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','D','D','D','D','D','D','D','D','D','D','C','C','C','C','C','C','C','C','C','C','B','B','B','B','B','B','B','B','B','B','A','A','A','A','A','A','A','A','A','A','A']
    try:
        n=int(input("Enter Score(0-100): "))
        print("The letter grade of your score is", score[n]+".")
    except ValueError:
        print("Invalid input")
    except IndexError:
            print("Invalid input: try again with a number (0-100)")
    except:
        print("\nSomething went wrong, sorry!")
main()
