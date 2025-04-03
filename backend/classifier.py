# backend/classifier.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load training data
data = pd.read_csv('../data/faqs.csv')

# Encode labels
le = LabelEncoder()
data['category_encoded'] = le.fit_transform(data['category'])

# Features and labels
X = data['question']
y = data['category_encoded']

# Vectorize text
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_vec, y)

# Train KNN
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_vec, y)

# Save models
joblib.dump(dt_model, 'dt_model.pkl')
joblib.dump(knn_model, 'knn_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(le, 'label_encoder.pkl')

def classify_question(question):
    vec = vectorizer.transform([question])
    dt_pred = dt_model.predict(vec)
    knn_pred = knn_model.predict(vec)
    return {
        'decision_tree': le.inverse_transform(dt_pred)[0],
        'knn': le.inverse_transform(knn_pred)[0]
    }
