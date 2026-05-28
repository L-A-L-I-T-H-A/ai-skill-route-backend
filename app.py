#import the libraries
from flask import Flask,request,jsonify
import pickle
# create flask application
app = Flask(__name__)
#load the training model
linear_model = pickle.load(open("linear.pkl","rb"))
logistic_model = pickle.load(open("logistic.pkl","rb"))
svm_model = pickle.load(open("svm.pkl","rb"))
kMeans_model = pickle.load(open("kMeans.pkl","rb"))

# create the api route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    attendance = float(data['attendance'])
    coding = float(data['coding'])
    aptitude = float(data['aptitude'])
    communication = float(data['communication'])
    projects = float(data['projects'])
    certifications = float(data['certifications'])
        
    input_data = [[
        attendance,
        coding,
        aptitude,
        communication,
        projects,
        certifications
        ]]
    performance = linear_model.predict(input_data)[0]
    placement = logistic_model.predict(input_data)[0]
    career = svm_model.predict(input_data)[0]
    cluster_result = kMeans_model.predict(input_data)[0]

    if cluster_result == 0:
        skill = "Beginner"
    elif cluster_result ==1:
        skill = "Intermediate"  
    else :
        skill = "Advanced"

    return jsonify({
        "performance_score": round(float(performance),2),
        "placement_eligible": int(placement),
        "career_domain": career,
        "skill_category": skill
        })  
if __name__ == "__main__":
    app.run(debug=True)





