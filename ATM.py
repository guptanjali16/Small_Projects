print("Welcome to Iron Bank of Bravoos ATM")
restart=('Y')
chances=3
balance=67.14
while chances>=0:
    pin=int(input('please Enter Your 4 Digit PIN:'))
    if pin==(1234):
        print("you entered your pin correctly\n");
        while restart not in ('n','NO','no','N'):
            print('please press 1 for your Balance\n')
            print('please press 2 to make withdrawal\n')
            print('please press 3 to pay in\n')
            print('please press 4 to return card\n')
            option=int(input("What would you like to choose? "))
            if option == 1:
                print("Your balance is $ ",balance,'\n')
                restart=input('would you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank you')
                break
            elif option == 2:
                option2=('Y')
                withdrawal=float(input("How Much Would you like to withdraw? \n"))
                if withdrawal in [10,20,40,60,80,100]:
                    balance=balance-withdrawal
                    print('\n your balance is now $',balance)
                    restart=input("would you like to go back? ")
                    if restart in ('n','NO','no','N'):
                        print("Thank you")
                        break
                elif withdrawal!=[10,20,40,60,80,100]:
                    print("Invalid Amount ,Please retry!!\n")
                    restart=('y')
                elif withdrawal==1:
                    withdrawal=float(input("please enter your Desired Amount: "))

            elif option == 3:
                pay_in=float(input("How Much Would you like to Pay In? \n"))
                balance=balance+pay_in
                print("Your balance is now $",balance)
                restart = input("would you like to go back? ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank You")
                    break


            elif option == 4:
                print("Please Wait Whilst Your Card is Returned....\n")
                print("Thank You for your service")
                break

            else:
                print("Enter a correct number. \n")
                restart=('y')

    elif pin!=('1234'):
        print('Incorrect Password')
        chances=chances-1
        if chances==0:
            print('\nNo more tries')
            break

