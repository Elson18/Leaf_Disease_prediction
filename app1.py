from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'result': 'No file part'}), 400  # Return 400 if no file is provided

    file = request.files['file']
    if file.filename == '':
        return jsonify({'result': 'No selected file'}), 400  # Return 400 if no file is selected

    # Here you would add code to load and preprocess the image, then run the prediction
    # prediction = model.predict(preprocessed_image)
    # For example purposes, let’s return a placeholder result
    if result==1:
        jsonify=Diseased
    else:
        jsonify=healthy

    return jsonify({'result': 'Diseased'})  # Replace with actual prediction result

if __name__ == '__main__':
    app.run(debug=True)
