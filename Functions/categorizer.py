import pickle

class Categorizer():
    
    def __init__(self):
        self.tfidf = pickle.load(open('Functions/tfidf_categorizer.pkl', 'rb'))
        #self.lemmatizer = lemmatizer
        self.svc = pickle.load(open('Functions/svc.pkl', 'rb'))
        
    def preprocess(self, X):
        # Check if X is string, turn to list
        if type(X) == str:
            X = [X]
        # Lemmatization
        #X_lem = [self.lemmatizer.lem_text(x) for x in X]
        # Tfidf vectorization
        X_tfidf = self.tfidf.transform(X)
        return X_tfidf
    
    def pred(self, X):
        # preprocess
        X_tfidf = self.preprocess(X)
        # return categories
        return self.svc.predict(X_tfidf)[0]
    
    