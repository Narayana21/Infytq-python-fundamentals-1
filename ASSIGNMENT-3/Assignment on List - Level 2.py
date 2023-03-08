'''
ARS Gems Store sells different varieties of gems to its customers.

Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased.
Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount.
If any gem required by the customer is not available in the store, then consider total bill amount to be -1.

Assume that quantity required by the customer for any gem will always be greater than 0.

Perform case-sensitive comparison wherever applicable.
'''

# for gem in reqd_gems:
    #     for g in gems_list:
    #         if gem==g:
    #             quantity=reqd_quantity.index(gem)
    #             price=price_list[g]
    #             bill_amount=bill_amount+(price*quantity)
    #         else:
    #             bill_amount=-1
    # if(bill_amount>30000):
    #     bill_amount=bill_amount*0.95

def calculate_bill_amount(gems_list,price_list,reqd_gems,reqd_quantity):
    bill_amount=0
    for i in reqd_gems:
        if i not in gems_list:
            bill_amount=-1
            return bill_amount
    for i in range(len(reqd_gems)):
        k=gems_list.index(reqd_gems[i])

        bill_amount+=price_list[k]*reqd_quantity[i]
    if bill_amount>30000:
        bill_amount=bill_amount-(5/100)*bill_amount
    return bill_amount


gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]
bill_amount=calculate_bill_amount(gems_list,price_list,reqd_gems,reqd_quantity)
print(bill_amount)

