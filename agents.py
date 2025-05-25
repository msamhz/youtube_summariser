####################################
# Import necessary libraries
####################################

from crewai import Agent, Task, Crew, LLM
from tools import yt_tools, llm


#############################################
# Create a senior learning content researcher agent 
#############################################

# Original version with YouTube tools
senior_learning_content_researcher = Agent(
    role="Senior Learning Content Researcher",
    goal="Research and find the most relevant educational content for the given topic {topic} from YouTube channels to create helpful learning materials",
    verbose=True,
    memory=True,
    backstory="You are a senior learning content researcher with expertise in identifying the most valuable and educational content for self-study. \
        You excel at finding comprehensive YouTube videos on AI, Data Science, Machine Learning, and Gen AI topics that can be transformed into effective learning resources, summaries, and study guides.",
    tools=yt_tools,
    allow_delegation=True,
    llm=llm,
    max_execution_time=60,
    respect_context_window=True,  # 🔑 Default: auto-handle context limits
)

####################################
# Create a data science learning content creator agent
####################################

learning_content_creator = Agent(
    role="Data Science Learning Content Creator",
    goal="Create comprehensive learning materials including summaries, Q&A sessions, and concept maps for data science topics {topic} from Youtube Channel content",
    verbose=True,
    memory=True,
    backstory="You are an expert learning content creator specializing in data science education. You excel at breaking down complex AI, machine learning, and data science concepts into digestible learning materials. \
        Your expertise includes creating structured summaries, thoughtful Q&A sessions, and visual concept maps that help learners understand and retain knowledge effectively.",
    tools=yt_tools,
    allow_delegation=False,
    llm=llm,
)


####################################
