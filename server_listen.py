from flask import Flask, request, render_template,send_from_directory, send_file
from flask_cors import cross_origin
import json
import os

app = Flask(__name__)
files1 = os.listdir('.')
print(files1)

@app.route('/save', methods=['POST'])
def save_phrase():
    phrase = request.form['phrase']
    with open("phrase.txt", "w") as text_file:
        text_file.write(phrase)
    return "Phrase saved to file"

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/capitals")
@cross_origin()
def capitals():
    return render_template('Capitals.html')
	
@app.route("/another_adress")
def another():
    return "Yet another server"

@app.route("/data")
@cross_origin()
def data():
    param = request.args.get('city')
    print(param)
    try:
      print("OK!")
      return render_template(f'texts/{param}.txt')
      
    except:
      print (f"No city {param}")
      return "Nothing here"

@app.route("/scatter.html")
@cross_origin()
def scatter():
      return render_template('scatter.html')
      
@app.route("/scatter.css")
@cross_origin()
def css():
      return render_template('scatter.css')            
    
@app.route("/scatter.js")
@cross_origin()
def send_js():
      return send_from_directory('templates', 'scatter.mjs')

@app.route("/image")
def send_image():
    filename = 'image.jpg'
    return send_file(filename, mimetype='image/jpg')	  

@app.route("/data.csv")
@cross_origin()
def data_csv():
      return render_template("data.csv")
	  
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
