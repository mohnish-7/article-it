from flask import Flask, render_template, request
from flask import current_app as app
from application.database import update_database
from application.models import Author,Article
# -------------------------------------------------------------------------------------------------------------------------------#

@app.route('/', methods=['GET','POST'])
def all_articles():

	articles = Article.query.all()
	articles.reverse()

	if len(articles) == 0:
		
		return render_template('empty_page.html', articles=articles)

	else:
		
		return render_template('all_articles.html', articles=articles)

# -------------------------------------------------------------------------------------------------------------------------------#

@app.route('/article_by/<author_name>', methods=['GET','POST'])
def articles_by_author(author_name):

	articles = Article.query.filter(Article.authors.any(name=author_name))


	if articles.count() == 0:
		
		return render_template('empty_page.html', articles=articles, author=author_name)

	else:
		
		return render_template('article_by_author.html', articles=articles, author=author_name)

# -------------------------------------------------------------------------------------------------------------------------------#	

@app.route('/new_post', methods=['GET','POST'])
def new_post():

		return render_template('new_post.html')

# -------------------------------------------------------------------------------------------------------------------------------#	

@app.route('/upload_post', methods=['GET','POST'])
def upload_post():

		new_name = request.form['new_name']
		new_title = request.form['new_title']
		new_content = request.form['new_content']

		success = update_database(new_name,new_title,new_content)

		if success:
			
			return render_template('upload_post_success.html')
	
		else:

			return render_template('upload_post_error.html')

# -------------------------------------------------------------------------------------------------------------------------------#

@app.route('/author_search', methods=['GET','POST'])
def author_search():

	author_name = request.form['author_name']
	return articles_by_author(author_name)

# -------------------------------------------------------------------------------------------------------------------------------#