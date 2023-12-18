from transformers import BartTokenizer, BartForConditionalGeneration
from youtube_transcript_api import YouTubeTranscriptApi
import re
import logging

# Suppress transformers library logging
logging.getLogger("transformers.tokenization_utils_base").setLevel(logging.ERROR)

class Summarizer:
    """
    A class for generating summaries from YouTube video transcripts using the BART model.

    Attributes:
    - tokenizer: An instance of the BartTokenizer for tokenizing text.
    - model: An instance of the BartForConditionalGeneration for generating summaries.

    Methods:
    - is_valid_youtube_link(link): Validates if the provided link is a valid YouTube video link.
    - extract_video_id(link): Extracts the video ID from a valid YouTube video link.
    - generate_summary(link): Generates a summary for a YouTube video given its link.
    """

    def __init__(self):
        """
        Initializes the Summarizer class with a tokenizer and a model.
        """
        self.tokenizer = self.get_tokenizer()
        self.model = self.get_model()

    def get_tokenizer(self):
        """
        Retrieves and returns an instance of the BartTokenizer.

        Returns:
        - tokenizer: An instance of the BartTokenizer.
        """
        tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn', truncation=True)
        return tokenizer

    def get_model(self):
        """
        Retrieves and returns an instance of the BartForConditionalGeneration model.

        Returns:
        - model: An instance of the BartForConditionalGeneration model.
        """
        model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
        return model

    @staticmethod
    def is_valid_youtube_link(link):
        """
        Validates if the provided link is a valid YouTube video link.

        Args:
        - link (str): The YouTube video link.

        Returns:
        - bool: True if the link is valid, False otherwise.
        """
        regex_pattern = r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]+)"
        return bool(re.match(regex_pattern, link))

    def extract_video_id(self, link):
        """
        Extracts the video ID from a valid YouTube video link.

        Args:
        - link (str): The valid YouTube video link.

        Returns:
        - str or None: The extracted video ID or None if not found.
        """
        match = re.search(r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]+)", link)
        return match.group(4) if match else None

    def generate_summary(self, link):
        """
        Generates a summary for a YouTube video given its link.

        Args:
        - link (str): The YouTube video link.

        Returns:
        - str: The generated summary or an error message if an issue occurs.
        """
        try:
            # Check if the link is in the expected format
            if not self.is_valid_youtube_link(link):
                raise ValueError("Invalid YouTube video link format. Please provide a valid link.")

            # Extract the video ID from the link
            video_id = self.extract_video_id(link)
            if not video_id:
                raise ValueError("Unable to extract video ID from the link.")

            # Attempt to get the transcript
            try:
                sub = YouTubeTranscriptApi.get_transcript(video_id)
            except Exception as transcript_error:
                raise RuntimeError(f"Error retrieving transcript: {str(transcript_error)}")

            # Attempt to generate the summary
            try:
                subtitle = " ".join([x['text'] for x in sub])
                input_tensor = self.tokenizer.encode(subtitle, return_tensors="pt", max_length=1024)
                outputs_tensor = self.model.generate(input_tensor,
                                                     max_length=1200,
                                                     min_length=120,
                                                     length_penalty=2.0,
                                                     num_beams=4,
                                                     early_stopping=True)
                summary = self.tokenizer.decode(outputs_tensor[0], skip_special_tokens=True)
                return summary
            except Exception as generation_error:
                raise RuntimeError(f"Error generating summary: {str(generation_error)}")

        except ValueError as value_error:
            return f"Error: {str(value_error)}"
        except RuntimeError as runtime_error:
            return f"Error: {str(runtime_error)}"
        except Exception as general_error:
            return f"An unexpected error occurred: {str(general_error)}"