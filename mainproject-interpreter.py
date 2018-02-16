from Tkinter import *
from MyExceptions import *
from Value_Assigning import *
from arith import *
from bool0 import *

PI=3.14159  #These are global variables which can be used while giving input
pi=3.14159
e=2.71828

class GUI:

	def __init__(self,parent):

		self.ptr=0				#pointer pointing to given command
		self.length=0			#intially length of command list is zero 
		self.commandlist=[]		#empty list

		self.commandlist.append('exit()')
		self.length+=1			#length increases when commands are given and pointer points to last command
		self.ptr=self.length 	#pointer points to last added command
		#base frame on which all frames are placed
		self.base=Frame(root,height=700,width=1430)
		#frame1- having text and scrollbar
		self.frame1=Frame(self.base)
		#frame2- having entry
		self.frame2=Frame(self.base)
		#frame3- having canvas
		self.frame3=Frame(self.base)

		self.base.pack(expand=YES,fill=BOTH)
		self.frame2.pack(expand=YES ,fill=BOTH)
		self.frame1.pack(expand=YES ,fill=BOTH)
		self.frame3.pack(expand=YES ,fill=BOTH)
		
		#placing the frames on the root window
		self.frame1.place(height=660,width=430,x=1000,y=0)
		self.frame2.place(height=40,width=430,y=660,x=1000)
		self.frame3.place(height=700,width=1000,y=0,x=0)

		self.makewidgets()			
	
	def makewidgets(self):

		self.text=Text(self.frame1)
		self.sbar=Scrollbar(self.frame1)		#scroll bar :To move screen up or down 
		self.entry=Entry(self.frame2)
		
		#will bring the cursor to the entry
		self.entry.focus()

		self.sbar.config(command=self.text.yview)
		self.text.config(yscrollcommand=self.sbar.set , bg='#384e67' , borderwidth=5 , font=('times',15,'normal'), fg='white',highlightbackground='black', relief='sunken')
		self.entry.config( font=('times',15,'normal') , relief='sunken' , borderwidth=5 , bg='#5e6b6a' , highlightbackground=  'black', fg='white')

		self.entry.bind('<Return>',self.takeentry)	
		self.entry.bind('<Up>',self.moveup)
		self.entry.bind('<Down>',self.movedown)

		self.entry.pack(expand=YES,fill=BOTH)
		self.sbar.pack(side=RIGHT,fill=Y)
		self.text.pack(side=LEFT,expand=YES,fill=BOTH)

		self.canvas=Canvas(self.frame3, height=700,width=1000)
		self.canvas.config(bg='white',relief='sunken',borderwidth=5,highlightbackground='black')
		self.canvas.pack(expand=YES,fill=BOTH)


		self.canvas.bind('<Motion>',self.move)
		self.canvas.bind('<Double-1>',self.coordinates_print)
		self.canvas.bind('<Enter>',self.graph_enter)
		self.canvas.bind('<B1-Motion>',self.draw)

		self.graph_intialise()

		
	
	def takeentry(self,event):
		
		self.command=self.entry.get()				#takes command from user		
		self.commandlist.append(self.command)		#appends command to list
		self.length+=1								#increases list length by 1
		self.ptr=self.length 						#pointer points to given command

		self.entry.delete(0,END)					#after we press enter it clears all input given
		self.sendtotext()							#sends commands to function


	def sendtotext(self):
		
		self.text.insert(END,'\n'+'>>> '+self.command)	#curses will be at end of input so from there we go to next line and paste command there

		self.text.see(END)
		

		self.analysecommand()


	def output(self,text):
		self.text.insert(END,'\n'+'  '+text)		#displays output of command

	def movedown(self,event):
		self.entry.delete(0,END)
		if self.ptr==self.length:			#if pointer is at last command then we point pointer to first command and display it while using down arrow  
			self.ptr=0
			self.entry.insert(0,self.commandlist[self.ptr])
		elif self.ptr==self.length-1:		
			self.ptr=0
			self.entry.insert(0,self.commandlist[self.ptr])
		else:
			self.ptr+=1						#if we pointer is not at last two places then we increase pointer and displays that  command
			self.entry.insert(0,self.commandlist[self.ptr])

	def moveup(self,event):
		self.entry.delete(0,END)
		if self.ptr==0:									#if pointer is at first command then we show commands which were given last and decrease pointer to display previous one of that command
			self.ptr=self.length-1
			self.entry.insert(0,self.commandlist[self.ptr])
		else:
			self.ptr-=1									#generally displays previous command				
			self.entry.insert(0,self.commandlist[self.ptr])


	def analysecommand(self):
		op=['+','-','/','*','^','%']
		if self.command=='exit()':						#if user gives exit() then console closes
			sys.exit()
		else:
			#checks if plotting has to be donw
			if self.command[:7]=='plot y=':
				self.command=self.command[7:]
				self.plot_graph()

			#for clearing the graph
			elif self.command =='clear graph':
				self.canvas.delete('all')
				self.graph_intialise()

			#for grid
			elif self.command =='draw grid':
				self.draw_grid()

			elif self.command.count('+=') is 1:			#verifying whether += is in command if there then we increase it by increment function
				try:
					a=increment()
					y=a.check(self.command)				#verifying command if variable is in var_names  
				except invalid_variable as X:			#prints error in given command
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")


			elif self.command.count('-=') is 1:			#verifying whether -= is in command if there then we increase it by decrement function
				try:
					a=decrement()
					a.check(self.command)				#verifying command if variable is in var_names
				except invalid_variable as X:			#prints error in given command
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			elif self.command.count('*=') is 1:			#verifying whether *= is in command if there then we increase it by multiply function
				try:
					a=multiply()
					a.check(self.command)				#verifying command if variable is in var_names
				except invalid_variable as X:			#prints error in given command
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			elif self.command.count('/=') is 1:			#verifying whether /= is in command if there then we increase it by divide function
				try:
					a=divide()
					a.check(self.command)				#verifying command if variable is in var_names
				except invalid_variable as X:			#prints error in given command
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			elif self.command.count('=') is 1 :			#assigning value to variable 	
				a=Value_Assigning()								
				self.output(a.defining_var(self.command))

			elif self.command.count('==') is 1:			#checking value of given variable equals given value or not
				try:
					a=bool()
					self.output(str(a.check(self.command)))
				except invalid_variable as X:
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			elif self.command =='clear all':			#if user gives clear all as command then it displays an empty screen 
				self.text.delete('1.0',END)

			
			else:
				
				a=preparing_arithmetic()
				self.command=a.insert_spaces(self.command)
			
				a=str(self.command)
				a=a.replace('e-','')				#if there is 'e-' in command remove  'e-' from command 
				a=a.replace('e+','')				#if there is 'e-' in command remove  'e+' from command
				a=a[1:]
				a=a.replace('.','')					#if there is '.' in command remove  '.' from command
				if a.isdigit():						#check whether it is a digit or not
					self.output(self.command)
				else:
				
					try:
						errors(self.command)		#check if there are any errors in it
						a=variable_names()			#this replaces variable to its value and used in solving command
						self.command=a.names(self.command)
						a=solving()
						self.output(str(a.postfix(self.command)))
						

					except (last_is_operator,first_is_operator,invalid_brackets,operator_side_by_side,invalid_variable) as X:		#if there are any errors prints which type error is it
						self.output(X.message())
					except Exception:
						self.output("INVALID SYNTAX")
		self.text.see(END)

	def graph_intialise(self):
		self.z=50 	#refer to the scale
		#drawing the axis
		self.canvas.create_line(0,350,1000,350,width=2)
		self.canvas.create_line(500.0,0,500.0,700,width=2)
		#pltting numbers on the axis
		#on x axis
		y=1
		for x in range(500+self.z,1000,self.z):
			self.canvas.create_text(x,358,text=y)
			y+=1
		# plotting the origin
		self.canvas.create_text(508,358,text=0)	
		#on -x axis
		y=1
		for x in range(500-self.z,0,-self.z):
			self.canvas.create_text(x,358,text=-y)
			y+=1
		#on y axis
		y=1
		for x in range(350-self.z,0,-self.z):
			self.canvas.create_text(508,x,text=y)
			y+=1
		#on -y axis	
		y=1
		for x in range(350+self.z,700,self.z):
			self.canvas.create_text(508,x,text=-y)
			y+=1	

	def plot_graph(self):
		
		x=0
		y=0
		px=0
		py=0
		#plotting on x axis
		while(x<500/self.z):

			#throwing values of x into the function
			inp=self.command
			inp=inp.replace('x',str(x))
			a=preparing_arithmetic()
			inp=a.insert_spaces(inp)
		
			a=str(inp)
			a=a.replace('e-','')				#if there is 'e-' in command remove  'e-' from command 
			a=a.replace('e+','')				#if there is 'e-' in command remove  'e+' from command
			a=a[1:]
			a=a.replace('.','')					#if there is '.' in command remove  '.' from command
			if a.isdigit():						#check whether it is a digit or not
				pass
			else:
			
				try:
					errors(self.command)		#check if there are any errors in it
					a=variable_names()			#this replaces variable to its value and used in solving command
					inp=a.names(inp)
					a=solving()
					inp=a.postfix(inp)
					

				except (last_is_operator,first_is_operator,invalid_brackets,operator_side_by_side,invalid_variable) as X:		#if there are any errors prints which type error is it
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			a=float(inp)
			y=self.z*a

			#plotting a dot at each coordinate
			self.canvas.create_oval((x*self.z+500.0),350-y-1,(x*self.z+500.0)+1,350-y)
			nx=x
			ny=y
			#drawing a line in the previous dot and the new dot
			self.canvas.create_line((px*self.z+500.0),350-py-1,(nx*self.z+500.0)+1,350-ny)
			px=nx
			py=ny
			
			x+=1/float(self.z)
			
			inp=self.command
			inp=inp.replace('x',str(x))
			a=preparing_arithmetic()
			inp=a.insert_spaces(inp)
		
			a=str(inp)
			a=a.replace('e-','')				#if there is 'e-' in command remove  'e-' from command 
			a=a.replace('e+','')				#if there is 'e-' in command remove  'e+' from command
			a=a[1:]
			a=a.replace('.','')					#if there is '.' in command remove  '.' from command
			if a.isdigit():						#check whether it is a digit or not
				pass
			else:
			
				try:
					errors(self.command)		#check if there are any errors in it
					a=variable_names()			#this replaces variable to its value and used in solving command
					inp=a.names(inp)
					a=solving()
					inp=a.postfix(inp)
					

				except (last_is_operator,first_is_operator,invalid_brackets,operator_side_by_side,invalid_variable) as X:		#if there are any errors prints which type error is it
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			a=float(inp)		
			y=self.z*a
			self.canvas.create_oval((x*self.z+500.0),350-y-1,(x*self.z+500.0)+1,350-y)
			nx=x
			ny=y
			
			x+=1/float(self.z)
			self.canvas.create_line((px*self.z+500.0),350-py-1,(nx*self.z+500.0)+1,350-ny)
			px=nx
			py=ny

		#plotting on y axis
		x=0
		y=0
		px=0
		py=0
		while(x>-500/self.z):

			inp=self.command
			inp=inp.replace('x',str(x))
			a=preparing_arithmetic()
			inp=a.insert_spaces(inp)
		
			a=str(inp)
			a=a.replace('e-','')				#if there is 'e-' in command remove  'e-' from command 
			a=a.replace('e+','')				#if there is 'e-' in command remove  'e+' from command
			a=a[1:]
			a=a.replace('.','')					#if there is '.' in command remove  '.' from command
			if a.isdigit():						#check whether it is a digit or not
				pass
			else:
			
				try:
					errors(self.command)		#check if there are any errors in it
					a=variable_names()			#this replaces variable to its value and used in solving command
					inp=a.names(inp)
					a=solving()
					inp=a.postfix(inp)
					

				except (last_is_operator,first_is_operator,invalid_brackets,operator_side_by_side,invalid_variable) as X:		#if there are any errors prints which type error is it
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			a=float(inp)
			y=self.z*a
			self.canvas.create_oval((x*self.z+500.0),350-y-1,(x*self.z+500.0)+1,350-y)
			nx=x
			ny=y
			self.canvas.create_line((px*self.z+500.0),350-py-1,(nx*self.z+500.0)+1,350-ny)
			px=nx
			py=ny
			
			x-=1/float(self.z)
			
			inp=self.command
			inp=inp.replace('x',str(x))
			a=preparing_arithmetic()
			inp=a.insert_spaces(inp)
		
			a=str(inp)
			a=a.replace('e-','')				#if there is 'e-' in command remove  'e-' from command 
			a=a.replace('e+','')				#if there is 'e-' in command remove  'e+' from command
			a=a[1:]
			a=a.replace('.','')					#if there is '.' in command remove  '.' from command
			if a.isdigit():						#check whether it is a digit or not
				pass
			else:
			
				try:
					errors(self.command)		#check if there are any errors in it
					a=variable_names()			#this replaces variable to its value and used in solving command
					inp=a.names(inp)
					a=solving()
					inp=a.postfix(inp)
					

				except (last_is_operator,first_is_operator,invalid_brackets,operator_side_by_side,invalid_variable) as X:		#if there are any errors prints which type error is it
					self.output(X.message())
				except Exception:
					self.output("INVALID SYNTAX")

			a=float(inp)
			y=self.z*a
			self.canvas.create_oval((x*self.z+500.0),350-y-1,(x*self.z+500.0)+1,350-y)
			nx=x
			ny=y
			
			x-=1/float(self.z)
			self.canvas.create_line((px*self.z+500.0),350-py-1,(nx*self.z+500.0)+1,350-ny)
			px=nx
			py=ny

	#hover the mouse over the canvas and prints the coordinates at the top 
	def move(self,event):
		s='x: ' +str((event.x-500)/float(self.z)) + ', y : '+str((350-event.y)/float(self.z))
		l=Label(self.canvas,text=s,height=2,width=20)
		l.place(x=800,y=20)

	#double click to print the coordiante on the text screen		
	def coordinates_print(self,event):
		s='( ' +str((event.x-500)/float(self.z)) + ' , '+str((350-event.y)/float(self.z))+' )'
		self.output(s)
		self.text.see(END)


	#draws the grid for user convenience
	def draw_grid(self):

		for x in range(500+self.z,1000,self.z):
			self.canvas.create_line(x,0,x,700)
		for x in range(500-self.z,0,-self.z):
			self.canvas.create_line(x,0,x,700)
		for x in range(350-self.z,0,-self.z):
			self.canvas.create_line(0,x,1000,x)
		for x in range(350+self.z,700,self.z):
			self.canvas.create_line(0,x,1000,x)

	#whenver the mouse is hovered over the canvas its cursor changes to a cross
	def graph_enter(self,event):
		self.canvas.config(cursor='cross')


	#for drawing over the canvas or highlighting the canvas
	def draw(self,event):
		self.canvas.create_oval(event.x,event.y-5,event.x+5,event.y,fill='red',outline='')



		
		




root=Tk()
screen=GUI(root)
root.title('Interpreter')
root.mainloop()

