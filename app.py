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

        # return redirect(url_for('prediction', data=data))
    return render_template('index.html')


@app.route('/prediction/data')
def prediction(filename):
    # Step 1
    my_image = plt.imread(os.path.join('uploads', filename))
    # Step 2
    my_image_re = resize(my_image, (32, 32, 3))

    # Step 3
    with graph.as_default():
        set_session(sess)
        probabilities = model.predict(np.array([my_image_re, ]))[0, :]
        print(probabilities)
# Step 4
        number_to_class = ['airplane', 'automobile', 'bird',
                           'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        index = np.argsort(probabilities)
        predictions = {
            "class1": number_to_class[index[9]],
            "class2": number_to_class[index[8]],
            "class3": number_to_class[index[7]],
            "prob1": probabilities[index[9]],
            "prob2": probabilities[index[8]],
            "prob3": probabilities[index[7]],
        }
# Step 5
    return render_template('predict.html', predictions=predictions)


if __name__ == '__main__':
    app.run(debug=True)
