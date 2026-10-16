# SparshGPT

A small Streamlit chat interface for an OpenAI-compatible chat-completions service. The app sends a prompt to the configured model and displays its response.

**Live app:** [sparshgpt.streamlit.app](https://sparshgpt.streamlit.app/)

## Run locally

```bash
git clone https://github.com/sparsh0106/SparshGPT.git
cd SparshGPT
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create a local `.env` file in the project root:

```dotenv
api_key=your_api_key
```

The application reads the `api_key` environment variable through `python-dotenv`. Keep the real key out of Git and do not share it in screenshots or logs.

Start the app:

```bash
streamlit run main.py
```

## Notes

- The chat model and compatible API endpoint are configured in `main.py`.
- Prompts are sent to the configured service. Avoid submitting passwords, private records, or other sensitive information.
- This is a lightweight personal project, not a production chatbot or a source of professional advice.
