amt_spent = int(input("Enter the amount spent: "))
loyalty_program = input("Are you part of the loyalty program(True/False): ") 
if amt_spent >= 10000:
    total_bill= amt_spent - (amt_spent * 0.2) 
    print(f"Total Bill: {total_bill}")
elif amt_spent >= 10000 and loyalty_program == "True":
    total_bill= amt_spent - (amt_spent * 0.25) 
    print(f"Total Bill: {total_bill}")
elif amt_spent < 10000 and loyalty_program == "False":
    total_bill= amt_spent - (amt_spent * 0.05) 
    print(f"Total Bill: {total_bill}")
