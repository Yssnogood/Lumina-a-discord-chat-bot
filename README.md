# Lumina Discord Bot

This project was doone to experiment with a LLM and see if I could use a discord interface to interact with it. 

Lumina is a Discord bot designed to interact with users, manage conversations, and provide engaging experiences through AI-driven responses. It leverages the `discord.py` library, SQLite for database management, and a language model for AI responses.

Want to create and use your own model, check that video : 
```
https://youtu.be/gyX-N-ppU3E?si=sDroAVpdygco8bV1 
```

## Features

- **Dynamic Command Handling**: Automatically loads command extensions from the `BotCommands` directory.
- **Conversation Tracking**: Maintains a history of conversations using SQLite.
- **AI-Powered Responses**: Communicates with users using the `Lumina-llama` language model.
- **Random Prompt Generation**: Sends random prompts to users for engaging interactions.
- **Automated Notifications**: Periodically sends messages to users or notifies all users who interacted with the bot.

## Prerequisites

- Python 3.8+
- A Discord bot token
- `discord.py` library
- SQLite3
- `ollama` library

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   Run the bot to initialize the SQLite database (`memory.db`) automatically.

4. Add your Discord bot token in the `config.py` file:
   ```python
   APIKEY = 'SUPER-SECRET-DISCORD-KEY-GOES-HERE'
   ```

5. Create a `prompt.json` file in the project directory with random prompt data. Example:
   ```json
   [
       {"role": "assistant", "content": "What's your favorite hobby?"},
       {"role": "assistant", "content": "Share a fun fact about yourself!"}
   ]
   ```

## File Structure

```
project/
|-- BotCommands/
|   |-- <command_modules>.py
|-- memory.db
|-- config.py
|-- main.py
|-- BDD.py
|-- utils.py
|-- README.md
```

- **`main.py`**: Entry point for the bot.
- **`BDD.py`**: Handles database interactions for conversation storage and retrieval.
- **`BotCommands/`**: Contains command modules dynamically loaded by the bot.
- **`prompt.json`**: Stores random prompts used for interactions.
- **`config.py`**: Stores the Discord API token.

## Commands

### General
- `!ping`: Responds with "Pong!" to verify the bot's status.

### AI Interaction
- `!t <message>`: Engage in a conversation with Lumina.

### Admin Commands
- `!senddmTo`: Sends a message to a random user who has interacted with the bot.
- `!notifyall`: Sends a message to all users who have interacted with the bot.

## Database Structure

### Table: `memory`
| Column       | Type    | Description                     |
|--------------|---------|---------------------------------|
| `id`         | INTEGER | Primary key                    |
| `user_id`    | TEXT    | Discord user ID                |
| `user_msg`   | TEXT    | Message sent by the user       |
| `ia_answer`  | TEXT    | Response from the AI assistant |
| `date`       | DATETIME | Timestamp of the interaction   |

## Running the Bot

Start the bot by running the `main.py` script:
```bash
python main.py
```

The bot will:
- Load command modules from the `BotCommands` directory.
- Connect to Discord using the token provided in `config.py`.
- Begin listening for user interactions and sending automated notifications.

## Contributions

Feel free to submit issues or pull requests to improve the bot.

## License

This project is licensed under the MIT License.
