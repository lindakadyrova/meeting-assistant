# Privacy-Oriented Meeting Assistant

A privacy-oriented meeting assistant for automatic meeting transcription, summarization, and action item extraction.

## About

Meetings often contain important information, decisions, and tasks. However, responsibilities and deadlines can easily get lost after a meeting.

This project aims to develop a meeting assistant that processes meeting recordings locally and automatically extracts relevant information.

The system uses local speech-to-text processing with Whisper and compares three approaches for information extraction:

1. **Rule-based approach** – Extracting information using predefined rules and patterns.
2. **LLM-based approach** – Using a locally running Large Language Model (LLM) to identify and extract information.
3. **Hybrid approach** – Combining rule-based methods with an LLM.

The extracted information focuses on:

- Tasks
- Responsible persons
- Deadlines

## Privacy

Privacy is a central aspect of this project. Audio processing and information extraction are designed to run locally, avoiding external cloud-based processing.

## Project Structure

```text
meeting-assistant/
├── data/          # Input data and transcripts
├── src/           # Source code
├── tests/         # Tests
├── docs/          # Project documentation
├── evaluation/    # Evaluation and comparison of approaches
├── README.md
├── requirements.txt
└── .gitignore
```

## Technology Stack

- **Python** – Main programming language
- **faster-whisper** – Local speech-to-text transcription
- **SQLite** – Local data storage (planned)
- **spaCy** – Rule-based information extraction (planned)
- **Ollama** – Local LLM execution (planned)

## Installation

### Prerequisites
- Python 3.12

### Setup

```bash
# Clone repository
git clone https://github.com/lindakadyrova/meeting-assistant.git

# Navigate into project
cd meeting-assistant

# Create virtual environment
py -3.12 -m venv .venv

# Activate virtual environment (Windows Git Bash)
source .venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt
```

The virtual environment is stored locally in `.venv/` and is excluded from version control.

## Project Status

Work in progress – Winter Semester 2026/27.

The initial Python environment and local Whisper model have been set up. Further implementation and evaluation of the three extraction approaches are ongoing.

## Author

[Linda Kadyrova](https://github.com/lindakadyrova)