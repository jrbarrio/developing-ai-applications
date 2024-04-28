```
pyenv virtualenv 3.11.7 developing-ai-applications
echo "developing-ai-applications" > .python-version
pip install pipenv
pipenv install transformers datasets
pipenv install torch torchvision torchaudio torchtext --index=pytorch
pipenv install huggingface_hub
```
