# Intent Classification App

This repository contains a Streamlit app designed to classify text inputs into predefined intents. The app utilizes a machine learning model trained on a dataset of text samples labeled with corresponding intents. It is intended for demonstration purposes, showcasing a basic NLP application using a Support Vector Classifier and TF-IDF vectorization.

## Features

- **Text Input**: Users can enter text they wish to classify.
- **Intent Classification**: The app classifies the text and displays the predicted intent.
- **Confidence Score**: Alongside the intent, a confidence score is shown, indicating the certainty of the classification.
- **Fallback Mechanism**: If the confidence score is below a certain threshold, the app provides a fallback response.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Aiaxis/Intent-Classification-App.git
cd Intent-Classification-App
  ```
2.**Create a virtual environment:**

  ```bash
  python -m venv venv
  
  ```
3.**Create a virtual environment:**

  * **Windows**
    ```bash
    .\venv\Scripts\activate
    ```
  
 *  **Mac**
    ```bash
    source venv/bin/activate
    ```

4.**Install dependencies:**

  ```bash
  pip install -r requirements.txt
  
  ```

```bash
streamlit run app.py
```

Now, the app should be running locally on your machine.
