import numpy as np


# d1 = 'London is windy today'
# d2 = 'It is quite windy'
# d3 = 'The weather is nice in Paris'

def calc_term_frequency(query, data):
    res = {}
    for word in query:
        total = 0
        for i, d in enumerate(data):
            index = (word, i)
            tokens = d.split()
            count = tokens.count(word)
            res[index] = count
            if count > 0:
                total += 1
        res[word] = total
    return res

def calc_inverse_document_frequency(query, data, tf):
    res = {}
    for word in query:
        numerator = len(data) - tf[word] + 0.5
        denominator = tf[word] + 0.5
        fraction = numerator / denominator
        res[word] = np.log(fraction + 1)
    return res

def calc_document_length_normalization(data):
    res = 0
    for d in data:
        res += len(d.split(' '))
    res /= len(data)
    return res

def bm25(query, data):
    query = query.split(' ')

    tf = calc_term_frequency(query, data)
    idf = calc_inverse_document_frequency(query, data, tf)
    dln = calc_document_length_normalization(data)
    k1 = 1.2 
    b = 0.75
    res = {}
    for i, d in enumerate(data):
        score = 0
        
        for word in query:
            num = tf[(word, i)] * (k1 + 1)
            den = tf[(word, i)] + (k1 * (1 - b + b * (len(d.split(' ')) / dln)))
            
            frac = num / den 
            score += idf[word] * frac
        res[f'd{i+1}'] = score
    
    return res
    
# query = 'windy London'
# bm25(query)

    
            