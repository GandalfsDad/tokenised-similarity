import openai
import os
import numpy as np


class OpenAITokenizer:

    DEFAULT_MODEL = "text-embedding-ada-002"
    
    def __init__(self, key, modelName = None):
        openai.api_key = os.getenv(key)

        if modelName is None:
            self._model = OpenAITokenizer.DEFAULT_MODEL
        else:
            self._model = modelName

    def tokenize(self, inputs):
        response = openai.Embedding.create(
            model=self._model,
            input=inputs)
        
        return np.array([x['embedding'] for x in response['data']])