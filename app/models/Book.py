from system.core.model import Model

class Book(Model):
	def __init__(self):
		super(Book, self).__init__()

	def create(self, post_data):
		title = post_data['title']
		query = "INSERT INTO books (title, created_at, updated_at) VALUES (%s, NOW(), NOW())"
		self.db.query_db(query, title)

	def show(self,post_data):
		query = "SELECT books.id AS b_id,users.id AS u_id, users_has_books.id as rev_id, users_has_books.review, users_has_books.rating, users_has_books.created_at, books.title, authors.name AS a_name,users.name AS u_name FROM books LEFT JOIN books_has_authors ON books.id = books_has_authors.book_id LEFT JOIN authors ON authors.id = books_has_authors.book_id LEFT JOIN users_has_books ON books.id = users_has_books.book_id LEFT JOIN users ON users.id = users_has_books.user_id WHERE books.id = {}".format(post_data)
		return self.db.query_db(query)

	def index_recent(self):
		query = "SELECT books.title, books.id as b_id, users.id as u_id, users_has_books.created_at, users.alias, users_has_books.rating, users_has_books.review FROM books LEFT JOIN users_has_books ON books.id = users_has_books.book_id LEFT JOIN users ON users.id = users_has_books.user_id ORDER BY users_has_books.created_at DESC LIMIT 3;"
		return self.db.query_db(query)

	def index_remaining(self):
		recent_books = self.index_recent()
		recent_book_list = []
		for book in recent_books:
			recent_book_list.append(book['b_id'])
		query = "SELECT DISTINCT(books.id), books.title FROM books JOIN users_has_books ON books.id = users_has_books.book_id WHERE NOT books.id in ("
		for book_id in recent_book_list:
			query += (str(book_id)+",")
		new_query = query[0:-1]
		new_query += ")"
		print '*' * 100
		print new_query
		return self.db.query_db(new_query)







