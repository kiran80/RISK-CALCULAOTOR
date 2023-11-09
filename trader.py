print('HERE IS AN ATTEMPT TO TRADE WITH CALCULATED RISK, HENCE THE NAME')
print(' ********    RISK CALCULATOR *********        ')
print('Enter the funds that you want to trade')
funds=input()
funds=float(funds)
print('Transferred to your trading account INR',funds)
print('Now, decide on your risk percentage by entering a number')
riskpercentage=input()
riskpercentage=float(riskpercentage)
dayrisk=(funds*riskpercentage)/100
print("Mention the buy price of the stock")
buyprice=input()
buyprice=float(buyprice)
print("Mention the stoploss of the stock")
stoploss=input()
stoploss=float(stoploss)
gap=buyprice-stoploss
positionsize=float((dayrisk/gap))
x=int(positionsize)
print(x, " IS YOUR POSTION SIZE THAT YOU SHOULD NOT EXCEED WHILE BUYING STOCKS")
print('Now you need to exit the postions in 2 phases.Therefore we will divide the position size into 2 lots')
lot1=int(x/2)
target1=(0.6*gap)+buyprice
target2=(1*gap)+buyprice
print('FIRST LOT IS', lot1)
print('SELL THE FIRST LOT AT AT INR', target1)
print("SECOND LOT IS", lot1)
print('SELL THE SECOND LOT AT INR', target2)
print("**********THANKS FOR YOUR PATIENCE*************")


     
      
      
      





    
