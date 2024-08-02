from flask import Flask, render_template, request
import subprocess
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/run_script1', methods=['POST'])
def run_script1():
    try:
        result = subprocess.check_output(['python', 'E:\\BTECH\\sem-3\\dmgt-sem3\\project dmgt sem3\\Traffic1\\Traffic\\Code\\YOLO\\darkflow\\simulation.py'], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
@app.route('/run_script2', methods=['POST'])
def run_script2():
    try:
        result = subprocess.check_output(['python', 'E:\\BTECH\\sem-3\\dmgt-sem3\\project dmgt sem3\\Traffic1\\Accident\\Code\\YOLO\\darkflow\\simulation.py'], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
@app.route('/run_script3', methods=['POST'])
def run_script3():
    try:
        result = subprocess.check_output(['python', 'E:\\BTECH\\sem-3\\dmgt-sem3\\project dmgt sem3\\Traffic1\\Lane\\Code\\YOLO\\darkflow\\simulation.py'], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
if __name__ == '__main__':
    app.run(debug=True)
