import streamlit as st
from joblib import load
from sklearn.pipeline import Pipeline

# Load the pre-trained model
model: Pipeline = load('app/trained_intent_classifier.joblib')

def classify_intent(text, model, threshold=0.7):
    # Predict the probability distribution over the classes
    probs = model.predict_proba([text])[0]
    # Get the maximum probability and its corresponding class
    confidence = max(probs)
    intent = model.classes_[probs.argmax()]

    # Check if the confidence meets the threshold
    if confidence < threshold:
        return "NLU fallback: Intent could not be confidently determined"
    else:
        return f"Intent: {intent}, Confidence: {confidence:.2f}"

def main():
    st.title("Intent Classification App")
    st.write("""
    This app uses a machine learning model to classify user intents based on the text they provide.
    Simply enter some text below and click 'Classify' to see the predicted intent and confidence level.
    """)

    # Sidebar for settings
    st.sidebar.title("Settings")
    threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.7, 0.01)
    st.sidebar.write("Adjust the confidence threshold to classify intents.")

    # User input in the main area
    user_input = st.text_area("Enter your text here:", height=150)

    if st.button("Classify"):
        if user_input:
            # Classify the intent
            result = classify_intent(user_input, model, threshold=threshold)
            st.success(f"Classified as: {result}")
        else:
            st.error("Please enter some text to classify.")

if __name__ == "__main__":
    main()
