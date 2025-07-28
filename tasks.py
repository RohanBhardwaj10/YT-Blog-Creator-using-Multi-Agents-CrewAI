from crewai import Task
from agents import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description=(
        "Identify the video related to the topic: {topic}. "
        "Gather detailed insights from the channel's video content."
    ),
    expected_output="A comprehensive 3-paragraph report on the topic {topic} from the channel's videos.",
    agent=blog_researcher,
)

write_task = Task(
    description=(
        "Based on the research info about {topic}, summarize the findings and create a blog-ready content."
    ),
    expected_output="A well-structured blog post summarizing the video content on {topic}.",
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)
