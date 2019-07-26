from math import sqrt

# This method is for soving a discriminant
def solveDiscriminant(descriminant):
    a = 0; b = 0; c = 0; wasOperator = False
    for i in range(0, len(descriminant)+1):
        if descriminant[i] == '^':
            a = int(descriminant[i-1])
        if isOperator(i):
            if wasOperator == False:
                b = int(descriminant[i-1])
                wasOperator = True
            else:
                c = int(descriminant[i+1])

    # finding discriminant
    D = b**2 - 4*a*c

    # if D > 0 then discriminant has 2 roots
    if D > 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        listOfX = [x1, x2]
        listOfResult = []

        # Converting results of the descriminant to string
        for i in listOfX:
            if i < 0:
                listOfResult.append('(x + ' + str(abs(i)) + ') ')
            else:
                listOfResult.append('(x - ' + str(i) + ')')

        return listOfResult

    # if D == 0 then discriminant has 1 root
    elif D == 0:
        result = ''
        x = -b / (2*a)
         # Converting results of the descriminant to string
        if x < 0:
            result = '(x + ' + str(abs(i)) + ')'
        else:
            result = '(x - ' + str(i) + ')'

        return result

    # if D < 0 then discriminant has no roots
    else:
        return False

    
# This method is called when the limit aims to number        
def solveEquation(lim, equation):
    fullEquation = []
    for i in range(0, len(equation)+1):
        if 'x' == equation[i] and equation[i].isdigit():
            fullEquation.append('*' + lim)
        else:
            fullEquation.append(equation[i])

    result = ''.join(fullEquation).replace('x', lim)
    return int(eval(result))

# this method checks whether expression has plus/minus            
def isOperator(opr):
    ops = '+-'
    for i in ops:
        if i == opr:
            return True
        else:
            return False

def checkExpression(equation):
    if 'x^2' in equation and :

# ----- MAIN BODY --------
# Asking the aim of limit
lim = input('Enter aim of limit: ')
# Asking to enter the expression itself
equation = input('Write down the equation: ').replace('^', '**')

# This condition checkes whether the limit aims to number or infinity
if lim.isdigit():
    equationParts = equation.split('/')
    if len(equationParts) < 2:
        print(checkExpression(equation))
#else:
    