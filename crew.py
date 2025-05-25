from crewai import Crew, Process, LLM
from agents import senior_learning_content_researcher, learning_content_creator
from tasks import research_task, content_summary_task, learning_task
from tools import llm

# forming a tech-focused crew with enhanced configurations 
crew = Crew(
    agents=[
        senior_learning_content_researcher, 
        learning_content_creator
        ]
    ,
    tasks=[content_summary_task,
           learning_task
           ]
    ,
    process=Process.sequential,
    cache=True,
    max_rpm=100,
    share_crew=True,
    verbose=True,
    llm = llm
)
# Start task execution 
result = crew.kickoff(
    inputs={
        "topic": "Large Language Models explained briefly"
    }   
)
# Print the result 
print(result)


