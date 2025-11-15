am=50
while True:
     print("Amount Due:", am)
     x=int(input("Insert Coin: "))
     if x!=5 and x!=25 and x!=10:
        continue
     am = am - x
     if am<=0:
        print("Change Owed:", -am)
        break
