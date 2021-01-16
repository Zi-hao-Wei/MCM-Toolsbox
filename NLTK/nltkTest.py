import nltk
from nltk.corpus import stopwords,wordnet
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
# sentence = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
sentence ="'football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.'"

ps=PorterStemmer()
wnl=WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

tokens=tokenizer.tokenize(sentence)
filtered=[]

for w in tokens:
    if w not in stop_words:
        filtered.append(w)

tagged_sent=nltk.pos_tag(filtered) #filterWords

filteredWords=[]

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

for w in tagged_sent:
    wordnet_pos = get_wordnet_pos(w[1]) or wordnet.NOUN
    fwords=wnl.lemmatize(w[0],pos=wordnet_pos) #Lemmatization
    filteredWords.append(fwords)

print(filteredWords)
