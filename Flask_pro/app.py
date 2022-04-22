from flask import Flask, render_template,url_for, request
import flask_sqlalchemy
from sklearn.externals import joblib
import numpy as np
app = Flask(__name__)

@app.route('/')

def home():
	return render_template('recommend.html')

@app.route('/prediction', methods = ['POST'])
def prediction():
	if request.method == 'POST':
		movie = request.form['movie']
		
	try:
		movie = str(movie)
		x_app = np.array([[movie]])
		model = joblib.load('nlp_model.pkl')
		ans = model.predict(x_app)
		if (ans==1):
			print("Congratulations your eligble for this Loan")
		else:
			print("We sad to inform that your request has not been accepted")
		return render_template('shit.html', prediction=ans)
	except ValueError:
		return render_template('error.html', prediction=1)
	

if __name__ == '__main__':
	app.run(debug=True)