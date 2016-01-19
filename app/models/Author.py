from system.core.model import Model
import re

class Author(Model):
	def __init__(self):
		super(Author, self).__init__()

	def index(self):
		query = "SELECT name FROM authors"
		return self.db.query_db(query)

	def create(self, post_data):
		name = post_data['name']
		if len(name >0)
			query = "INSERT INTO authors (name, created_at, updated_at) VALUES ('%s', now(), now())"
			#pass variable to prevent sql injection
				self.db.query_db(query, name)