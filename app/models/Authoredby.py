from system.core.model import Model

class Authoredby(Model):
	def __init__(self):
		super(Authoredby, self).__init__()

	def create(self, post_data):
		book_id = post_data['b_id']
		author_id = post_data['a_id']
		if len(name >0)
			query = "INSERT INTO books_has_authors(author_id, book_id, created_at, updated_at) VALUES(%s, %s, now(), now())"
			#pass variable to prevent sql injection
				self.db.query_db(query, (author_id), (book_id))

	def delete(self, post_data):
		authoredby_id = post_data
		query = "DELETE from books_has_authors where id = %s"
		self.db.query_db(query, authored_by)