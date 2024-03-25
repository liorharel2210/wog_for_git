
from flask import Flask, render_template
from Utils_file_utils import SCORES_FILE_NAME
#from Utils_file_utils import read_score_from_file

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        score = read_score_from_file()
        return render_template('score_template.html', score=score, error=None)
    except Exception as e:
        return render_template('score_template.html', score=None, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
