# Language-Detection
Language Detection

Introduction:
This project helps you identify the language of any text you input using a method called Naive Bayes classification. It's like a smart tool that can understand different languages and tell you which one your text belongs to. This could be handy if you're dealing with multilingual content or need to automatically categorize text based on language.

How It Works:

Data Gathering: We collected a bunch of text samples from 22 different languages, each containing 1000 sentences. This creates a diverse dataset that our model learns from.
Training: We taught our model how to recognize languages using a technique called Multinomial Naive Bayes. It's a simple yet effective way to classify text data.
Testing: To ensure our model is accurate, we tested it on a separate set of data that it hasn't seen before. This helps us gauge how well it can predict the language of new text.
Getting Started:

Clone the Repository: First, copy this project to your computer.
Install Dependencies: You'll need some Python libraries like pandas, numpy, scikit-learn, and googletrans. Don't worry; you can install them all at once by running pip install -r requirements.txt.
Run the Script: Open the language_detection.py file and run it. You'll be prompted to enter text, and the program will tell you which language it is.
Usage:

Type any text you want to analyze when prompted.
The program will detect the language automatically.
If the text is not in English, you can choose to translate it to English for easier understanding.
The program will then tell you the language of the text based on its prediction.
