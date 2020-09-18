from flask import Flask, request, jsonify, render_template,session, jsonify
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/getimage', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)
