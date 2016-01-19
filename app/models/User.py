from system.core.model import Model
import re

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def show(self, data):
		query = "SELECT users.alias, users.name, books.title, users.email, books.id, COUNT(users_has_books.id) AS counted FROM users LEFT JOIN users_has_books ON users.id = users_has_books.user_id LEFT JOIN books ON users_has_books.book_id = books.id WHERE users.id = {}".format(data)
		return self.db.query_db(query)

	def show_by_email(self, post_data):
		#post_data is just the string that was in the email palce of our data
		print '*' * 100
		print post_data
		if len(post_data) > 0:
			query = "SELECT * FROM users WHERE email = '{}'".format(post_data)
			return self.db.query_db(query)
		return {'error':'no email'}

	def create(self,post_data):
		#for proper login registration call is_valid
		query = "INSERT INTO users (name, alias, email, password, created_at, updated_at) VALUES (%s, %s, %s,%s,NOW(), NOW())"
		self.db.query_db(query, (post_data['name'], post_data['alias'], post_data['email'], post_data['password']))
		return self.show_by_email(post_data['email'])


	def login(self, post_data):
		possible_user = self.show_by_email(post_data['email'])
		if post_data['password'] == possible_user['email']:
			return possible_user
		return False

	def is_valid(self, post_data):
		#build validation here!

		has_email = self.show_by_email(post_data['email'])
		#has_email, error, null has_email
		errors = {}
		try:
			has_email
		except:
			try:
				has_email['error']
				errors['email'] = 'Please enter an email address'
			except:
				return False
		return True