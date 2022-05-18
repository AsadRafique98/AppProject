# AppProject
Project Description

Important packegs use in this project

	PyQt5
	nltk
	googletrans==3.1.0a0
	vaderSentiment

There are two python files.
GUI.py 
Main.py

GUI.py file contain class Ui_MainWindow and main method
in which all the codes related to the GUI created of the project.

Main.py file contain all backend logic of the project.
This contain two classes with data members and functions.Four outside functions
Classes:
1) Sentiment_Analysis 
	This class use to do sentiment analysis
	There are two member functions
	1) def __init__(self, text):
		This is use to initialize the text data.
	2) def sentiment_scores(self):
		This is use to calculate the score of text.
2) Data_Cleaning
	This class use to clean the data.
	This class have text_clean_helper function which call text_cleaning function created 
	outside the class
	
3) Main
	This is the main class of the project. 
	This class have two methods
	1) def __init__(self):
		This function use to initialize the GUI part.
	2) Predict
		This function use to do prediction and in this function 
		first get the text from GUI part on button click and then pass the text to 
		Sentiment_Analysis class.
OutSide Functions:

1) def convert_to_english(text):
	This function use google translators to translate non english text to english
2) def text_cleaning(text):
	This function use to clean the text from punctuations emojies all non english words.
3) def sentiment_calculator(sentiment_result):
	This function  decide sentiment as positive, negative and neutral.
4) if __name__ == '__main__':
	This is the main driver function of the project.
