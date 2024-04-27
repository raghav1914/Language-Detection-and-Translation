import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from googletrans import Translator

#Load Dataset
dataset = pd.read_csv("dataset.csv")
#print(dataset)
dataset_head = dataset.head()
print(dataset_head)

#Let’s have a look at whether this dataset contains any null values or not:
check_null_values = dataset.isnull().sum() 
print(check_null_values)

# Fill NaN values with empty strings
dataset['Text'].fillna('', inplace=True)

#Now let’s have a look at all the languages present in this dataset:
dataset_languages = dataset['language'].value_counts()
print(dataset_languages)
#This dataset contains 22 languages with 1000 sentences from each language. This is a very balanced dataset with no missing values, so we can say this dataset is completely ready to be used to train a machine learning model.

#Preprocessing
#Splitting dataset
x = np.array(dataset['Text'])
y = np.array(dataset['language'])
cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

'''x = np.array(data["Text"]): This line extracts the "Text" column from the DataFrame data and converts it into a NumPy array x.
y = np.array(data["language"]): This line extracts the "language" column from the DataFrame data and converts it into a NumPy array y.
cv = CountVectorizer(): This line initializes a CountVectorizer object cv, which is used to convert text data into a matrix of token counts.
X = cv.fit_transform(x): This line applies the fit_transform method of the CountVectorizer object cv to the text data x, converting it into a sparse matrix X where each row represents a document and each column represents a word, with the cell value indicating the frequency of the word in the corresponding document.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42): This line splits the data into training and testing sets. It takes the feature matrix X and target array y, along with the specified test size (in this case, 33% of the data will be used for testing), and a random state for reproducibility. It returns four arrays: X_train (training features), X_test (testing features), y_train (training labels), and y_test (testing labels).'''


#Train the model
model = MultinomialNB()
model.fit(X_train, y_train)
model.score(X_test, y_test)

# use this model to detect the language of a text by taking a user input



while True:
    user_input_language = input("Enter a text: ")
    if user_input_language == "":
        break

    # Detect language of user input
    detected_language = Translator().detect(user_input_language)        # Detect language of user input
    detected_language_code = detected_language.lang                     #represents the detected language (e.g., "en" for English, "fr" for French).  The language code is a short identifier, usually two or three letters, that represents a specific language. For example, "en" stands for English, "fr" for French, and "es" for Spanish. It helps programs understand and process text in different languages.
    print("Detected language is: ", detected_language_code)

    # If not English, ask for translation
    if detected_language_code != 'en':
        translate_to_english = input("Detected language is not English. Would you like to translate to English? (yes/no): ")
        if translate_to_english.lower() == 'yes':
            translated_text = Translator().translate(user_input_language, dest='en')
            print("Translated text:", translated_text.text)
            user_input_language = translated_text.text


    # Predict Language based on the original or translated text
    dataset = cv.transform([user_input_language]).toarray()
    output = model.predict(dataset)
    print(output)

'''
Unstructured multilingual structured English language - yes it takes unstructured data

Text analytics use krakte ho....like my name is raghav and all....



Pick all languages from the world and categorize.

My name is Nishtha ek category hogyi like Introduction.

Text analytics kya krega ki sentences ko category ko daaldega.


Sentimental analysis hoskta h ye.

Hilthy is good but not for me.
Ai kya krega isko ki review bad h
take image input
'''