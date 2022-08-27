class library:
	login_flag = False
	def __init__(self, users, books):
		self.users = users
		self.books = books

	def register(self):
		name = input('Please enter user name')
		password =input('Please enter password')
		self.users[name] = password
		self.books[name] = 0
		print('User successfully created')

	def login(self):
		name = input('Please enter user name')
		password =input('Please enter password')
		if self.users[name] == password:
			print('Successfully logged in')
			self.login_flag = True
			self.loan(name)

	def loan(self, name):
		if self.login_flag == True:
			flag = input('loan or return a book')
			if flag == 'loan':
				print('The number of books before loan = ', self.books[name])
				self.books[name] = self.books[name] + 1
				print('The number of books after loan = ', self.books[name])

			elif flag == 'return':
				print('The number of books before loan = ', self.books[name])
				self.books[name] = self.books[name] - 1
				print('The number of books after loan = ', self.books[name])

	def main(self):
	
		while 1:
			flag = input('login / register / exit')
			if flag == 'login':
				self.login()
			elif flag == 'register':
				self.register()
			elif flag == 'exit':
				break




books = {}
users = {}
l = library(users, books)
l.main()