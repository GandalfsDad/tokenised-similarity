# OPENAI Embeddings Work

This repo is just me attempting to play around with the openai api embeddings models.


# Dataset
The dataset i've used is a book summaries dataset.
Run the below command to extract it.
```bash
curl http://www.cs.cmu.edu/\~dbamman/data/booksummaries.tar.gz | tar xz -C bin
```

# Environment

1. Create a venv
```bash
python -m venv env
```
2. activate the environment
```bash
source ./env/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

# Run Script
After activating the environment and installing the requirements the script can be run.
```bash
python main.py
```

This should output the 10 most similar books in the dataset to The Hobbit.