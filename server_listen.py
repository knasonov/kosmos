from flask import Flask, request, render_template,send_from_directory, send_file
from flask_cors import cross_origin
import json
import os

app = Flask(__name__)
files1 = os.listdir('.')
print(files1)

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents


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
    param = request.args.get('param')
    if (param == "Test"):
        return "This is a test text"
    
    try:
       s = read_file(f"{param}.txt")
       return s
    except:
       print("Error")	
	
    
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
    filename = 'Girl17.jpeg'
    return send_file(filename, mimetype='image/jpg')	  

@app.route("/data.csv")
@cross_origin()
def data_csv():
      return render_template("data.csv")

@app.route("/mySite")
@cross_origin()
def mySite():
      return render_template("Site/my1.html")
	 
@app.route("/game")
@cross_origin()
def game():
      return render_template("game.html")


	 
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
