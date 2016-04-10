from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def light_grid():
    items = [
            {'class':'sabnzbd', 'img':'assets/sabnzbd.png', 'div':'sabdiv'},
            {'class':'plexlogo', 'img':'assets/plex.png', 'div':'pldiv'},
            {'class':'sickbeard', 'img':'assets/sickbeard.png', 'div':'sbdiv'},
            {'class':'milight', 'img':'assets/light.png', 'div':'lidiv'} 
            ];
    return render_template('index.html', items=items)

@app.route('/light', methods=['POST'])
def light():
	print(request.data)
	return "Test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

