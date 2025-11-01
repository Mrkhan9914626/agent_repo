# Helpful Assistant

This repository contains a Python script (`main.py`) that demonstrates how to use the OpenAI API to create and interact with a helpful assistant. The script initializes an assistant with a code interpreter tool, creates a conversation thread, adds a user message, and then runs the assistant to process the query.

## Getting Started

To run this script, you will need to have the OpenAI Python library installed and your OpenAI API key configured.

### Prerequisites

- Python 3.x
- OpenAI Python library (`pip install openai`)
- OpenAI API Key

### Usage

1.  **Set up your OpenAI API Key:**
    Make sure your OpenAI API key is set as an environment variable or configured in your application.

2.  **Run the script:**
    ```bash
    python main.py
    ```

## Script Details

The `main.py` script performs the following actions:

-   **Assistant Creation:** Creates an OpenAI assistant named "Helpful assistant" with instructions to assist users with general queries and enables the `code_interpreter` tool.
-   **Thread Management:** Creates a new conversation thread.
-   **Message Addition:** Adds a user message to the newly created thread.
-   **Assistant Run:** Executes the assistant on the thread, providing specific instructions to address the user as "Mujeeb ur Rehman."

## Files

-   `main.py`: The core Python script for interacting with the OpenAI assistant.
-   `readme.md`: This file, providing an overview and instructions for the project.
