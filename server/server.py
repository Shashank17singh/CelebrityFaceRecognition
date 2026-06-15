from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# Load artifacts at module level — runs on Vercel import
util.load_saved_artifacts()

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', methods=['GET'])
def home():
    return "Celebrity Face Recognition API is running!"

if __name__ == "__main__":
    print("Starting Python Flask Server for Sports Celebrity Face Recognition")
    app.run(port=5000)
