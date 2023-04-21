import datetime

inputSymbol = input ("Please Enter in a symbol in all caps: ")

if inputSymbol.isalpha() == True and inputSymbol.isupper() == True and len(inputSymbol) <= 7:
    print("Your symbol has been successfully entered.")
else:
    print("This is not a valid symbol type!")

try:
    chart_type = int(input("Please enter either Chart Type 1 or 2: "))
    if (chart_type == 1 or 2):
        print("Chart type has been saved successfully.")
    else:
        print("This is not a valid chart type.")
except ValueError:
    print("Please choose a valid chart type!")

try:
  input_time_series = int(input("Please enter a time series 1-4: ")) 
  if input_time_series > 0 and input_time_series < 5:  
    print("Time series has been successfully saved.") 
  else:
    print("This is not a valid time series input.") 
except ValueError:
  print("Value Error, please reenter.") 

date_string = input("Enter Start Date: YYYY-MM-DD ") 
date_format = '%Y-%m-%d'

try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print("Start date has been successfully saved.") 
except ValueError:
  print("Error: Format must be in YYYY-MM-DD format.")

date_string = input("Enter End Date: YYYY-MM-DD ") 
date_format = '%Y-%m-%d'

try:
  date_obj = datetime.datetime.strptime(date_string, date_format) 
  print("End date has been successfully saved.") 
except ValueError:
  print("Error: Format must be in YYYY-MM-DD format")
