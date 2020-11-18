import pickle

vc = pickle.load(open("Functions/vc.pickle", "rb"))

def analyse(vec_input):
    proba = vc.predict_proba(vec_input)
    result = (proba[:,1] > 0.65) *1
    if result == 0:
        return 'This seems to be a neutral/negative text.'
    else:
        return 'This seems to be a positive text.'