import os
from modeling.tokenizer import OpenAITokenizer



if __name__ == '__main__':
    
    keyVariable = 'OPENAI_API_KEY'
    tokenizer = OpenAITokenizer(keyVariable)

    example = ['This is a test','and so is this']

    
    print(tokenizer.tokenize(example).shape)