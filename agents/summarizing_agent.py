from langchain_core.tools import Tool
from langchain import hub
from langchain.agents import (create_react_agent,AgentExecutor)
from langchain.agents import AgentType, initialize_agent    
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from agents.tools import get_ytb_transcript,fetch_transcript_all
from langchain.prompts import PromptTemplate

load_dotenv()

def summ_agent(youtube_url:str,start_time:str, end_time:str):

    llm = ChatGroq(
                #model_name="llama3-70b-8192",
                model_name="llama-3.3-70b-versatile",
                temperature=0
                ) 
    
    tools_for_agent = [fetch_transcript_all, get_ytb_transcript]
    
    """tools_for_agent = [
        Tool(
            name="Get Youtube Transcript for a Segment",
            func=get_ytb_transcript,
            description="Please use this when you already have the full youtube transcript, otherwise it won't work. This tool is used to get the segment of the youtube video transcript. The output is a string. You will be provided with a list of transcript entries, a start time, and an end time. Select the correct segment using those values with the correct parameters. ",
        ),
        Tool(
            name="Get Full Youtube Transcription",
            func=fetch_transcript_all,
            description="Use this tool to get the full transcription of the youtube video. The output is a list of dictionaries with the keys: start, duration, text. The input is the youtube video url.",
        )]"""
                
    prompt="""You are a smart assistant with access to tools.

    Your task is to summarize the transcript of a YouTube video, but only for a specific segment (start and end time). You may need to:
    1. Fetch the full transcript.
    2. Extract just the segment between start and end.
    3. Summarize it.

    If needed, you can call multiple tools. You are allowed to use one tool to get data and another tool to use that data.

    Video URL: {youtube_url}
    Start Time: {start_time}
    End Time: {end_time}

    Output format:
    - Summary title
    - Important bullet points
"""

    prompt_template = PromptTemplate(
        input_variables=["youtube_url","start_time", "end_time"],
        template=prompt,
    )
    react_prompt= hub.pull("hwchase17/react")
    agent= create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    #agent_executor = initialize_agent(tools=tools_for_agent,llm=llm,agent=AgentType.OPENAI_MULTI_FUNCTIONS,verbose=True)
    result = agent_executor.invoke({"input": prompt_template.format_prompt(youtube_url=youtube_url,start_time=start_time,end_time=end_time).to_string()})
    return result
    
      