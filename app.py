from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def light_grid():
    items = [
            {'class':'sabnzbd', 'img':'assets/sabnzbd.png', 'div':'sabdiv', 'url':'https://home.holderness.io:10091'},
            {'class':'plexlogo', 'img':'assets/plex.png', 'div':'pldiv', 'url':'http://home.holderness.io:32400/web'},
            {'class':'sickbeard', 'img':'assets/sickbeard.png', 'div':'sbdiv', 'url':'https://home.holderness.io:10081'},
            {'class':'milight', 'img':'assets/light.png', 'div':'lidiv', 'url':'http://home.holderness.io:8000'} 
            ];
    return render_template('index.html', items=items)

@app.route('/light', methods=['POST'])
def light():
	print(request.data)
	return "Test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

