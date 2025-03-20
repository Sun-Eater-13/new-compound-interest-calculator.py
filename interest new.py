def two_digits(messsage):
    global control
    try:
        digits = float(input(messsage))
        if digits >= 0:
            digits1 = round(digits, 2)
            if digits1 == digits:
                control += 1
                return digits
            else:
                print("Input proper number")
        else:
            print("Input proper number")
    except ValueError:
        print("Input proper number")

control=0
while   control<5:
    if control==0:
        initial=two_digits("Input initial investment (no more than 2 digits after the decimal): ")
        if control==1:
            final=initial
    elif control==1:
        deposit=two_digits("Input additional deposit  (no more than 2 digits after the decimal): ")
    elif control==2:
        try:
            period=str(input("Is the additional deposit annual and monthly (A/M)? "))
            if period=="A" or period=="M":
                control+=1
            else:
                print("Input A or M")
        except ValueError:
            print("Input proper letter")
    elif control==3:
        try:
            time=int(input("Input number of periods (no digits after the decimal): "))
            if time>0:
                control += 1
            else:
                print("Input proper number of periods")
        except ValueError:
            print("Input proper number of periods")
    else:
        interest=two_digits("Input interest rate (in %, no more than 2 digits after the decimal): ")
        if period == "M":
            interest = interest / 1200
        else:
            interest = interest/100
for i in range (1, time + 1):
    final=round(final * (1 + interest) + deposit, 2)
if period=="A":
    print(f"With initial investment {initial}, additional annual deposit {deposit} and {interest * 100}% interest rate after {time} years you will have {final}")
else:
    print(f"With initial investment {initial}, additional monthly deposit {deposit} and {interest * 1200}% interest rate after {time} months you will have {final}")