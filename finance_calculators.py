# The below program is a financial calculator.
# User has access to two different ( investment and home loan )
# If user choice is investment, the program will output the amount after
# Users conditions i.e amount to deposit, interest rate, number of years and interest type ( Simple or Compound )
# If home loan, program will output the amount to repay every month.

# import math module.

import math

user_choice = input('Choose either \' investment \' or \' bond \' from the menu below to proceed: \n'
                    'investment   - to calculate the amount of interest you\'ll earn on interest \n'
                    'bond         - to calculate the amount you\'ll have to pay on a home loan ').upper()

if user_choice == 'INVESTMENT':
    deposit_money = int(input('How much are you deposit for the investment? '))
    interest_rate = int(input('Enter the interest rate (NUMBER ONLY) for investment? '))
    years = int(input('Enter the number of years you plan on investing? '))
    interest = input('Enter the preferred interest \'simple \n or \'compound \' ?').upper()

    if interest == 'SIMPLE':
        amount = deposit_money * (1 + (interest_rate / 100) * years)
        print(f'The investment with a deposit of {deposit_money} and '
              f'interest rate of {interest_rate}% for a period of {years} years with a '
              f'{interest.lower()} interest will amount to {amount}'.format(deposit_money, interest_rate, years,interest, amount))
    else:
        amount = deposit_money * (1 + interest_rate / 100) ** years
        print(f'The investment with a deposit of {deposit_money} and '
              f'interest rate of {interest_rate}% for a period of {years} years with a '
              f'{interest.lower()} interest will amount to {amount}'.format(deposit_money, interest_rate, years,interest, amount))

else:
    deposit_money = int(input('How much are you deposit for the bond loan? '))
    interest_rate = int(input('Enter the interest rate (NUMBER ONLY) for bond loan? ')) / 100
    months = int(input('The number of months to repay the bond loan? '))

    repayment = (interest_rate/12 * deposit_money) / (1 - (1 + interest_rate/12) ** (-months))

    print(f'The home bond loan with a deposit of {deposit_money} and '
          f'interest rate of {int(interest_rate * 100)}%  will be repaid after a period of {months} months '
          f' will amount to {repayment} per month.'.format(deposit_money, interest_rate, months, repayment))
