import streamlit as st
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from tools import get_youtube_tool

st.set_page_config(page_title="AI Blog Generator", page_icon="📝", layout="centered")
st.title("YT Blog Generator using Crew AI")

channel_handle = st.text_input("Enter YouTube channel handle :", placeholder="@xyz")
topic = st.text_input("Enter your blog topic:", placeholder="e.g., AI vs ML vs DL vs Data Science")

if st.button("Generate Blog"):
    if topic.strip():
        with st.spinner("Generating blog..."):
            yt_tool = get_youtube_tool(channel_handle)

            crew = Crew(
                agents=[blog_researcher, blog_writer],
                tasks=[research_task, write_task],
                process=Process.sequential,
                memory=True,
                cache=True,
                tools=[yt_tool] if yt_tool else []
            )
            result = crew.kickoff(inputs={'topic': topic})
        
        st.subheader("Generated Blog:")
        st.write(result)
    else:
        st.warning("please enter the topic ")






