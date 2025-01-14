from flask import Flask, render_template, request
from run_ml import predictions

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        print(request.form["age"])
        gender = request.form["gender"]
        age = float(request.form["age"])

        model_age = 0
        model_gender = 0
        if(age >= 50 and age <= 54):
            model_age = 7
        elif(age >= 22 and age <= 24):
            model_age = 4

        if(gender == "Male"):
            model_gender = 0
        elif(gender == "Nonbinary"):
            model_gender = 1
  
        prediction = predictions(model_age,model_gender)

        output = prediction[0]

        results = ""

        if(output == 3):
            results = "https://i0.wp.com/worldscholarshipforum.com/wp-content/uploads/2020/01/how-long-does-it-take-to-get-a-masters-degree-2.jpg?fit=1300%2C1300&ssl=1"
        elif(output == 0):
            results = "https://i0.wp.com/worldscholarshipforum.com/wp-content/uploads/2020/01/how-long-does-it-take-to-get-a-masters-degree-2.jpg?fit=1300%2C1300&ssl=1"
        elif(output == 1):
            results = "https://i0.wp.com/worldscholarshipforum.com/wp-content/uploads/2020/01/how-long-does-it-take-to-get-a-masters-degree-2.jpg?fit=1300%2C1300&ssl=1"


        print(output)
        return render_template("results.html", results=results)





