import pandas as pd

def loadBookSummaries(path):
    data = pd.read_csv(path, sep='\t', header=None)
    data.columns = ['WikipediaID','FreebaseID','BookTitle','Author','PublicationDate','Genres','PlotSummary']

    return data