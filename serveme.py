from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
       return render_template('about.html')

@app.route('/projects')
def projects():
       return render_template('projects.html')

@app.route('/gallery')
def gallery():
       return render_template('gallery.html')

@app.route('/contacts')
def contacts():
       return render_template('contacts.html')




#--------------------start server------->
if __name__ == '__main__':
	app.run(debug=True, host= '0.0.0.0')
