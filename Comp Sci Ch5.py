s1="spam"
s2="ni!"
s1[1]
s1[2]+s2[:2]
s1.upper()
s2[:2].upper()
s1.lower()
[s1[:2],s1[-1]]
for w in "Now is the winter of our discontent...".split():
    print(w)
for w in "Mississippi".split("i"):
    print(w, end=" ")
msg=""
for ch in "secrest":
    msg=msg+chr(ord(ch)+1)
print(msg)
def main():
    print("Grade String\n")
    print("Please enter the count of each grade")
    a=int(input("A's: "))
    b=int(input("B's: "))
    c=int(input("C's: "))
    d=int(input("D's: "))
    f=int(input("F's: "))
    A1="A"
    B1="B"
    C1="C"
    D1="D"
    F1="F"
    total=F1*f+D1*d+C1*c+B1*b+A1*a
    print("grade string=",total)
main()
def main():
    print("Grade String\n")
    print('Please enter the count of each grade: ',end='')
    print()
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
main()
def main():
    #score is a list as a look up table
    score=['F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','D','D','D','D','D','D','D','D','D','D','C','C','C','C','C','C','C','C','C','C','B','B','B','B','B','B','B','B','B','B','A','A','A','A','A','A','A','A','A','A','A']
    n=int(input("Enter Score(0-100): "))
    print("The letter grade of your score is", score[n]+".")
main()
def main():
    print("This program will give you an acronym for the phrase of your choosing")
    phrase=input("Enter the phrase you would like an acronym for: ").upper()
    words=phrase.split()
    acronym=""
    for word in words:
        acronym= acronym+word[0]
    print("Your acronym is:", acronym)
main()
def main():
    print("This program converts a single name into its numeric value")
    name=input("Enter a name: ").upper()
    total_value= 0
    print("\nHere is the unicode: ")
    for i in name:
        letter_value=ord(i)-ord('A')+1
        total_value= total_value+letter_value
    print("The numeric value for your name is: ", total_value)
main()
