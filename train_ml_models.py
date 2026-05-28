import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans
import pickle

# Dataset
data = """attendance,coding_score,aptitude_score,communication_score,projects_completed,certifications,performance_score,placement_eligible,career_domain,skill_category
95,90,88,85,5,4,92,1,Data Scientist,Advanced
88,85,82,78,4,3,86,1,Web Developer,Intermediate
75,65,70,60,2,1,68,0,Support Engineer,Beginner
92,89,91,87,6,5,94,1,AI Engineer,Advanced
70,60,58,55,1,0,61,0,Testing Engineer,Beginner
85,80,79,75,3,2,82,1,Software Developer,Intermediate
60,50,55,48,0,0,52,0,Technical Support,Beginner
98,95,93,90,7,6,97,1,Machine Learning Engineer,Advanced
78,72,75,68,2,1,74,1,Frontend Developer,Intermediate
65,58,60,52,1,0,59,0,System Administrator,Beginner
90,87,84,80,4,3,88,1,Backend Developer,Advanced
82,76,79,72,3,2,80,1,Cloud Engineer,Intermediate
68,62,57,54,1,1,60,0,QA Engineer,Beginner
94,91,89,88,5,4,93,1,Cyber Security Analyst,Advanced
72,67,64,61,2,1,69,0,Network Engineer,Beginner
87,83,81,79,4,2,85,1,Full Stack Developer,Intermediate
96,94,92,91,6,5,96,1,Data Engineer,Advanced
58,45,50,47,0,0,49,0,Help Desk Support,Beginner
84,78,76,74,3,2,81,1,Mobile App Developer,Intermediate
91,88,86,84,5,3,89,1,DevOps Engineer,Advanced"""

# Save CSV
with open("info.csv", "w") as file:
    file.write(data)

# Read CSV
df = pd.read_csv("info.csv")

# Features
X = df[['attendance',
        'coding_score',
        'aptitude_score',
        'communication_score',
        'projects_completed',
        'certifications']]

y1 = df['performance_score']

linear_model = LinearRegression()

linear_model.fit(X, y1)

y2 = df['placement_eligible']

logistic_model = LogisticRegression()

logistic_model.fit(X, y2)

y3 = df['career_domain']

svm_model = SVC()

svm_model.fit(X, y3)

cluster = KMeans(n_clusters=3, random_state=42)

cluster.fit(X)

pickle.dump(linear_model, open("linear.pkl", "wb"))

pickle.dump(logistic_model, open("logistic.pkl", "wb"))

pickle.dump(svm_model, open("svm.pkl", "wb"))

pickle.dump(cluster, open("kMeans.pkl", "wb"))

print("Models are saved successfully")