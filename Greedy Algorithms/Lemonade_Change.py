
def lemonade_change(bills):
        five_bill = 0
        ten_bill = 0
        for i in bills:
                if i == 5:
                        five_bill +=1
                elif i == 10:
                        if five_bill == 0 : return False
                        ten_bill+=1
                        five_bill-=1
                else : 
                    if five_bill == 0 or ten_bill == 0 : return False
                    ten_bill-=1
                    five_bill-=1
        return True

'''
bills = [5, 5, 5, 10, 20]
print(lemonade_change(bills))

bills = [5, 5, 10, 10, 20]
print(lemonade_change(bills))
'''