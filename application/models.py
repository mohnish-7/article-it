from application.database import db

class Author(db.Model):

	__tablename__ = 'author'
	author_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String, unique=True, nullable=False)

class Article(db.Model):

	__tablename__ = 'article'
	article_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String, nullable=False)
	content = db.Column(db.String, nullable=False)
	authors = db.relationship('Author', secondary='article_author')

class ArticleAuthor(db.Model):

	__tablename__ = 'article_author'
	author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'), primary_key=True, nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'), primary_key=True, nullable=False)