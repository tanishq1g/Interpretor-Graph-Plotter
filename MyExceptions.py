class invalid_brackets(Exception):            #If no of brackets or order of brackets is wrong

  	def message(self):
  		a='error in giving brackets'
  		return a

class last_is_operator(Exception):            #If the last no is missing 
   
    def message(self):
     	a='Last number is missing'
     	return a

class first_is_operator(Exception):           #If first number is missing
  
  	def message(self):
  		a='first number is missing'
  		return a

class operator_side_by_side(Exception):       #If there are any operators side by side except uninary operator
  	def message(self):
  		a='number is missing'
  		return a

class invalid_variable(Exception):            #If there is any variable which is not declared    
  	def message(self):
  		a='variable is not declared'
  		return a

class first_ch_is_digit(Exception):           #If there is any variable which has ist charecter as a number 
	
	def message(self):
		a='first character can\'t be a digit'
		return a 

class no_spaces(Exception):                   #If there is any variable which have spaces
	
	def message(self):
		a='no spaces allowed '
		return a 

class invalid_characters(Exception):          #If there is any variable which other symbols except "_"
	
	def message(self):
		a='characters are invalid'
		return a 

class invalid_number(Exception):              #If any number consists of a charecter
	
	def message(self):
		a='number is not valid'
		return a 

class keyword(Exception):                     #If user uses any key word ('exit()','clear all','pi','e','PI')as a variable

  	def message(self):
  		a='variable name can\'t be a keyword'
  		return a





