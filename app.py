import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import json

from model import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # data = request['data']
        to_predict = request.form['data']
        print(to_predict)
        prediction, confidence = predict(to_predict)

        res = {
                'prediction':prediction,
                'confidence':confidence
                }
        return render_template('res.html', res=res)

        # return redirect(url_for('prediction', data=data))
    return render_template('index.html')

@app.route('/prediction/data')
def prediction(filename):
    #Step 1
    my_image = plt.imread(os.path.join('uploads', filename))
    #Step 2
    my_image_re = resize(my_image, (32,32,3))

    #Step 3
    with graph.as_default():
      set_session(sess)
      probabilities = model.predict(np.array( [my_image_re,] ))[0,:]
      print(probabilities)
#Step 4
      number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
      index = np.argsort(probabilities)
      predictions = {
        "class1":number_to_class[index[9]],
        "class2":number_to_class[index[8]],
        "class3":number_to_class[index[7]],
        "prob1":probabilities[index[9]],
        "prob2":probabilities[index[8]],
        "prob3":probabilities[index[7]],
      }
#Step 5
    return render_template('predict.html', predictions=predictions)





if __name__ == '__main__':
    app.run(debug=True)
