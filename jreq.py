from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, template_folder='template')

@app.route("/alerts", methods = ['POST', 'GET'])
def alerts():
	if request.method == 'POST':
		req_data = request.get_json()
		alert = req_data['alerts']
		with open('template/notif.html','w') as f:
			write_content = ''
			for keys in alert:
				write_content += '<p>'
				for vals in keys:
					write_content += '<h5>'+ keys[vals] + '</h5>'
				write_content+= '</p>'
			f.write(write_content)
		
		return ''

	return render_template("notif.html")

		

@app.route("/")
def home():
	return '<h1>Enter Alert Data through POST<h2>'


if __name__ == '__main__':
	app.run(debug=True)