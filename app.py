from flask import Flask, render_template, request
from model import calculate_cvd_score

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve input values from the form
    age = int(request.form['age'])
    gender = request.form['gender']
    b_AF = int(request.form.get('b_AF', 0))
    b_atypicalantipsy = int(request.form.get('b_atypicalantipsy', 0))
    b_corticosteroids = int(request.form.get('b_corticosteroids', 0))
    b_impotence2 = int(request.form.get('b_impotence2', 0))
    b_migraine = int(request.form.get('b_migraine', 0))
    b_ra = int(request.form.get('b_ra', 0))
    b_renal = int(request.form.get('b_renal', 0))
    b_semi = int(request.form.get('b_semi', 0))
    b_sle = int(request.form.get('b_sle', 0))
    b_treatedhyp = int(request.form.get('b_treatedhyp', 0))
    b_type1 = int(request.form.get('b_type1', 0))
    b_type2 = int(request.form.get('b_type2', 0))
    bmi = float(request.form['bmi'])
    fh_cvd = int(request.form.get('fh_cvd', 0))
    rati = float(request.form['rati'])
    sbp = float(request.form['sbp'])
    sbps5 = float(request.form['sbps5'])
    smoke_cat = int(request.form['smoke_cat'])

    # Call the CVD risk calculation function
    result = calculate_cvd_score(age, gender, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, fh_cvd, rati, sbp, sbps5, smoke_cat)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)