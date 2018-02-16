from MyExceptions import *
from math import *

PI=3.14159
pi=3.14159
e=2.71828

class preparing_arithmetic:

	
# This inset function will take the string from user and removes spaces in the sring
	def insert_spaces(self,inp):
		op=['+','-','/','*','^','%']
		s = ''
		self.inp=inp
		self.inp=self.inp.replace(" ","")

		#trigo
		self.inp=self.trigo(self.inp)
		a=self.inp
		a=a.replace('e-','')
		a=a.replace('e+','')
		if a[0]==" ":
		 a=a[1:]
		a=a.replace('.','')

		if a.isdigit():
			return self.inp
#consecutive 2 '-'
		self.inp=self.inp.replace("--","+")				#if '--' is present then replacing it by '+'

		self.inp=self.inp.replace("++","+")				#if '++' is present then replacing it by '+' 
		
		self.inp=self.inp.replace("*+","*")				#if '*+' is present then replacing it by '*'
		
		self.inp=self.inp.replace("/+","/")				#if '/+' is present then replacing it by '/'
		
		self.inp=self.inp.replace("-+","-")				#if '-+' is present then replacing it by '-'	
		
		self.inp=self.inp.replace("^+","^")				#if '^+' is present then replacing it by '^'
		
		self.inp=self.inp.replace("%+","%")				#if '%+' is present then replacing it by '%'
		
#This is to convert the given raw input to list creating spaces where ever required (i.e.,where we wanted to split the input it would be before and after any operator except whe there is uninary '-' operator)
		for ch in self.inp:
			if ch in op:
		   		s = s + ' ' + ch + ' ' #If there is any operator creating space befor and after it so that it will split accordingly
			elif ch=='(':
				s = s + ch + ' ' #If there is '(' craeting space after it as the before elemt is an operator and space after it is created alredy
			elif ch==')':
				s = s + ' ' + ch 
			else:
				s = s + ch
		self.inp=s.split()
		self.negation()
		return self.inp
#This negation function is defined to avoid splitting of '-' and number when ever we use '-' as a uninary opereator .
	def negation(self):
		op=['+','-','/','*','^','%']
		count=0
		for i in range (0,len(self.inp)):
			if self.inp[i]=='-':
				if self.inp[i-1] in op or self.inp[i-1]=='(':
	        	 		count= count+1 #counting number of uninary '-' operators 
		k=0
		for i in range(0,len(self.inp)):
			if(k<count):
				if self.inp[i]=='-' and i!=0:
					if self.inp[i-1]=='(' or self.inp[i-1] in op:
						self.inp[i]+=self.inp[i+1] #Making the '-'sign and a number as a negative number
			   			del self.inp[i+1]
						k=k+1
					
#This trigo function will search for any trignometric or logarithmic functions in the input and replaces it by its value using eval (inbuilt function)
	def trigo(self,inp):
		funcs=['sin','cos','tan','log']
		k=0
		l=0
		m=0
		j=0
		r=0
		p=0
		for r in range(0,len(inp)-3):# checking number of trignometric or logarithmic functions 
				if inp[r]+inp[r+1]+inp[r+2] in funcs:
					p=p+1				
		for i in range (0,p):
			for k in range(0,len(inp)-3):
				for ch in inp:
					if k<len(inp)-3:
						if inp[k]+inp[k+1]+inp[k+2] in funcs: #this is to check if there is any trignometric (sin,cos,tan) or logarithmic finction in the input
							for i in range (k+3,len(inp)):
								if inp[i] == '(': 
									l=l+1
								if inp[i] == ')' :
									m=m+1
								if l==m :#to check till where the trignometric or logarithmic function is to be operated 
									a=inp[k:i+1]
								
									a=a.replace("^","**")
									
									inp=inp.replace(inp[k:i+1],str(eval(a))) #This is replacing the trignometric or logarithmic function with its value
									break
		return inp	



#This class will raise errors if any in the given input the errors are defined in an another module MyExceptions 
class errors:

	def __init__(self,inp):
		op=['+','-','/','*','^','%']
		oper=['+','/','*','^','%']

		a=len(inp)
		count=0
		num=0
# If user forgets giving last number then last would be an operator or if he forgets giving number at start 
		if inp[a-1] in op:
		 	raise last_is_operator
		if inp[0] in oper:
		 	raise first_is_operator
#If there are errors in giving brackets like no of "(" many not be equal th no of ")"
		l1=[]
		k=-1
		for i in range(0,len(inp)):
			if inp[i]=='(':
			  	l1.append(inp[i])#Appending a braket if a pair is not found
			  	k=k+1
			elif inp[i]==')':
			  	if i==0:
			   		l1.append(inp[i])
			   		k=k+1
			  	if k>=0:
			   		if l1[k]=='(':
			   			l1.pop()#We are popping out the brackets when it finds a pair of it 
			   			k=k-1
			  	else:
			   		l1.append(inp[i])#Appending a braket if a pair is not found
			   		k=k+1
 #If there are no brackets in the list It means that all brackets have found pair of all brackets that means there is no error else we are raising an error 		
		if len(l1)==0:
			 pass
		else:
			 raise invalid_brackets
#If there is any opertor just after "(" or just before ")" we are raising an error
		for i in range(0,len(inp)):
		 	if inp[i] in oper:
		   		if inp[i-1] in oper:
		   			raise operator_side_by_side
			   	elif inp[i-1]== '(':
			   		raise operator_side_by_side
			   	elif inp[i+1]==')':
			   		raise operator_side_by_side
		for i in range (0,len(inp)-1):
			if inp[i]=='-':
				if inp[i+1]==')':
					raise operator_side_by_side


#This class is for solving the expression given 
class solving:
#This postfix function is going to change an infix expression to postfix expression by using priorites of the operators (BODMAS rule) so that we could solve the given expression
	def postfix(self,inp):
		operatorlist=['+','-','/','*','^','(',')','%']
		d={'(':0,'+':1,'-':2,'%':3,'*':4,'/':5,'^':6,')':0}#Giving priorities to the operators 
		endlist=[]#In which the postfix expression will be stored
		intermediatelist=[]#In which we append operators temporarily
		self.inp=inp
		for i in self.inp:
			if i not in operatorlist:
				endlist.append(i)#appending all the operands in the end list in order
			else:
				if intermediatelist==[]:
					intermediatelist.append(i) 
				else:
					if d[intermediatelist[len(intermediatelist)-1]]<d[i] or i=='(': #Appending operators in intermediate list if the coming operator is more prior than the last element in intermediate list
						intermediatelist.append(i)
					else:
						if i==')': # If there are brackets it is like building a wall and appending operators again follow the above rule and once we get its pair bracket we will shift all to the end list
							for j in intermediatelist[::-1]:
								if (j=='('):
									break
								else:
									if(j!='(' and j!=')'):
										endlist.append(j)
								intermediatelist.pop()
							intermediatelist.pop()
						else:
							for j in intermediatelist[::-1]:
								if d[j]>d[i] and j!='(' and j!=')':
									endlist.append(j)
									intermediatelist.pop()
								else:
									break
							intermediatelist.append(i)
 # Once we are done with whole string the elements in the intermediate list are moved to end list using stack concept
		for i in intermediatelist[::-1]:
			if i!='(' and i!=')':
				endlist.append(i)
		self.inp=endlist
		return self.final_solve()

#This final solve function will take the postfix expression and solve it
	def final_solve(self):
		operatorlist=['+','-','/','*','^','(',')','%']
		n=len(self.inp)
		l=[]
		for i in range(0,n):
			if self.inp[i] not in operatorlist: #If the postfix stack has operand it is appended into new stack
				l.append((self.inp[i]))
#If it is an operator then the 2 elements are popped and the operation is performed on 2 elements aand result is popped into the stack			
			elif self.inp[i]=="+":
				a=l.pop()
				b=l.pop()
				l.append(float(a)+float(b))
			elif self.inp[i]=="*":
				a=l.pop()
				b=l.pop()
				l.append(float(a)*float(b))
			elif self.inp[i]=="/":
				a=l.pop()
				b=l.pop()
				l.append(float(b)/float(a))
			elif self.inp[i]=="-" and len(l)>=2:
				a=l.pop()
				b=l.pop()
				l.append(float(b)-float(a))
			elif self.inp[i]=="-" and len(l)==1:
				a=l.pop()
				l.append(-float(a))
			elif self.inp[i]=="^":
				a=l.pop()
				b=l.pop()
				l.append(float(b)**float(a))
			elif self.inp[i]=="%":
				a=l.pop()
				b=l.pop()
				l.append(float(b)%float(a))
		m=l.pop()

		if float(m)<1 and float(m)>-1:
			return float(m)
		elif (float(m)/int(m))==1 :# It gives integer as an integer not as a float
			
			return int(m)
		else:
			return m 
			
			

				
