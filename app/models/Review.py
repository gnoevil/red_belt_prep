from system.core.model import Model

class Review(Model):
	def __init__(self):
		super(Review, self).__init__()

	def create(self, post_data):
		user_id = post_data['user_id']
		book_id = post_data['book_id']
		rating = post_data['rating']
		review = post_data['review']
		query = "INSERT INTO users_has_books (user_id, book_id, review, rating, created_at, updated_at) VALUES (%s, %s, %s, %s, NOW(), NOW())"
		self.db.query_db(query, (user_id, book_id, review, rating))

	def delete(self, post_data):
		query = "DELETE FROM users_has_books WHERE id = {}".format(post_data)
		self.db.query_db(query)

