from nltk.stem import PorterStemmer, SnowballStemmer

words = ["running", "runs", "easily", "fairly", "studies", "studying",
         "connection", "connected", "connecting", "generous", "generously", "happiness"]

porter = PorterStemmer()
snowball = SnowballStemmer("english")

print(f"{'Word':14s}{'Porter':12s}{'Snowball'}")
for w in words:
    print(f"{w:14s}{porter.stem(w):12s}{snowball.stem(w)}")
