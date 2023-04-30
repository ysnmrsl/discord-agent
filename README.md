# Discord Agent 🤖

Discord Agent is a Discord bot that serves as a versatile assistant, designed to provide assistance with a wide range of tasks and engage in natural-sounding conversations. It can answer questions by retrieving information from a pinecone database or by performing a google search, provide in-depth explanations, and discuss various topics. Discord Agent uses OpenAI's gpt-4 for reasoning and deciding on which action to take.

## Requirements 🔧

- Python 3.10
- A Pinecone database
- An OpenAI account
- A SerpAPI account
- A Discord bot token

## Installation 📦

1. Clone the repository:

```bash
git clone https://github.com/ysnmrsl/discord-agent.git
```

2. Change the working directory:

```bash
cd discord-agent
```

3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

- For Windows:

```bash
venv\Scripts\activate.bat
```

- For Linux/macOS:

```bash
source venv/bin/activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration ⚙️

1. Create a `.env` file in the root directory of the project.
2. Add the following environment variables in the `.env` file:

```bash
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
PINECONE_INDEX_NAME=your_pinecone_index_name
PINECONE_NAMESPACE=your_pinecone_namespace
```

Replace the values with your actual environment variables.

## Running the Bot 🚀

After completing the installation and configuration, run the `main.py` script:

```bash
python main.py
```

The bot should now be up and running, and you should see a message in the console indicating that it has logged in.

## Usage 💬

Discord Agent will automatically respond to messages in Discord when it is mentioned. It answers questions and engages in conversations in French. Discord Agent utilizes its own QA system based on your Pinecone database to answer questions and refers to Google Search when it cannot find a suitable answer.

## Contributing 🙌

If you'd like to contribute to this project, feel free to create a fork and submit a pull request.
