def divide(ourdivdend, ourdivisor):
    sign = (-1 if(ourdivdend<0)^(ourdivisor<0) else 1);
    ourdivdend = abs(ourdivdend);
    ourdivisor = abs(ourdivisor);
    quotientNum = 0
    tempNum = 0
    for i in range(31, -1, -1):
        if(tempNum + (ourdivisor<<i) <= ourdivdend):
            tempNum += ourdivisor << i
            quotientNum |= 1 << i
    if sign == 1:
        quotientNum = -quotientNum
    return quotientNum

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))  
print("Result of", a,"/", b,"is", divide(a, b))