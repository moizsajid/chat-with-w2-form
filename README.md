# Chat with W-2 form

This a Streamlit application uses that `gpt-4-turbo` for answering questions about W-2 tax form

To run the Streamlit, enter the following in the terminal:
```
streamlit run app.py
```

To run Streamlit via Docker, first build the Docker image and then run the Docker container:
```
docker build -t latest .
docker run -it --rm -p 8501:8501 latest
```

To run the unit test, run the following command:
```
python tests.py
```
