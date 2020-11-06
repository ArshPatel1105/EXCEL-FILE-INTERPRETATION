from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
#enctype=multipart/form-data
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', shape=df.shape)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()