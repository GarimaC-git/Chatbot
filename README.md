# Gemini AI Chatbot

A simple chatbot using Google's Gemini AI and Streamlit.
## 🔗 Live Demo  
[Click here to try the chatbot!](https://ai-chatbot-gc.streamlit.app/chat)  


## Installation

1. Clone the repository and navigate to the project folder:

   ```sh
   git clone https://github.com/GarimaC-git/Chatbot.git
   cd Chatbot
   ```

2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the App

Start the chatbot using the following command:

```sh
streamlit run home.py
```

## Configuration

Ensure your API key is set in `secrets.toml` inside the `.streamlit` folder:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

## Deployment

To deploy on Streamlit Cloud, push your code to GitHub and connect your repository on [Streamlit Share](https://share.streamlit.io/).


