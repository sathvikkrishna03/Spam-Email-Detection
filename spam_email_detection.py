import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset from the CSV file
data = pd.read_csv('mail_data.csv')

# Step 2: Split the dataset into features (email text) and labels
X = data['Email']
y = data['Label']

# Step 3: Create a text vectorizer to convert text data into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Step 4: Split the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a Multinomial Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Step 6: Make predictions on the testing set and evaluate the model's performance
y_pred = clf.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)

# Step 7: Use the trained model for email classification
# Replace 'new_email_text' with the text of the new email you want to classify
new_email_text = "Dear Sathvik, Your order is Undelivered! image Your Slice order couldn't be delivered today due to the following reason: Reason Customer refused to receive the order However, if you still want your product(s), please give us a missed call on 011-41185504 or click the button below to reschedule your delivery: Make Reattempt Request"

# Preprocess the new email text using the same vectorizer
new_email_vector = vectorizer.transform([new_email_text])

# Use the trained model to classify the new email
prediction = clf.predict(new_email_vector)

if prediction == 1:
    print("The email is classified as SPAM.")
else:
    print("The email is classified as LEGITIMATE.")

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Step 1: Load the dataset from the CSV file
data = pd.read_csv('mail_data.csv')

# Step 2: Split the dataset into features (email text) and labels
X = data['Email']
y = data['Label']

# Create a text vectorizer to convert text data into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Train a Multinomial Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X, y)

# Save the trained model and vectorizer to disk
joblib.dump(clf, 'spam_classifier_model.joblib')
joblib.dump(vectorizer, 'email_vectorizer.joblib')

import time

# Start the timer
start_time = time.time()

# Your code to measure the execution time
# ...


import joblib

# Load the trained model and vectorizer
clf = joblib.load('spam_classifier_model.joblib')
vectorizer = joblib.load('email_vectorizer.joblib')

# Replace 'new_email_text' with the text of the new email you want to classify
new_email_text = "Dear Sathvik, Your order is Undelivered! image Your Slice order couldn't be delivered today due to the following reason: Reason Customer refused to receive the order However, if you still want your product(s), please give us a missed call on 011-41185504 or click the button below to reschedule your delivery: Make Reattempt Request"

# Preprocess the new email text using the loaded vectorizer
new_email_vector = vectorizer.transform([new_email_text])

# Use the trained model to classify the new email
prediction = clf.predict(new_email_vector)

if prediction == 1:
    print("The email is classified as SPAM.")
else:
    print("The email is classified as LEGITIMATE.")

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
time_in_microseconds = elapsed_time * 1e12
print(f"Execution time: {elapsed_time} microseconds")

