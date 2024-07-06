# chatBot_Microsoft_phi3

## Overview

This project implements a basic bot using the Microsoft Phi-3-mini-128k-instruct model from the Hugging Face Transformers library. The bot interacts with users by asking for their name, email, and company, and stores this information in a simple in-memory structure (Python dictionary). The bot is built using Streamlit for the frontend interface.

## Prerequisites

- **Python**: Ensure Python 3.7 or higher is installed.
- **GPU**: A good GPU is required to run the model efficiently.

## Installation

1. **Clone the repository:**
  ```sh
  git clone https://github.com/your-repo/chatBot_Microsoft_phi3.git
  cd chatBot_Microsoft_phi3
  ```

2. **Create and activate a virtual environment:**

  ```sh
  python -m venv venv
  source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
  ```

3. **Install the required packages:**

  ```sh
  pip install -r requirements.txt
  ```

## Usage

1. **Run the Streamlit app:**

  ```sh
  streamlit run app.py
  ```

2. Interact with the bot:
  -Enter your query in the input field.
  -Click on the "Result" button to see the bot's response and provide the requested information.


## Notes

  -Ensure you have a valid Hugging Face token set in the environment variable HF_TOKEN before running    the code.
  -The bot requires a good GPU to run efficiently due to the computational load of the LLM.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
