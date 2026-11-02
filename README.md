# Automatic Text Summarization Using Transformers

## Overview
This project is an AI-powered text summarization application built with Python, Transformers, and Streamlit. It uses a pre-trained Transformer model from Hugging Face to generate concise summaries of long text articles.

## Model Information & Source Link
* **Model Name:** `facebook/bart-large-cnn`
* **Model Type:** Sequence-to-sequence Transformer model fine-tuned for text summarization.
* **Hugging Face Source Link:** [https://huggingface.co/facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)

## Project Structure
- `app.py`: Streamlit frontend web user interface.
- `summarizer.py`: Text summarization pipeline logic using Hugging Face Transformers.
- `evaluation.py`: Model evaluation script (calculating ROUGE scores).
- `requirements.txt`: Python dependencies required to run the project.
- `README.md`: Project documentation and setup guide.

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt