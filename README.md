---
license: apache-2.0
title: YT_Blog_MultiAgent
sdk: streamlit
emoji: 📚
colorFrom: green
colorTo: yellow
short_description: App using crewai multiagents to create blog of YT vid
---
# YT-Blog-Creator-using-Multi-Agents-CrewAI
**Overview**
The YT Blog Generator is a Streamlit-based application that uses CrewAI multi-agent architecture to research content from a specified YouTube channel and generate well-structured blog posts.
It employs multiple AI agents, each with a defined role (researcher and writer), to collaboratively gather information and produce high-quality blog content. 
**Link : https://huggingface.co/spaces/RohanBhardwaj10/MultiAgent_YT_Blog**
## Features
Multi-Agent System: Separate agents for researching video content and writing blog posts.

YouTube Channel Integration: Fetches video transcripts and insights from any specified YouTube channel.

Dynamic User Input: Enter your desired blog topic and YouTube channel handle.

Streamlit UI: Simple, user-friendly interface for generating blogs instantly.

Extensible Design: Easily add more agents or tasks to improve functionality.

## Tech Stack
Python 3.9+

CrewAI (multi-agent framework)

Streamlit (UI framework)

yt_dlp (YouTube video loader)

youtube-transcript-api (fetch video transcripts)

OpenAI GPT-4 (language model for agents)

## Installation
Clone the repository


git clone https://github.com/your-username/yt-blog-generator.git
cd yt-blog-generator

**Create and activate a virtual environment**
conda create -n crewai_env python=3.9
conda activate crewai_env
Install dependencies

pip install -r requirements.txt
Install additional required packages


pip install yt_dlp==2023.11.14 youtube-transcript-api==0.6.1
Set up environment variables
Create a .env file and add:

OPENAI_API_KEY=your_openai_api_key

## Project Structure


├── agents.py          # Defines multi-agents (researcher & writer)
├── tasks.py           # Defines tasks assigned to agents
├── tools.py           # Tool setup (YouTube channel search)
├── app.py             # Streamlit app entry point
├── crew.py            # Crew setup and execution
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
