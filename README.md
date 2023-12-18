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

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Change into the project directory:

    ```bash
    cd your-repo
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
Visit http://localhost:8501 in your web browser to use the app.

## Credits
Niez Gharbi: Project creator and developer.
License
This project is licensed under the MIT License.

javascript
Copy code

Make sure to include a `requirements.txt` file in your project directory with the necessary dependencies. You can generate the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
This will save a list of installed packages in your virtual environment to the requirements.txt file. Adjust the pip install -r requirements.txt command in the README if needed.