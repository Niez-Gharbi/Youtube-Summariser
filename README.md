# YouTube Video Summarizer

## Overview

The YouTube Video Summarizer is a Streamlit app that uses the BART model to generate summaries from YouTube video transcripts. It allows users to input a YouTube video link, and the app retrieves the transcript, processes it, and generates a concise summary.

## Features

- Accepts YouTube video links as input.
- Validates the link format.
- Extracts the video ID from the link.
- Retrieves the video transcript using the YouTube Transcript API.
- Uses the BART model to generate a summary from the transcript.

## Installation

1. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    ```bash
    .\venv\Scripts\activate
    ```
    
3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Streamlit app:

```bash
cd src
streamlit run app.py
```

Visit http://localhost:8501 in your web browser to use the app.

## License

This project is licensed under the [Apache License 2.0](https://github.com/Niez-Gharbi/Youtube-Summariser/blob/main/LICENSE).
