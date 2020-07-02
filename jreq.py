from flask import Flask, request, redirect, url_for, render_template
import json

app = Flask(__name__, template_folder='template')

@app.route("/alerts", methods = ['POST', 'GET'])
def alerts():
	if request.method == 'POST':
		req_data = request.get_json()
		metric_alert = 'alerts' in req_data
		lods_alert = 'msg' in req_data
		if metric_alert:
			metrics_alert = req_data['alerts']
			with open('template/notif.html','w') as m:
				write_content = ''
				for keys in metrics_alert:
					write_content += '<p>'
					for vals in keys:
						write_content += '<h5>'+ vals + " : " + keys[vals] + '</h5>'
					write_content+= '</p>'
				m.write(write_content)
			
			return ''
		elif lods_alert:
			with open('template/notif.html','w') as l:
				content = ''
				for logvals in req_data:
					content += '<p>'
					content += '<h5>' + logvals + ' : '+ str(req_data[logvals]) + '</h5>'
					content += '</p>'
				l.write(content)
			return ''	

	return render_template("notif.html")

		

@app.route("/")
def home():
	return '<h1>Enter Alert Data through POST<h2>'


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)