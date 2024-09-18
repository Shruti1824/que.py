num=int(input("Enter any positive number"))
try:
    if num<=0:
        raise
        ValueError("Positive number is correct ")
    else:
        raise
        ValueError("Negitive number is incorrect")
except ValueError as e:
     print(e)