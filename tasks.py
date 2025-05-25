from crewai import Task
from tools import yt_tools
from agents import simple_assistant, senior_learning_content_researcher, learning_content_creator

# YouTube Content Analysis Task with Educational Focus
content_summary_task = Task(
    description=(
        "For the topic '{topic}', analyze the YouTube channel content and teach it as an experienced tutor: \n"
        "1. Start with a beginner-friendly introduction to the concept\n"
        "2. Break down the main concepts using simple analogies and real-world examples\n"
        "3. Analyze and explain the content from the video, highlighting:\n"
           "   - Core concepts and their relationships\n"
           "   - Key insights and their practical significance\n"
           "   - Technical details explained in simple terms\n"
        "4. Provide your own insights and additional examples to reinforce learning\n"
        "5. Include 'Think About This' questions to encourage deeper understanding\n"
        "6. Add a 'Common Misconceptions' section to clarify potential confusion points\n"
        "7. Conclude with a 'Next Steps' section for further learning"
    ),
    expected_output=(
        "A comprehensive learning guide containing:\n"
        "- Curated summary of best explanations\n"
        "- Synthesized introduction for beginners\n"
        "- Multiple perspectives and teaching approaches\n"
        "- Diverse examples and analogies\n"
        "- Interactive elements from various sources\n"
        "- Common misconceptions and their clarifications\n"
        "- Recommended learning pathway with best resources\n"
        "- References to specific helpful timestamps in videos"
    ),
    tools=yt_tools,
    agent=senior_learning_content_researcher
)

# Learning Task

learning_task = Task(
    description="Create comprehensive learning materials including summaries, Q&A sessions, and concept maps for data science topics {topic}",
    expected_output="Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog",
    tools = yt_tools,
    agent = learning_content_creator,
    output_file="learning_content.md"
)
