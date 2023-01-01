### Download required packages

# import nltk
# nltk.download('gutenberg')
# nltk.download('genesis')
##### Imporing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

## Importing Textblob package
from textblob import TextBlob
# Importing CountVectorizer for sparse matrix/ngrams frequencies
from sklearn.feature_extraction.text import CountVectorizer

## Import datetime
import datetime as dt


import nltk.compat
import itertools
import chardet
##### Read the data file
filepath = "E:/Ruia lectures TY sem 5/project ty/ticketcogflask/ticketpredictiondataclean.csv"


## Checking the encoding factor
with open(filepath,"rb") as mydata:
    result = chardet.detect(mydata.read(1000000))
##### Read the data file
import codecs
# types_of_encoding = ["utf8", "cp1252"]
filepath = "E:/Ruia lectures TY sem 5/project ty/ticketcogflask/ticketpredictdata3.csv"
train_incidents = pd.read_csv(filepath,encoding="utf8")
train_incidents["description_nwords"] = train_incidents["description"].apply(lambda x: len(str(x).split(" ")))
train_incidents[["description","description_nwords"]].sort_values(by = "description_nwords",ascending = True).head()
train_incidents[["description","description_nwords"]].sort_values(by = "description_nwords",ascending = False).head()
train_incidents["description_nchars"] = train_incidents["description"].str.len()
train_incidents[["description","description_nchars"]].sort_values(by = "description_nchars",ascending = False).head()
train_incidents[["description","description_nchars"]].sort_values(by = "description_nchars",ascending = True).head()
def ave_word_len(sentence):
    words  = sentence.split(" ")
    return ((sum((len(word) for word in words))/len(words)))

train_incidents["description_avg_word_len"] = train_incidents["description"].apply(ave_word_len)
train_incidents[["description","description_avg_word_len"]].sort_values(by = "description_avg_word_len",ascending = True).head()
## Importing stop words from nltk.corpus
from nltk.corpus import stopwords
stop = stopwords.words("english")
train_incidents["description_nstopwords"] = train_incidents["description"].apply(lambda word: len([x for x in word.split(" ") if x in stop]))
train_incidents[["description","description_nstopwords"]].sort_values(by = "description_nstopwords",ascending = False).head()
train_incidents["description_ndigits"] = train_incidents["description"].apply(lambda x: len([x for x in x.split() if x.isdigit()]))

train_incidents[["description","description_ndigits"]].sort_values(by = "description_ndigits",ascending = False).head()
train_incidents["description_nupper"] = train_incidents["description"].apply((lambda word: len([x for x in word.split() if x.isupper()])))
train_incidents[["description","description_nupper"]].sort_values(by = "description_nupper",ascending = False).head()
train_incidents["description"] = train_incidents["description"].apply(lambda x: x.lower())
train_incidents["description"].head()
train_incidents["description"] = train_incidents["description"].str.replace("qlik view","qlikview")
train_incidents["description"] = train_incidents["description"].str.replace("qv","qlikview")
train_incidents["description"] = train_incidents["description"].str.replace("wrongly","wrong")
train_incidents["description"] = train_incidents["description"].str.replace("[^\w\s]","")
train_incidents["description"].tail()
train_incidents["description"] = train_incidents["description"].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
from textblob import Word
train_incidents["description"] = train_incidents["description"].apply(lambda x: " ".join([Word(myword).lemmatize() for myword in x.split()])  )
train_incidents["description"].head(5)
### Most frequent words in short description
description_most_freq_words = pd.Series(" ".join(train_incidents["description"]).split()).value_counts()
description_most_freq_words.head(20)
### Least frequent words in short description
description_least_freq_words =  pd.Series(" ".join(train_incidents["description"]).split()).value_counts().sort_values(ascending = True)
description_least_freq_words.head(10)
TextBlob(train_incidents["description"][1]).words
train_incidents["description"][1]
train_incidents["description_tokens"] =  train_incidents["description"].apply(lambda x: TextBlob(x).words)
train_incidents["description_tokens"].head(10)
from nltk import word_tokenize,sent_tokenize
train_incidents["description"].apply(lambda x: word_tokenize(x))
from nltk.stem import PorterStemmer

st = PorterStemmer()

train_incidents["description"][:5].apply(lambda words: " ".join([st.stem(word) for word in words.split()]))
train_incidents["created_at"] = (pd.to_datetime(train_incidents["created_at"],format='%d-%m-%Y %H:%M'))
# train_incidents["sys_updated_on"] = (pd.to_datetime(train_incidents["sys_updated_on"],format='%d/%m/%Y %H:%M'))
# train_incidents["opened_at"] = (pd.to_datetime(train_incidents["opened_at"],format='%d/%m/%Y %H:%M'))
# train_incidents["resolved_at"] = (pd.to_datetime(train_incidents["resolved_at"],format='%d/%m/%Y %H:%M'))
### Extracting dates from datetime object
train_incidents["created_at"] = train_incidents["created_at"].dt.date
# Creating Category GROUPBY Object
incidents_Category = train_incidents.groupby("Category")
print(incidents_Category)
## Creating sub Category GROUPBY Object
# incidents_incident_subcategory = train_incidents.groupby("incident_subcategory")
## Creating priority GROUPBY Object
incidents_priority= train_incidents.groupby("priority_idup")
print(incidents_priority)
## Creating priority GROUPBY Object
incidents_status_idup= train_incidents.groupby("status_idup")
print(incidents_status_idup)
## Creating re-open GROUPBY Object
# incidents_reopen_count= train_incidents.groupby("reopen_count")
## Creating made_sla GROUPBY Object
# incidents_made_sla= train_incidents.groupby("made_sla")
## Creating incident type GROUPBY Object
incidents_application_name= train_incidents.groupby("application_name")
print(incidents_application_name)
# Creating impact GROUPBY Object
# incidents_impact= train_incidents.groupby("impact")

## Creating Escalations GROUPBY Object
# incidents_escalation= train_incidents.groupby("escalation")

## Creating E2E resolution met Object
# incidents_e2e_resolution_met= train_incidents.groupby("e2e_resolution_met")

## Creating location Object
# incidents_location = train_incidents.groupby("current_location")

## Creating location Object
# incidents_country = train_incidents.groupby("country")

## Creating contact type Object
# incidents_contact_type = train_incidents.groupby("contact_type")

## Creating affected user Object
# incidents_affected_user = train_incidents.groupby("affected_user")

## Creating assigned group Object
incidents_assigned_to = train_incidents.groupby("assigned_to")
print(incidents_assigned_to)
## Analyzing top 20 frequent words


sd_freq_plot = description_most_freq_words.head(20).sort_values(ascending = True).plot(kind="barh",title = "Top 20 Frequent Number Of Words")

plt.style.use("ggplot")
sd_freq_plot.set_xlabel("Frequency")
sd_freq_plot.set_ylabel("Terms")

totals = []
for i in sd_freq_plot.patches:
    totals.append(i.get_width())

for i in sd_freq_plot.patches:
    sd_freq_plot.text(i.get_width()+.3,i.get_y()+0.1,str(i.get_width()),fontsize = 8,color= 'black')
    
plt.show()
bigrams = TextBlob(" ".join(train_incidents["description"])).ngrams(2)
word_vectorizer = CountVectorizer(ngram_range=(2,2), analyzer='word')
sparse_matrix = word_vectorizer.fit_transform(train_incidents["description"])
frequencies = sum(sparse_matrix).toarray()[0]
bi_grams_df = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])
print(bi_grams_df)
bi_grams_df.sort_values(by = "frequency",ascending=False).head(20)
plt.style.use("ggplot")
plt.xlabel("Frequency",)
plt.ylabel("Terms")
top20_bigrams = bi_grams_df["frequency"].sort_values(ascending = False).head(20)

top20_bigrams.head(20).sort_values(ascending = True).plot(kind="barh",title = "Top 20 Frequent Bi Grams")
plt.show()

word_vectorizer = CountVectorizer(ngram_range=(2,2), analyzer='word')
sparse_matrix = word_vectorizer.fit_transform(train_incidents["description"])
frequencies = sum(sparse_matrix).toarray()[0]
bi_grams_issue_df = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])

bi_grams_issue_df[bi_grams_issue_df.index.str.contains("access")].sort_values(by = "frequency",ascending=False).head(10)
print(bi_grams_issue_df)
# ### Analyzing top 20 frequent BI Gram words- word containing issue

# plt.style.use("ggplot")
# plt.xlabel("Frequency")
# plt.ylabel("Terms")
# plt.title("Top 10 Frequent Bi Grams contains word ""access""")
# top20_bigrams_issue = bi_grams_issue_df["frequency"].sort_values(ascending = False)

# top20_bigrams_issue_plot = top20_bigrams_issue[top20_bigrams_issue.index.str.contains("issue")].head(10).sort_values(ascending = True).plot(kind="barh")

# totals = []
# for i in top20_bigrams_issue_plot.patches:
#     totals.append(i.get_width())

# for i in top20_bigrams_issue_plot.patches:
#     top20_bigrams_issue_plot.text(i.get_width()+.3,i.get_y()+0.1,str(i.get_width()),fontsize = 10,color= 'black')
# plt.show()
word_vectorizer = CountVectorizer(ngram_range=(3,3), analyzer='word')
sparse_matrix = word_vectorizer.fit_transform(train_incidents["description"])
#sparse_matrix = word_vectorizer.fit_transform(train_incidents["short_description_tokens"])
frequencies = sum(sparse_matrix).toarray()[0]
tri_grams_df = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])
tri_grams_df.sort_values(by = "frequency",ascending=False).head(20)
print(tri_grams_df)
### Analyzing top 20 frequent Tri Gram words

plt.style.use("ggplot")
plt.xlabel("Terms",)
plt.ylabel("Frequency")
trigrams_short_description = tri_grams_df["frequency"].sort_values(ascending = False)
top20_trigrams = tri_grams_df["frequency"].sort_values(ascending = False).head(20)

top5_trigrams_plot =  top20_trigrams.head(5).sort_values(ascending = False).plot(kind="bar",title = "Top 5 Frequent Tri Grams")
top5_trigrams_plot
plt.xticks(rotation=75)
plt.show()
word_vectorizer = CountVectorizer(ngram_range=(2,2), analyzer='word')
sparse_matrix = word_vectorizer.fit_transform(incidents_Category.get_group("Login")["description"])
frequencies_Incident_cate = sum(sparse_matrix).toarray()[0]
grams_df_incident_cate = pd.DataFrame(frequencies_Incident_cate, index=word_vectorizer.get_feature_names_out(), columns=['Incident_category_frequency'])
grams_df_incident_cate.sort_values(by = "Incident_category_frequency",ascending= False).head(10)
print(grams_df_incident_cate)

train_incidents_sorted_opened_at_df  = train_incidents.sort_values(by = "created_at")
train_incidents_sorted_opened_at_df.shape
import seaborn as sns
# sd_token_timeseries["created_at"] = (pd.to_datetime(sd_token_timeseries["created_at"],format = '%Y/%m/%d '))
# ## Delete duplicates value of all the rows
# sd_token_timeseries = sd_token_timeseries.drop_duplicates()

# sd_token_timeseries.head
# sd_token_timeseries["Short_desc_selected_tokens"] = sd_token_timeseries["description"].str.extract("("+'authorization|reload|mismatch|reconciliation|access|qlikview|ebi|query|report|mapping'+")",expand = False)
# plt.figure(figsize=(16,10))

# # use horizontal stripplot with x marker size of 5
# sns.stripplot(y='Short_desc_selected_tokens',x='Opened_at', data=sd_token_timeseries_updated,
#  orient='h', marker='^', color='navy', size=4)
# # rotate x tick labels
# plt.xticks(rotation=50,size= 15)
# plt.yticks(size= 15)
# # remover borders of plot
# plt.style.use("ggplot")
# plt.tight_layout()
# plt.title("Tokens VS tickets Open Date - Time Series Analysis",size= 30)
# plt.ylabel("Issues",size = 20)
# plt.xlabel("Tickets Opened at",size = 20)
# plt.show()
plt.figure(figsize=(16,10))


# use horizontal stripplot with x marker size of 5
sns.stripplot(y='Category',x='created_at', data=train_incidents,
 orient='h', marker='X', color='navy', size=4)
# rotate x tick labels
plt.xticks(rotation=50)
# remover borders of plot
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Incident Category VS tickets Open Date - Time Series Analysis")
plt.ylabel("Sub category")
plt.xlabel("Tickets Opened at")
plt.show()

plt.figure(figsize=(16,10))


# use horizontal stripplot with x marker size of 5
sns.stripplot(y='application_name',x='created_at', data=train_incidents,
 orient='h', marker='X', color='navy', size=4)
# rotate x tick labels
plt.xticks(rotation=50)
# remover borders of plot
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Incident application VS tickets Open Date - Time Series Analysis")
plt.ylabel("Application")
plt.xlabel("Tickets Opened at")
plt.show()

plt.figure(figsize=(16,10))


# use horizontal stripplot with x marker size of 5
sns.stripplot(y='priority_idup',x='created_at', data=train_incidents,
 orient='h', marker='X', color='navy', size=4)
# rotate x tick labels
plt.xticks(rotation=50)
# remover borders of plot
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Incident Priority VS tickets Open Date - Time Series Analysis")
plt.ylabel("Priority")
plt.xlabel("Tickets Opened at")
plt.show()

plt.figure(figsize=(16,10))


# use horizontal stripplot with x marker size of 5
sns.stripplot(y='status_idup',x='created_at', data=train_incidents,
 orient='h', marker='X', color='navy', size=8)
# rotate x tick labels
plt.xticks(rotation=50)
# remover borders of plot
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Incident Status VS tickets Open Date - Time Series Analysis")
plt.ylabel("Status")
plt.xlabel("Tickets Opened at")
plt.show()

sns.lineplot(y='status_idup',x='created_at', data=train_incidents,)
# rotate x tick labels
# plt.xticks(rotation=50)
# remover borders of plot
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Incident Status VS tickets Open Date - Time Series Analysis")
plt.ylabel("Status")
plt.xlabel("Tickets Opened at")
plt.show()

plt.figure(figsize=(16,10))


# use horizontal stripplot with x marker size of 5
sns.stripplot(y='Category',x='application_name', data=train_incidents,
 orient='h', marker='X', color='navy', size=8)
# rotate x tick labels
plt.xticks(rotation=50)
# remover borders of plot
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Incident Category VS tickets Application - Time Series Analysis")
plt.ylabel("Status")
plt.xlabel("Tickets Opened at")
plt.show()

sns.lineplot(y='Category',x='application_name', data=train_incidents)
# rotate x tick labels
# plt.xticks(rotation=50)
# remover borders of plot
# plt.barh(Category,application_name)
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Incident Category VS tickets Application - Time Series Analysis")
plt.ylabel("Status")
plt.xlabel("Tickets Opened at")
plt.show()
# plot(kind="barh",title = "Top 20 Frequent Bi Grams")


plt.figure(figsize=(16,10))

# use horizontal stripplot with x marker size of 5
sns.stripplot(y='resolved_date',x='created_at', data=train_incidents,
 orient='h', marker='X', color='navy', size=4)
# rotate x tick labels
plt.xticks(rotation=50)
# remover borders of plot
plt.style.use("ggplot")
plt.tight_layout()
plt.title("Ticket closure status VS tickets Open Date - Time Series Analysis")
plt.ylabel("Tickets Closure Status")
plt.xlabel("Tickets Opened at")
plt.show()

# bigrams = TextBlob(" ".join(train_incidents["description"])).ngrams(2)
# word_vectorizer = CountVectorizer(ngram_range=(2,2), analyzer='word')
# sparse_matrix = word_vectorizer.fit_transform(train_incidents["description"])
# frequencies = sum(sparse_matrix).toarray()[0]
# bi_grams_df = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])
# print(bi_grams_df)
# bi_grams_df.sort_values(by = "frequency",ascending=False).head(20)
# plt.style.use("ggplot")
# plt.xlabel("Frequency",)
# plt.ylabel("Terms")
# top20_bigrams = bi_grams_df["frequency"].sort_values(ascending = False).head(20)

# top20_bigrams.head(20).sort_values(ascending = True).plot(kind="barh",title = "Top 20 Frequent Bi Grams")
# # plt.show()
# # set size of figure
# plt.figure(figsize=(16,10))

# # use horizontal stripplot with x marker size of 5
# sns.stripplot(y= 'top20_bigrams',x='created_at', data=(train_incidents, bi_grams_df),
#  orient='h', marker='^', color='navy', size=4)
# # rotate x tick labels
# plt.xticks(rotation=50,size= 15)
# plt.yticks(size= 15)
# # remover borders of plot
# plt.style.use("ggplot")
# plt.tight_layout()
# plt.title("Bi Grams VS Tickets Open Date - Time Series Analysis",size= 30)
# plt.ylabel("Bi Grams",size = 20)
# plt.xlabel("Tickets Opened at",size = 20)
# plt.show()

# print(bi_grams_df)
# bi_grams_df.sort_values(by = "frequency",ascending=False).head(20)
# plt.style.use("ggplot")
# plt.xlabel("Frequency",)
# plt.ylabel("Terms")
# top20_bigrams = bi_grams_df["frequency"].sort_values(ascending = False).head(20)

# top20_bigrams.head(20).sort_values(ascending = True).plot(kind="barh",title = "Top 20 Frequent Bi Grams")
# plt.show()
train_incidents["sentiments"] = train_incidents["description"].apply(lambda x: TextBlob(x).sentiment[0])
train_incidents[["description","sentiments","description_tokens"]].sort_values(by = "sentiments",ascending = True)
print(train_incidents)
incidents_priority["sentiments"].sum()
# print(incidents_priority["sentiments"])
incidents_priority["sentiments"].sum().plot(kind= "bar")
plt.title("Sentiment Polarity VS Incident Impact")
plt.xlabel("Impact")
plt.ylabel("Polarity")
plt.xticks(rotation = "0.5")
plt.show()
incidents_Category["sentiments"].sum().sort_values(ascending = True)
print(incidents_Category['sentiments'].sum())
incidents_application_name["sentiments"].sum().plot(kind ="bar",color= ["pink","brown"])
plt.title("Application Wise Sentiment Polarity Analysis")
plt.xlabel("Application")
plt.ylabel("Polarity")
plt.xticks(rotation = "0.5")
plt.show()

def sentiment_type(value):
    if value >= 0.5:
        return "Positive"
    elif value <= -0.5:
        return "Negitive"
    else:
        return "Neutral"
train_incidents["sentiment_types"] = train_incidents["sentiments"].apply(sentiment_type)
train_incidents["sentiment_types"].value_counts()
print(train_incidents["sentiment_types"].value_counts())
train_incidents["sentiment_types"].value_counts().plot(kind = "bar",color = ["blue","red","green"])
plt.title("Sentiment types classification frequency")
plt.xlabel("Sentiment Types")
plt.ylabel("Frequency")
plt.xticks(rotation = "0.5")
plt.show()

# train_incidents["issue_turnaround_time_hours"] = (train_incidents["resolved_date"] - train_incidents["created_at"]).astype('timedelta64[h]')
# ## Impute missing values with mean 
# train_incidents["issue_turnaround_time_hours"][train_incidents["issue_turnaround_time_hours"].isna() == True] = train_incidents["issue_turnaround_time_hours"].mean(skipna= True)

# train_incidents["issue_turnaround_time_days"] = (train_incidents["resolved_date"].dt.date - train_incidents["created_at"].dt.date)
# train_incidents["issue_turnaround_time_days"] = pd.to_numeric(train_incidents["issue_turnaround_time_days"].dt.days)
# ## Impute missing values with mean 
# train_incidents["issue_turnaround_time_days"][train_incidents["issue_turnaround_time_days"].isna() == True] = train_incidents["issue_turnaround_time_days"].mean(skipna= True)

# train_incidents["issue_turnaround_time_days"].head(2)
# linregress(train_incidents["issue_turnaround_time_days"],train_incidents["sentiments"])
# train_incidents.plot.scatter("issue_turnaround_time_days","sentiments")
# plt.show()
