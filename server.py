from flask import Flask, render_template, redirect, request, session, flash

secret_key = open('secret-key.txt', 'r').read().strip()

app = Flask(__name__)
app.secret_key = secret_key

params = {
	'dc': 'Washington D.C.',
	'sj': 'San Jose',
	'chi': 'Chicago',
	'py': 'Python',
	'sql': 'SQL',
	'js': 'JavaScript'
}
params.setdefault('','')

@app.route('/')
def index():	
	return render_template('index.html', **params)


@app.route('/process', methods=['POST'])
def process():
	name = request.form.get('name','')
	comment = request.form.get('comment','')
	errors = 0
	if len(name)==0:
		flash('Name field is required')
		errors += 1
	if len(comment)==0:
		flash('Comment field is required')
		errors += 1
	elif len(comment) > 120:
		flash('Comment should not be longer than 120 characters')
		errors += 1
		
	if errors > 0:
		return redirect('/')
	else:
		session.update(dict(list(request.form.items())))
		return redirect('/result')


@app.route('/result')
def result():
	vals = {
		'name': session.get('name', ''),
		'location': params[session.get('location', '')],
		'lang': params[session.get('lang','')],
		'comment': session.get('comment','')
	}

	if vals['lang']:
		vals['lang'] += '!!!'
	
	return render_template('result.html', **vals)


app.run(debug=True)