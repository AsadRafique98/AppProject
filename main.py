import random
import sys
from GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
# vader library to calculate sentiments
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import string
import re
# google translator package import
from googletrans import Translator

#function use to convert into english
def convert_to_english(text):
    translator = Translator()

    translated_text = translator.translate(text)
    return translated_text.text

#function use to clean the data
def text_cleaning(text):
    from nltk.corpus import stopwords
    punctuation = string.punctuation
    stopwords = stopwords.words('english')
    text = convert_to_english(text)
    text = text.lower()
    text = re.sub('www.[^\s]+', '', text)
    text = re.sub('https:[^\s]+', '', text)
    text = re.sub(r'[0-9]', '',text)
    emoj = re.compile("["
                      u"\U0001F600-\U0001F64F"  # emoticons
                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                      u"\U00002500-\U00002BEF"  # chinese char
                      u"\U00002702-\U000027B0"
                      u"\U00002702-\U000027B0"
                      u"\U000024C2-\U0001F251"
                      u"\U0001f926-\U0001f937"
                      u"\U00010000-\U0010ffff"
                      u"\u2640-\u2642"
                      u"\u2600-\u2B55"
                      u"\u200d"
                      u"\u23cf"
                      u"\u23e9"
                      u"\u231a"
                      u"\ufe0f"  # dingbats
                      u"\u3030"
                      "]+", re.UNICODE)
    text = re.sub(emoj, '', text)
    text = "".join(x for x in text if x not in punctuation)
    words = text.split()
    words = [w for w in words if w not in stopwords]
    text = " ".join(words)

    return text
def sentiment_calculator(sentiment_result):
    # decide sentiment as positive, negative and neutral
    if sentiment_result['compound'] >= 0.05:
        return "Positive"

    elif sentiment_result['compound'] <= - 0.05:
        return "Negative"

    else:
        return "Neutral"

class Data_Cleaning:
    def __init__(self, text):
        self.input_text = text
    def text_clean_helper(self):
        return text_cleaning(self.input_text)


class Sentimet_Analysis:
    def __init__(self, text):
        self.input_text = text
    def sentiment_scores(self):
        # Create a object SentimentIntensityAnalyzer .
        s_obj = SentimentIntensityAnalyzer()
        # which contains pos, neg, neu, and compound scores.
        sentiment_result = s_obj.polarity_scores(self.input_text)

        return sentiment_calculator(sentiment_result)



class Main:
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_2.clicked.connect(self.predict)

    def predict(self):
        # get data from input text editor
        text = self.ui.textEdit.toPlainText()
        # creating object of Data_Cleaning class and pass text to constructor
        data_cleaning_obj = Data_Cleaning(text)
        # text clean function call which is in Data_Cleaning class
        clean_text = data_cleaning_obj.text_clean_helper()

        # Make object of Sentiment_Analysis Class
        sentiment_obj = Sentimet_Analysis(clean_text)
        # function call to calculate sentiment score
        prediction = sentiment_obj.sentiment_scores()
        self.ui.label_3.setText(prediction)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.MainWindow.show()
    sys.exit(app.exec_())
