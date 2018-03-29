import nltk
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
porter = WordNetLemmatizer()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open('news2.csv','ab') as csvfile:
    fieldnames = ['Date','Title','Description'];
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames);
    writer.writeheader();

    with open('news.csv') as csvfile:
        reader = csv.DictReader(csvfile);
        for row in reader:
            date = row['Date'].encode("utf-8");
            title = row['Title'].encode("utf-8");
            description = row['Description'].encode("utf-8");

            print("\nNEWS : ");
            print(title);
            print(description);

            titleTokens = word_tokenize(title)
            descriptionTokens = word_tokenize(description)
            titleWords = [word for word in titleTokens if word.isalpha()]
            descriptionWords = [word for word in descriptionTokens if word.isalpha()]
            titleTokens = titleWords;
            titleTokens = [w.lower() for w in titleTokens]
            descriptionTokens = descriptionWords;
            descriptionTokens = [w.lower() for w in descriptionTokens]
            titleTokens = [w for w in titleTokens if not w in stop_words]
            descriptionTokens = [w for w in descriptionTokens if not w in stop_words]
            stemmedTitle = [porter.lemmatize(word) for word in titleTokens]
            stemmedDescription = [porter.lemmatize(word) for word in descriptionTokens]

            joinedTitle = " ".join(stemmedTitle);
            joinedDescription = " ".join(stemmedDescription)
            print(joinedTitle);
            print(joinedDescription);

            writer.writerow({'Date':date,'Title':joinedTitle,'Description':joinedDescription});
