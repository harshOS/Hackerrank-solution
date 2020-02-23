def staircase(n):
    for i in range(1,n+1):
        string = (n-i)*' ' + (i*'#') # line to print for every loop
        print(string)

staircase(6)