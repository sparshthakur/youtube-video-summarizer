from pydantic import BaseModel

class TranscriptInput(BaseModel):
    #transcript: list[dict[str, str,str]]
    #start_time: int
    #end_time: int
    args_str: str

class TranscriptInput2(BaseModel):
    video_url: str
