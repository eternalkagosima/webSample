from flask import Flask, render_template
from flask import request
import time
import datetime
import signal
import sys

app = Flask(__name__)


@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/calc",methods=['POST'])
def connect():
	print("calc called")
	num1 = int(request.form['num1'])
	num2 = int(request.form['num2'])
	powered=0
	try:
		powered = num1 ** num2
		print("data:",num1,num2,powered)
	except:
		pass
	return render_template('calc.html', a=num1,b=num2,c=powered)

def sigint_handler(signal,frame):
	sys.exit(0)

if __name__ == '__main__':
	signal.signal(signal.SIGINT, sigint_handler)
	app.run(host='0.0.0.0', port=5000, debug=True) 
