
# import io
# import random
# import string # to process standard python strings
# import warnings
# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import warnings
# warnings.filterwarnings('ignore')

# import nltk
# from nltk.stem import WordNetLemmatizer
# nltk.download('popular', quiet=True) 

# import pandas as pd
# # from flask_mysqldb import sql
# # db_connect =sql.connect(host:127.0.0.1)
# # db_connect = sql.connect(host='127.0.0.1', database='ticketcog', user = 'root', password = 'root')
# # data = pd.read_sql('SELECT * from ticket', con=db_connect)
# # data.head()
# data=pd.read_csv('kedb.csv')
# question=data['Issue'].tolist()
# Category=data['Category'].tolist()
# Application_name=data['Application_name'].tolist()
# answer=data['Resolution'].tolist()

# lemmer = nltk.stem.WordNetLemmatizer()


# #WordNet is a semantically-oriented dictionary of English included in NLTK.
# def LemTokens(tokens):
#     return [lemmer.lemmatize(token) for token in tokens]
# remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



# GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey","how are you")
# GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]
# def greeting(sentence):
 
#     for word in sentence.split():
#         if word.lower() in GREETING_INPUTS:
#             return random.choice(GREETING_RESPONSES)


# GI = ("how are you")
# GR = ["i'm fine","good,how can i help you!"]
# def greet(sentence):
 
#     for word in sentence.split():
#         if word.lower() in GREETING_I:
#             return random.choice(GREETING_R)

# def responses(v,a,q):
#     response=''
#     question.append(v)
#     Category.append(v)
#     Application_name.append(a)
#     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
#     tfidf = TfidfVec.fit_transform(question)
#     val = cosine_similarity(tfidf[-1], tfidf)

#     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
#     tfidf = TfidfVec.fit_transform(Category)
#     val1= cosine_similarity(tfidf[-1], tfidf)
#     tfidf1 = TfidfVec.fit_transform(Application_name)
#     val2 = cosine_similarity(tfidf1[-1], tfidf1)

#     id0=val.argsort()[0][-2]
#     id1=val1.argsort()[0][-2]
#     id2=val2.argsort()[0][-2]
#     print(id1)
#     print(id2)
#     print(id0)
    
#     flat = val.flatten()
#     flat.sort()
#     print(flat)
#     flat1 = val1.flatten()
#     flat1.sort()
#     print(flat1)
#     flat2 = val2.flatten()
#     flat2.sort()
#     print(flat2)
#     req = flat[-2]
#     req1 = flat1[-2]
#     req2 = flat2[-2]
#         # print(req)
#         # print(req1)
    
    	
#     # for word in response.split():
#     #     if word.lower() in GREETING_INPUTS:
#     #         return random.choice(GREETING_RESPONSES)

#     # if(response=='how are you'):
#     # 	return random.choice(GREETING_R)

#     # for word in response.split():
#     #     if word.lower() in ["nice","good","good job","okay","cool","great"]:
#     #         return "smile.."
    
#     if(req==0 and req1 == 0):
#         response=response+"I am sorry! I don't understand you"
#         return(print("No response"))
#     else:
#         if req1 in Category and req2 in Application_name :
#                 # if(req==val and req2==val2):
#             response = response+answer[id1]+answer[id2]
#             Category.remove(v)
#             Application_name.remove(a)
#             return response
# command=1
# while(command):
#     q = input("Enter your Issue: ") 
#     v = input("Enter your Category: ") 
#     a = input("Enter your application: ") 

#     # app = input("Enter your application: ") 
#     if(v=="exit"):
#         command=0
#     else:
#         print(responses(str(v), str(a), str(q))) 
# import csv
# def loadcsv(self,application):
#     search = input("Enter category:")
#     application = input("Enter application:")
#     print(search,application)
#     with open("kedb.csv","r") as csvfile:
#         csvloader = csv.reader(csvfile,delimiter=",",quotechar="|")
#         for row in csvloader:
#             print(row)
#             if search == row[2] and application == row[3] :
#                 print(row)
#                 self.category = search
#                 self.application = application
#                 # self.category =search
# loadcsv('crash','sap')
import csv
import sys

#input number you want to search
number = input('Enter Category to find\n')
application = input('Enter Applicaation name\n')


#read csv, and split on "," the line
csv_file = csv.reader(open('kedb.csv', "r"), delimiter=",")


#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number == row[2] and application == row[3]:
         print (row[0],row[4])
    

    