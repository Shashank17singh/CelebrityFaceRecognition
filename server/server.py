from flask import Flask, request, jsonify, render_template, send_from_directory
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import util

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

util.load_saved_artifacts()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'), filename)

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(port=5000)