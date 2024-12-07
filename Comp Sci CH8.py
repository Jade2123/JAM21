def sum_of_series():
    total_sum=0
    while True:
        num=int(input("Enter a number (enter 999 to stop)"))
        if num==999:
            break
        total_sum=total_sum+num        
def numbers_sum(n):
    total_sum=0
    i=1
    while i <= n:
        total_sum=total_sum+i
        i=i+1
def Fib_sequence(n):
    if n==1 or n==2:
        return 1
    return Fib_sequence(n-1)+Fib_sequence(n-2)
def main():
    n=int(input("Enter the position of the Fibonacci value you would like: "))
    print("Your Fibanacci nubver is: ",Fib_sequence(n))
main()
def syr_sequence(x):
    if x==1:
        return[1]
    if x%2==0:
        return [x]+syr_sequence(x//2)
    else:
        return [x]+syr_sequence(3*x+1)

    
def main():
    x=int(input("Enter the start value (whole number): "))
    sequence=syr_sequence(x)
    print("Your syracuse sequence is:", sequence)
main()
