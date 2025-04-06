from langchain_core.tools import Tool
from langchain import hub  
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from agents.tools import get_ytb_transcript,fetch_transcript_all
from langchain.prompts import PromptTemplate

load_dotenv()

def summ_agent(transcript:str)->list[dict]:

    llm = ChatGroq(
                model_name="llama-3.3-70b-versatile",
                temperature=0.3
                ) 
                
    prompt="""You are a smart assistant. Your task is to summarize the transcript of a YouTube video. 
    Output format:
    - Summary title
    - Important bullet points
    
    Here is the transcript of the video:
    <transcript>
    {transcript}
    </transcript>
"""
    prompt_template = PromptTemplate(
        input_variables=["transcript"],
        template=prompt,
    )
    chain = prompt_template | llm
    result = chain.invoke(input={"transcript":transcript})
    return result
    
      