def number_pattern(n): #function definition
  number_list = '' # an empty string for having equally spaced numbers
  if isinstance(n, int) == False:
    return "Argument must be an integer." # To check if the argument passed is an integer or not
  if n <= 0:
    return "Argument must be an integer greater than 0." # To check if the argument passed is greater than 0
  if isinstance(n, int): 
    for n in range(n): # To print the numbers in range
      number_list += str(n+1) + ' ' # Adds 1 and converts the integers to string and concatenates them with a space
    return number_list.strip() # returns the equally spaced string of numbers and strips of extra whitspaces

result = number_pattern() #The function call, pass an integer here
print(result)


    
  
