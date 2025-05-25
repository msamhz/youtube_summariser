# YouTube Educational Content Summarizer

An AI-powered application that analyzes and creates educational summaries from YouTube content, specifically focused on 3Blue1Brown's channel. The app uses CrewAI with local Ollama models (deepseek-r1) to provide in-depth analysis and learning materials.

## Features

- **Content Analysis**: Analyzes YouTube videos with an educational focus
- **Beginner-Friendly Summaries**: Creates accessible explanations of complex topics
- **Interactive Learning Elements**: Includes "Think About This" questions and exercises
- **Misconception Clarification**: Addresses common misunderstandings
- **Learning Pathways**: Suggests next steps for continued learning
- **Local AI Processing**: Uses Ollama with deepseek-r1 model for fast, private analysis

## Prerequisites

- Python 3.8+
- Ollama installed and running locally
- deepseek-r1 model pulled in Ollama

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd youtube_summariser
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure Ollama is running with deepseek-r1:
```bash
ollama pull deepseek-r1
```

## Configuration

The application is configured to use:
- Ollama's deepseek-r1 model for text generation
- Temperature of 0.3 for focused responses
- 3Blue1Brown's YouTube channel as the primary content source

Output is saved to `learning_content.md` and includes:
- Detailed topic summaries
- Key concepts and relationships
- Practical examples and analogies
- Interactive learning elements
- Common misconceptions and clarifications
- Next steps for learning

## Project Structure

- `agents.py`: Defines AI agents with specific roles
- `tools.py`: Configures YouTube content analysis tools
- `tasks.py`: Defines content analysis and learning material creation tasks
- `crew.py`: Orchestrates the workflow between agents and tasks
