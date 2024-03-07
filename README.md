# Youtube Video Assistant

## How to use

### 1. Clone or download the repository.

### 2. Create an account or login to your Hugging Face account. Then create a access token.

### 3. Copy that token.

### 4. Go the the project directory and create a .env file.

### 5. In .env file paste in your access token that you copied.

```
Example
HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxxxxxxxxx
```

#### P.S Make sure to name the environment like this: HUGGINGFACEHUB_API_TOKEN

### 6. Create a virtual environment.

```
python -m venv env
```

### 7. Activate your virtual environment

```
Windows
env\scripts\activate
Linux
source env/bin/activate
```

### 8. Install all the requirements.

```
pip install -r requirements.txt
```

### 9. Now go the terminal and run the app.

```
streamlit run main.py
```

### 10. In the terminal you will be given a url. Go to that url from your browser. Now give the youtube video url that you want to know about, then type in what you want to know about. Hit submit button and wait for the answer as it will take some time for the first time running the app.

#### P.S Answer will not be accurate all the time.
