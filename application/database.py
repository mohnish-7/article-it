from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import os


Base = declarative_base()
db = SQLAlchemy()

def update_author(new_name,new_article):

	from application.models import Author, Article, ArticleAuthor

	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLITE_DB_DIR = os.path.join(basedir,'../db_directory')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(SQLITE_DB_DIR,'testdb.sqlite3')

	engine = create_engine(SQLALCHEMY_DATABASE_URI)

	with Session(engine, autoflush=False) as session:

		session.begin()
		try:
			
			if session.query(Author).filter(Author.name == new_name).count() > 0:

				auth = session.query(Author).filter(Author.name == new_name).one()
				new_article.authors.append(auth)
				return new_article

			else:

				new_auth = Author(name=new_name)
				new_article.authors.append(new_auth)
				return new_article

		except:

			print('Error ! Something went wrong.')



def update_database(new_name,new_title,new_content):

	from application.models import Author, Article, ArticleAuthor

	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLITE_DB_DIR = os.path.join(basedir,'../db_directory')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(SQLITE_DB_DIR,'testdb.sqlite3')

	engine = create_engine(SQLALCHEMY_DATABASE_URI)

	with Session(engine, autoflush=False) as session:

		session.begin()
		try:

			if session.query(Article).filter(Article.title == new_title).filter(Article.content == new_content).count() > 0:

				new_article = session.query(Article).filter(Article.title == new_title).filter(Article.content == new_content).one()
				updated_article = update_author(new_name,new_article)

			else:

				new_article = Article(title=new_title, content=new_content)
				updated_article = update_author(new_name,new_article)
				session.add(updated_article)

		except:

			print('Something went wrong. Try Again later.')
			session.rollback()
			raise
			return False

		else:

			print('Commit successful.')
			session.commit()
			return True



