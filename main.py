import os

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from modeling.data import loadTokenizedBookSummaries


if __name__ == '__main__':
    
    keyVariable = 'OPENAI_API_KEY'
    
    titles, summaries = loadTokenizedBookSummaries(
                            'bin/titles.npy',                       #Book titles
                            'bin/tokenizedSummaries.npy',           #Tokenized summaries
                            'bin/booksummaries/booksummaries.txt',  #Book summaries
                            keyVariable=keyVariable                 #OpenAI API key
                        )

    #Find the most similar book to the Hobbit (85)
    n = 85
    similarity = cosine_similarity(summaries[n].reshape(1,-1), summaries)

    #Find the 10 most similar books
    mostSimilar = np.argsort(similarity[0])[::-1][1:11] #skip the first (will be the same book)

    #Print the results
    print('Most similar books to: ', titles[n])
    for i in mostSimilar:
        print(titles[i], similarity[0][i])
