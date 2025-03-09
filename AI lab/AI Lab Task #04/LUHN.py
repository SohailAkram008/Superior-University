# LUHN algoritham
cardNumber=[4,7,8,2,7,8,0,0,0,1,6,1,6,4,0,1]

cardNumber.pop()
print(cardNumber)
cardNumber.reverse()
print(cardNumber)
for i in range(0,len(cardNumber)):
    if i % 2==0:
        cardNumber[i]*=2
       
print(cardNumber)
for i in range(0,len(cardNumber)):
    if cardNumber[i] >= 9:
        cardNumber[i]-=9
print(cardNumber)

sumOfList=sum(cardNumber)+1
print(sumOfList)
if sumOfList %10==0:
    print("Valid card")
else:
    print("Not Valid Card")    