def trial_and_error(input_amount):#verify valid numeric inputs with an internal loop 
  repeat_loop = 1
  while(repeat_loop == 1):
  
    try: 
      input_amount = float(input()) 
      return input_amount 
    except ValueError: 
      print('Please only input digits') 
    
repeat_loop = 1
while(repeat_loop == 1):#Loops code to allow continuous calculation
  
#This section gets data from the user and verifies that only digits are taken via the
#trial_and_error function
  print("Account Balance ($): ") 
  balance = trial_and_error(input)
  
  print("Risk Percentage (%): ")
  risk_percentage = trial_and_error(input)
  
  print("Stop-Loss (pips): ")
  stop_loss = trial_and_error(input)
  
  print("Pip Value: ")
  pip_value = trial_and_error(input)

# Calculation and Formula
  needed_lots_0 = ( balance * risk_percentage) / (stop_loss * pip_value * 100 )

# Rounding to 2 Decimals
  needed_lots = round( needed_lots_0 , 2) 

# Display the result
  print("Your ideal position size is: ", needed_lots, "Lot(s)")
  
  string = input("Would you like to use this calculator again? Yes or No")
  choice = string.upper()
  
#Ends our loop if need be  
  if(choice == "NO"):
    repeat_loop = 0
    print("Thank you for using the Lot Size Calculator!")
  else:
    print("\n")
  

    