# OPENAI Embeddings Work

This repo is just me attempting to play around with the openai api embeddings model.
I've just made a quick script that finds similar books based on the similarity of embeddings.

---

## Setup

### direnv
I've used direnv to manage my environment variables. Installation is found [here](https://direnv.net/).
Once installed create a .envrc file based on .envrc.example and add in your openapi key.

You may have to allow direnv to use the .envrc (usually you are prompted when you enter the directory)
```bash
direnv allow
```

### Dataset
The dataset i've used is a book summaries dataset.
Run the below command to extract it.
```bash
curl http://www.cs.cmu.edu/\~dbamman/data/booksummaries.tar.gz | tar xz -C bin
```

### Environment

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

---
## Run Script
After activating the environment and installing the requirements the script can be run.
```bash
python main.py
```

This should output the 10 most similar books in the dataset to The Hobbit.