from Value_Assigning import*
from MyExceptions import *
from arith import *
from Value_Assigning import *

PI=3.14159
pi=3.14159
e=2.71828

class bool:

	def check(self,inp):				#This function will check if a==b is true or not 	
		self.inp=inp
		ind=self.inp.find('==')			# checking if '==' is there and dividing the strings before and after it
		str1=self.inp[:ind]
		str2=self.inp[ind+2:]

		while str1[-1] is " ":
			str1=str1[:-1]
		while str2[0] is " ":
			str2=str2[1:]

		
		if str1 in var_names.keys():
			if str2 in var_names.keys():
				if var_names[str1]==var_names[str2]:		# if both strings are equal returns True
					return True
				else:
					return False
			else:
				raise invalid_variable 						# checking if variable is valid
		else:
			raise invalid_variable

class increment: 											#This class will define a+=2 as a=a+2
	def check(self,inp):
		self.inp=inp
		ind=self.inp.find('+=')								#checking if there is any "+=" in the input 
		str1=self.inp[:ind]
		str2=self.inp[ind+2:]

		while str1[-1] is " ":								#removing spaces
			str1=str1[:-1]
		while str2[0] is " ":
			str2=str2[1:]

		if str1 in var_names.keys():
			a=preparing_arithmetic()
			self.inp=a.insert_spaces(str1+'+'+str2)			#Now an arthimatic expression will be created with spaces required
			

			errors(self.inp)
			a=variable_names() 								#checking for errors in variable names 
			self.command=a.names(self.inp)
			a=solving()
			var_names[str1]=a.postfix(self.inp) 			# passing newly constucted sting to postfix expression
		else:
			raise invalid_variable	

class decrement:											#This class will define a-=2 as a=a-2
	def check(self,inp):
		self.inp=inp
		ind=self.inp.find('-=')								#checking if there is any "-=" in the input
		str1=self.inp[:ind]
		str2=self.inp[ind+2:]

		while str1[-1] is " ":								#removing spaces
			str1=str1[:-1]
		while str2[0] is " ":
			str2=str2[1:]

		if str1 in var_names.keys():
			a=preparing_arithmetic()
			self.inp=a.insert_spaces(str1+'-'+str2)			#Now an arthematic expression will be created with spaces required
			

			errors(self.inp)
			a=variable_names()								#checking for errors in variable names
			self.command=a.names(self.inp)
			a=solving()
			var_names[str1]=a.postfix(self.inp)				# passing newly constucted sting to postfix expression
		else:
			raise invalid_variable	

class multiply:												#This class will define a*=2 as a=a*2
	def check(self,inp):
		self.inp=inp
		ind=self.inp.find('*=')								#checking if there is any "*=" in the input
		str1=self.inp[:ind]
		str2=self.inp[ind+2:]

		while str1[-1] is " ":								#removing spaces
			str1=str1[:-1]
		while str2[0] is " ":
			str2=str2[1:]

		if str1 in var_names.keys():
			a=preparing_arithmetic()
			self.inp=a.insert_spaces(str1+'*'+str2)			#Now an arthimatic expression will be created with spaces required

		

			errors(self.inp)
			a=variable_names()								#checking for errors in variable names
			self.command=a.names(self.inp)
			a=solving()
			var_names[str1]=a.postfix(self.inp)				# passing newly constucted string to postfix expression
		else:
			raise invalid_variable	

class divide:												#This class will define a/=2 as a=a/2
	def check(self,inp):
		self.inp=inp
		ind=self.inp.find('/=')								#checking if there is any "/=" in the input
		str1=self.inp[:ind]
		str2=self.inp[ind+2:]

		while str1[-1] is " ":								#removing spaces
			str1=str1[:-1]
		while str2[0] is " ":
			str2=str2[1:]

		if str1 in var_names.keys():
			a=preparing_arithmetic()
			self.inp=a.insert_spaces(str1+'/'+str2)			#Now an arthimatic expression will be created with spaces required


			errors(self.inp)
			a=variable_names()								#checking for errors in variable names
			self.command=a.names(self.inp)
			a=solving()
			var_names[str1]=a.postfix(self.inp)				# passing newly constucted sting to postfix expression
		else:
			raise invalid_variable	

class var:
	def check(self,inp):
		self.inp=inp
		while self.inp[-1] is " ":
			self.inp=self.inp[:-1]
		if self.inp in var_names.keys():
			return var_names[self.inp]
		else:
			raise invalid_variable
