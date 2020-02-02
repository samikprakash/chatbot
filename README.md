# chatbot
A chatbot to answer student's queries regarding courses offered in their institutes

Types of queries answered: 
  1) Courses offered.
  2) Pre requisites required.
  3) Professors teaching the course and data on it.
  4) Past year records.
  
Dependencies:
  1) Python >= 3.5
  2) NLTK
    a) First, do pip install NLTK.
    b) Second, open interactive python shell and import NLTK.
    c) Third, type nltk.download() which will take you to a downloader. Download all modules.
  3) Keras
  4) Numpy

How to run:
  1) Open command prompt/terminal in this directory.
  2) python3 bot.py
  3) If the bot is unable to understand the user query, the control will be transferred to a human.
  4) To give the control back to the bot, type "bot" in the "(human):" section. 
