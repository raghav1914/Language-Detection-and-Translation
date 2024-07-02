# Language-Detection and Translation

Introduction:
I’ve developed solution using Python to detect languages and seamlessly translate text. I used Python for efficient data processing and the implementation of powerful machine learning algorithms to analyze text patterns accurately. Using the Multinomial Naive Bayes model, I’ve achieved an impressive 95% accuracy in identifying languages and translating them into English when needed.


How It Works:
Dataset Preparation and Training:
I started with a dataset containing 22 languages, each with 1000 sentences. After handling null values, I used CountVectorizer to convert text data into a structured format suitable for machine learning. The dataset was split into training and testing sets to validate model performance.

Model Training and Integration:
Using MultinomialNB, I trained the model to classify languages accurately based on text features. The model demonstrated robust performance with high accuracy scores during testing, ensuring its reliability in real-world applications.

Real-time Language Detection and Translation:
Integration with Google Translate API enabled real-time language detection and seamless translation. Upon user input, the system dynamically identifies the language and provides instant translations into English when needed. This feature enhances user interaction by improving accessibility across language barriers.


Usage:
Type any text you want to analyze when prompted.
The program will detect the language automatically.
If the text is not in English, you can choose to translate it to English for easier understanding.
The program will then tell you the language of the text based on its prediction.
