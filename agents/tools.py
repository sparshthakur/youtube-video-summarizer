from youtube_transcript_api import YouTubeTranscriptApi
from agents.schema import TranscriptInput,TranscriptInput2
from datetime import timedelta
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

def fetch_transcript_all(video_url:str):
    """
    Fetches the full transcript of a YouTube video using its URL..
    
    Args:
        video_url (str): The URL of the YouTube video.
        
    Returns:
        list: A list of dictionaries containing the transcript.
    """
    
    video_id = video_url.split("v=")[-1]   
    try:
        # Fetch available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Try to get manually created English transcript first
        try:
            transcript = transcript_list.find_manually_created_transcript(language_codes=["en"])
        except NoTranscriptFound:
            # If manual not found, try auto-generated
            transcript = transcript_list.find_generated_transcript(language_codes=["en"])
        
        transcript_all= transcript.fetch()
        transcript_clean= []
        for entry in transcript_all:
            entry_dict = vars(entry)
            transcript_clean.append({
                "text": entry_dict["text"],
                "start": entry_dict["start"],
                "duration": entry_dict["duration"], 
            })
        return transcript_clean

    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("No transcript found (manual or auto) in the given language.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_ytb_transcript(transcript:list[dict],start_time:int, end_time:int)->str:
    """
    Extracts a transcript segment from the full transcript between start and end times.
    
    """
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