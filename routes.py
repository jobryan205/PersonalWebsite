from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
	options = {
		'title': 'Work Experience'
	}
 	return render_template('about.html', **options)

@app.route('/skateboarder')
def skateboarder():
	options = {
		'title': 'Skateboarding'
	}
	return render_template('skateboarder.html', **options)
 
if __name__ == '__main__':
  app.run(debug=True)