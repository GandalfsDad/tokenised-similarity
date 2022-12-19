import pandas as pd
import os
import numpy as np

from modeling.tokenizer import OpenAITokenizer

def loadBookSummaries(path):
    data = pd.read_csv(path, sep='\t', header=None)
    data.columns = ['WikipediaID','FreebaseID','BookTitle','Author','PublicationDate','Genres','PlotSummary']

    return data

def loadTokenizedBookSummaries(nameArrayPath, tokenArrayPath, bookSummariesPath, keyVariable = 'OPENAI_API_KEY'):
    if os.path.exists(tokenArrayPath) & os.path.exists(nameArrayPath):
        
        with open(tokenArrayPath, 'rb') as f:
            tokenizedSummaries = np.load(f,allow_pickle=True)

        with open(nameArrayPath, 'rb') as f:
            titles = np.load(f,allow_pickle=True)

    else:
        data = loadBookSummaries(bookSummariesPath)

        titles = data['BookTitle'].values

        with open(nameArrayPath, 'wb') as f:
            np.save(f, titles)

        tokenizer = OpenAITokenizer(keyVariable)

        tokenizedSummaries = tokenizer.tokenize(list(data['PlotSummary'].values))
        with open(tokenArrayPath, 'wb') as f:
            np.save(f, np.array(tokenizedSummaries))

    return titles, tokenizedSummaries
