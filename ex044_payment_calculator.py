price=float(input('Enter the price of the product: '))
payment=input('''Choose your payment method: 
[1] Cash 
[2] Debit card
[3] 2 payments on the card
[4] 3 or more payments on the card
Your choice is: ''')

if payment == '1':
    print(f"You selected option {payment}.")
    discount=((price*10)/100)
    final_price=price-discount
    print(f'The product paid in cash receives a 10% discount and costs {final_price:.2f} dollars.')

elif payment == '2':
    print(f"You selected option {payment}.")
    discount=((price*5)/100)
    final_price=price-discount
    print(f'The product paid in debit card receives a 5% discount and costs {final_price:.2f} dollars.')

elif payment == '3':
    print(f"You selected option {payment}.")
    final_price = price
    print(f'Paying in 2 installments on the card does not include a discount and costs {final_price:.2f} dollars.')
    installment=(price/2)
    print(f'You will pay 2 installments of {installment:.2f} dollars.')

elif payment == '4':
    print(f"You selected option {payment}.")
    installments=int(input('In how many installments do you wish to pay? '))
    interest=((price*20)/100)
    final_price1 = interest+price
    final_price2 = final_price1/installments
    print(f'Payment in {installments} installments of {final_price2:.2f} dollars each, total cost {final_price1:.2f} dollars (including 20% interests).')

else:
    print("Invalid option. Please choose 1, 2, 3 or 4.")