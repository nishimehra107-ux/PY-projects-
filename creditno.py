credit_num="1234-5678-90123-4567"

last_digit= credit_num [-4:]

#print(credit_num [0])
#print(credit_num [3])
#print(credit_num [0:5])
#print(credit_num [:6])
#print(credit_num [-4])
#print(credit_num [::2])
#print(credit_num [2:9:2])
#print(credit_num [-1:-10:-2])

#print(f"your credit card number is XXXX-XXXX-XXXX-{last_digit}")

credit_num= credit_num[::-1]
print(credit_num)