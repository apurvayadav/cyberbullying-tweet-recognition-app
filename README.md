# cyberbullying-tweet-prediction-app
Web app Link: [https://apurvayadav-cyberbullying-tweet-recognition-app-webapp-z6y643.streamlitapp.com/](https://apurvayadav-cyberbullying-tweet-recognition-app-webapp-z6y643.streamlitapp.com/)

This app predicts the nature of the tweet into 6 Categories.

* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

## Tools and Technologies  
**Model:** Used linear Support Vector Machine to classify tweets.  
**Streamlit:** Used Streamlit to create simple webapp to make the model interactive.  

## Methodology
* Downloaded the data from kaggle. [(data)](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
* Performed some Exploratory Data Analysis to get the overview of data. [(initial_modelling.ipynb)](https://github.com/apurvayadav/cyberbullying-tweet-recognition-app/blob/main/initial_modelling.ipynb)
*  Created a Word Cloud from the data.
*  Performed the necessary steps for textual analysis.
    * Removing Stopwords, puctuations, URLs, etc
    * Performed Stemming and Lemmatization.
* Automated the process of preprocessing by creating functions. Which would be helpful in predicting Custom Outputs.
* Created Illustrations for the webapp from [Canva](https://www.canva.com/). [(Images)](https://github.com/apurvayadav/cyberbullying-tweet-recognition-app/tree/main/images)
* Deployed the webapp on streamlit.

## References
* Twitter Sentiment Analysis- A NLP Use-Case for Beginners - [https://www.analyticsvidhya.com/blog/2021/06/twitter-sentiment-analysis-a-nlp-use-case-for-beginners/](https://www.analyticsvidhya.com/blog/2021/06/twitter-sentiment-analysis-a-nlp-use-case-for-beginners/)
