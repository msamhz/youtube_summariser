from crewai_tools import YoutubeChannelSearchTool
from crewai import LLM

# Instatiate one model for the crew
llm=LLM(
        model="ollama/deepseek-r1",  # Using deepseek for better performance
        base_url="http://localhost:11434",
        temperature=0.3  # Lower temperature for more focused responses
    )

# Initialize the YoutubeSearchTool with deepseek-r1 configuration
yt_tools = [YoutubeChannelSearchTool(
    '@3blue1brown',
    config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="deepseek-r1",
                base_url="http://localhost:11434",
                temperature=0.1,  # Lower temperature for more focused responses
                top_p=0.5,  # Balanced token selection
                stream=True,  # Enable streaming for faster responses
            ),
        ),
        embedder=dict(
            provider="ollama",
            config=dict(
                model="deepseek-r1",
                base_url="http://localhost:11434",
            ),
        ),
    )
)]