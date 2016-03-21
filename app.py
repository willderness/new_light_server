from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def light_grid():
    items = ["All", "Living Room", "Kitchen", "Living Room Lamp", "Front Room", "Office", "Hall", "Bedside Left", "Bedside Right", "Master"];
    return render_template('index.html', items=items)

@app.route('/light', methods=['POST'])
def light():
	print(request.data)
	return "Test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

