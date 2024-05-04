import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from joblib import dump, load

# Load dataset
df = pd.read_csv('intent_dataset.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['Intent'], test_size=0.2, random_state=42)

# Create a pipeline with TF-IDF Vectorizer and Support Vector Classifier
model = make_pipeline(TfidfVectorizer(), SVC(probability=True))

# Train the model
model.fit(X_train, y_train)

# Evaluate the model on the test set
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Function to classify intents and handle fallbacks
def classify_intent(text, model, threshold=0.7):
    # Predict the probability distribution over the classes
    probs = model.predict_proba([text])[0]
    confidence = max(probs)
    intent = model.classes_[probs.argmax()]

    # Fallback mechanism
    if confidence < threshold:
        return "NLU fallback: Intent could not be confidently determined"
    else:
        return f"Intent: {intent}, Confidence: {confidence:.2f}"

# Save the model to disk
dump(model, 'trained_intent_classifier.joblib')

# Example usage
test_text = "Hello, how are you?"
print(classify_intent(test_text, model))
