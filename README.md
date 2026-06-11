# Gemini Chatbot (Python)

A simple terminal chatbot using Google Gemini.

## Setup
1. Create a virtual environment (optional but recommended):
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bat
   pip install google-generativeai python-dotenv
   ```
3. Add a `.env` file in the same folder:
   ```ini
   GEMINI_API_KEY=your_api_key_here
   ```


## Run
```bat
python "chat bot.py"
```

## Commands
- `exit` — quit
- `clear` — clear conversation memory

