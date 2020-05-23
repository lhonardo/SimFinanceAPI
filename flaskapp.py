from flask import Flask
from collections import Counter
app = Flask(__name__)

@app.route('/countme/<input_str>')
def count_me(input_str):
	return '<br>'.join('"{}": {}'.format(let, cnt) for let, cnt in Counter(input_str).most_common())

@app.route('/')
def hello_world():
  return 'Hello from Flask!'
if __name__ == '__main__':
  app.run()

