import nltk,json,pickle
from nltk.stem import WordNetLemmatizer
import numpy as np
import pickle
from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

class Bot:
    intents = json.loads(open('intents.json').read())
    words = pickle.load(open('words.pkl','rb'))
    classes = pickle.load(open('classes.pkl','rb'))
    model = load_model('chatbot_model.h5')
    lemmatizer = WordNetLemmatizer()
    def __init__(self):
       pass

    def clean(self,sentence):
        s_words = nltk.word_tokenize(sentence)
        s_words = [self.lemmatizer.lemmatize(word.lower()) for word in s_words]
        return s_words
    
    def bag_of_words(self,sentence,words,show_details=True):
        sentence_words = self.clean(sentence)
        bag = [0]*len(self.words)
        for s in sentence_words:
            for i,w in enumerate(self.words):
                if w == s: 
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))
    
    def predict(self,sentence,model):
        b = self.bag_of_words(sentence, words, show_details=False)
        res = self.model.predict(np.array([b]))[0]
        error_threshold = 0.90
        result = [[i,r] for i,r in enumerate(res) if r>error_threshold]
        result.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in result:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        # print(return_list)
        return return_list

    def response(self,ints, intents_json):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        return result
    
    def chatbot_answer(self,msg):
        ints = self.predict(msg,self.model)
        if len(ints )== 0:
            
            return 
        result = self.response(ints,self.intents)
        return result

if __name__ == "__main__":
    siri = Bot()
    print("Enter quit to exit.")
    x = ""
    flag = True
    while x != "quit":
        x = input("(User): ").lower()
        if x=="quit":
            print("(Bot): See you soon!")
            break
        if siri.chatbot_answer(x)!= None and flag==True:
            print("(Bot): " + siri.chatbot_answer(x))
        
        elif siri.chatbot_answer(x) == None:
            if flag==True:
                print("Sorry I am unable to understand you, A human will be with you soon!")
            flag = False
        
        if flag == False:    
            
            a = input("(Human): ")

            if a.lower() == "bot":
                
                flag = True
    



