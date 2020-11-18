import spacy
import pickle

class Preprocessor:
    
    def __init__(self, text_input=''):
        self.text = text_input
        self.nlp = spacy.load('en_core_web_sm')
        pickle_in = open("Functions/tfidf.pickle", "rb")
        self.transformer = pickle.load(pickle_in)
        
    def is_token_allowed(self, token):
        if (not token or not token.string.strip() or
            token.is_stop or token.is_punct) or token.like_url or token.like_email or token.like_num:
            return False
        return True
    
    def lem_text(self):

        text = self.text.lower()
        doc = self.nlp(text)
        text = [token.lemma_ for token in doc if self.is_token_allowed(token)]

        return ' '.join(text).replace('"', '').replace("'", '')
    
    def transform(self):
        text = self.lem_text()
        
        return self.transformer.transform([text])  