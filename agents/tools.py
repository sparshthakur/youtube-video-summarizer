from youtube_transcript_api import YouTubeTranscriptApi
from agents.schema import TranscriptInput,TranscriptInput2
from langchain.tools import tool
from datetime import timedelta
import ast

@tool(args_schema=TranscriptInput2)
def fetch_transcript_all(video_url:str):
    """
    Fetches the full transcript of a YouTube video using its URL.Use this tool to get the full transcription of the youtube video. The output is a list of dictionaries with the keys: start, duration, text. The input is the youtube video url.
    
    Args:
        video_url (str): The URL of the YouTube video.
        
    Returns:
        list: A list of dictionaries containing the transcript.
    """

    video_id = video_url.split("v=")[-1]
    transcript = YouTubeTranscriptApi().get_transcript(video_id)
    return transcript

@tool(args_schema=TranscriptInput)
#def get_ytb_transcript(transcript:list[dict],start_time:int, end_time:int)->str:
def get_ytb_transcript(args_str:str)->str:
    """
    Extracts a transcript segment from the full transcript between start and end times.
    
    Expects input like: ([{"text": "..."}, ...], 0, 60)
    """
    try:
        # Convert the string into an actual Python tuple
        parsed = ast.literal_eval(args_str)

        # Unpack values
        transcript, start_time, end_time = parsed

        # Basic validation
        if not isinstance(transcript, list) or not isinstance(start_time, (int, float)) or not isinstance(end_time, (int, float)):
            return "❌ Invalid input format."

    except Exception as e:
        return f"❌ Error parsing input: {e}"
    
    filtered_lines = [
        entry["text"]
        for entry in transcript
        if start_time <= entry["start"] <= end_time
    ]

    final_transcript = " ".join(filtered_lines)
    return final_transcript

def timestamp_to_seconds(ts: str) -> int:
    parts = list(map(int, ts.split(":")))
    if len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds
    elif len(parts) == 3:
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds
    else:
        raise ValueError("Invalid timestamp format. Use MM:SS or HH:MM:SS")

def seconds_to_timestamp(seconds: int) -> str:
    return str(timedelta(seconds=seconds))