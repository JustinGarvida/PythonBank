#Name: Justin Garvida
#Date: 04/23/23
#Purpose: To simulate a bank account using OOP concepts and ovveride methods


from money import Money
import inputroutines


balance = Money() #creates Money object with 0 dollars and 0 cents
while True:
    print("1. Deposit\n2. Withdraw\n3. See current balance\n4. Exit")
    option = input("Enter your choice: ")
    if option == "1": #if option is 1, user will deposit funds
        print("Deposit")
        print("Enter the dollar amount:")
        dollars = inputroutines.intInRange(0,1000) #checks to see if input is within valid range
        print("Enter the cents amount:")
        cents = inputroutines.intInRange(0,99) #checks to see if input is within valid range
        deposit = Money(dollars,cents)
        balance += deposit #deposit amount will be added to balance 
        print("Transaction completed.")
    
    elif option == "2": #if option is 2, user will withdraw funds
        print("Withdraw")
        print("Enter the dollar amount:")
        dollars = inputroutines.intInRange(0,1000) #checks to see if input is within valid range
        print("Enter the cents amount:")
        cents = inputroutines.intInRange(0,99) #checks to see if input is within valid range
        withdraw = Money(dollars,cents)
        if withdraw >= balance: #will return error statement if withdraw amount is greater or equal to current balance 
            print("You do not have enough funds.")
        else:
            balance -= withdraw #if valid, withdraw amount will be subtracted from balance
            print("Transaction completed.")
        
    elif option == "3": #if option is 3, then balance statement will print
        print(f"Your current balance is: {balance}")
        
    elif option == "4": #if option is 4, then the program will break from the loop, ending the program.
        print("Good-bye!")
        break
    else:
        print("\nInvalid choice. Try again.") #if user does not enter a choice 1-4, an error message will be given and program will reprompt for choice.
        continue
    
    
    