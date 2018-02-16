from MyExceptions import *
from arith import *
								#Giving values to global variable as pi and e
PI=3.14159
pi=3.14159
e=2.71828

var_names={'PI':3.14159,'pi':3.14159,'e':2.71828}
class Value_Assigning:
	
	def defining_var(self,inp):
		keywords=['exit()','clear all','pi','e','PI','sin','cos','tan','log']	
		string=""
		value=""
		for x in range(len(inp)):			# Assigning a value to the variable if we find an '=' sign
			if inp[x]!='=': 
				string=string+inp[x] 		#Till we get an '=' sign considering it as a variable name
			elif inp[x]=='=':
				for y in inp[x+1:]:
					value=value+y			#Once we get an '=' sign the characters after it are considred as value
				break

		while string[-1] is " ":
			string=string[:-1]
		while value[0] is " ":
			value=value[1:]					#The value is given by removing space
		
		try:
			if self.check_var_name(string):
				if string in keywords:
					raise keyword()			#As variable cannot be a key word
				else:
					a=preparing_arithmetic()
					value=a.insert_spaces(value)
					a=str(value)
					a=a.replace('e-','')
					a=a.replace('e+','')
					if a[0]==" ":
						a=a[1:]
					a=a.replace('.','')
					if a.isdigit():
						pass
					else: 					#If the assigned value is not a number it raises an error or even if the variable is invalid
						try:
							errors(value)
							a=variable_names()
							value=a.names(value)
							a=solving()
							value=str(a.postfix(value))
							

						except (last_is_operator,first_is_operator,invalid_brackets,operator_side_by_side,invalid_variable,keyword) as X:
							return (X.message())
						except Exception:
							return ("INVALID SYNTAX")

					if self.check_val(value):			#If the given value is valid
						value=self.true_val(value)		#Value is replaced if the first charecter is '-' with the negation of the given value
						var_names[string]=value

		except (first_ch_is_digit ,no_spaces,invalid_characters,invalid_number,keyword)as X:		#Making sure that the entered variable name is correct
			return X.message()
		except Exception:
			self.output("INVALID SYNTAX")

		return ' '
	
	def check_var_name(self,string):   

		if string[0].isdigit() :						# there is no number at start
			raise first_ch_is_digit()
			
		elif ' ' in string:								# Checks the variable names and make sure that there are no spaces
			raise no_spaces()
		flag=1
		for i in string:
			if i.isalnum() or i is "_":					#making sure that there shouldn't be any other symbols except '_'
	  			pass
			else:
	 			raise invalid_characters()
		if flag is 1:
			return 1

	def check_val(self,value):
		value=value.replace(" ","")
		a=value.replace(".","")
		if a[0].isdigit() or a[0] is '-':		#Making sure that there is a number or '-' at 1st place else it would be a wrong number
			pass
		else:
			raise invalid_number()
		for x in a[1:]:								#checking if all the other digits are numbers or not
			if x.isdigit():
				pass
			else:
				raise invalid_number()
		return 1
			
	def true_val(self,value):
		value=value.replace(" ","")
		negation=0
		if value[0] is '-':								#checking if the given value is negative 
			negation=1
			value=value[1:]
		value=float(value)
		if negation is 1:
			value=value-2*value 						#Returns a negative value if given is negative
		return value


class variable_names: 									#Checking if the variable names consist of any operators If it does then raising an error
	def names(self,inp):
		op=['+','-','/','*','^','%']
		for i in range(len(inp)):
			if any([ch.isalpha() for ch in inp[i]]):
				if inp[i] in var_names.keys(): 			#Substituting the value of the assigned variable which are stored in dictionary
					inp[i]=var_names[inp[i]] 
				else:
					raise invalid_variable
		return inp
