import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import json

from model import predict

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        senior_citizen = float(request.form['senior-citizen'])
        partener = int(request.form['partener'])
        dependents = int(request.form['dependents'])
        tenure = float(request.form['tenure'])
        phone_service = int(request.form['phone-service'])
        multiple_lines = int(request.form['multiple-lines'])
        internet_service = int(request.form['internet-service'])
        online_security = int(request.form['online-security'])
        online_backup = int(request.form['online-backup'])
        device_protection = int(request.form['device-protection'])
        tech_support = int(request.form['tech-support'])
        streaming_tv = int(request.form['streaming-tv'])
        streaming_movies = int(request.form['streaming-movies'])
        contract = int(request.form['contract'])
        paperless_billing = int(request.form['paperless-billing'])
        payment_method = int(request.form['payment-method'])
        monthly_charges = float(request.form['monthly-charges'])
        total_charges = float(request.form['total-charges'])

        prediction, confidence = predict(gender, senior_citizen, partener, dependents, tenure, phone_service, multiple_lines, internet_service, online_security,
                                         online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contract, paperless_billing, payment_method, monthly_charges, total_charges)

        res = {
            'prediction': prediction,
            'confidence': confidence
        }
        return render_template('res.html', res=res)

        # return redirect(url_for('index', data=data))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
