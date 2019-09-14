
def summation(n1,n2):
    summ = 0
    for i in range(n1, n2):
        summ +=i
    return(summ)


def contfractions(n):
    numerator = []
    denominator = []

    numerator.append(1)
    denominator.append(1)

    for i in range (n):
        numerator.append(numerator[i] + 2 *(denominator[i]))
        denominator.append(numerator[i] + denominator[i])
    return(numerator, denominator)


def isequal(num1, num2):
    check1 = num1/2
    check2 = num2/2

    if summation(1,check1) == summation(check1 + 1, check2+1):
        return True
    else:
        return False
    


numerator, denominator = contfractions(23)

try:
    for i in range(2,len(numerator)+1):
       if isequal(denominator[i], numerator[i]) == True:
            print "K:",denominator[i]/2, "N:",numerator[i]/2
except IndexError:
    print("All 32 bit integer values of K and N printed")

               



