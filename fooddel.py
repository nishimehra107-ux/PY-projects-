amount=int(input("enter order amount: "))
coupon=input("do you have a coupon code?(y/n): ")
if coupon=="y":
    code=input("enter your coupon code: ")
    if code=="CREAM30":
        discount=amount*0.3
        total=amount-discount
        print(f"you have saved {discount} and your total amount is {total}")
        