from agents.summarizing_agent import summ_agent
from agents.tools import fetch_transcript_all,timestamp_to_seconds,seconds_to_timestamp
import streamlit as st

if __name__=="__main__":
    
    # 🌟 Streamlit UI
    st.title("🎥 YouTube Transcript Summarizer")

    ytb_url = st.text_input("Enter YouTube Video URL")

    if ytb_url:
        try:
            transcript = fetch_transcript_all.invoke({"video_url": ytb_url})
            video_duration = int(transcript[-1]["start"] + transcript[-1]["duration"])
            st.info(f"Estimated video duration: {seconds_to_timestamp(video_duration)}")
            
            # User timestamp inputs
            col1, col2 = st.columns(2)
            with col1:
                start_ts = st.text_input("Start Time (MM:SS or HH:MM:SS)", value="00:00")
            with col2:
                end_ts = st.text_input("End Time (MM:SS or HH:MM:SS)", value="01:00")

            # Convert to seconds
            try:
                start_time = timestamp_to_seconds(start_ts)
                end_time = timestamp_to_seconds(end_ts)

                if start_time >= end_time:
                    st.error("⛔ End time must be greater than start time.")
                elif end_time > video_duration:
                    st.error("⛔ End time cannot exceed video duration.")    
            
                else:
                    if st.button("Get Summary"):
                        st.caption(f"Extracting transcript from {start_time}s to {end_time}s")
                        transcript = summ_agent(youtube_url= ytb_url,start_time=start_time, end_time=end_time)
                        st.success("Transcript segment fetched successfully!")
                        st.subheader("📝 Transcript Summary")
                        st.write(transcript["output"])
            except ValueError as e:
                st.error(f"❌ Invalid timestamp: {e}")
        except Exception as e:
            st.error(f"Error fetching transcript: {e}")