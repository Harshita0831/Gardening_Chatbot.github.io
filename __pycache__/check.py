import google.generativeai as genai
import config

# Configure API key
genai.configure(api_key=config.GEMINI_API_KEY)

# List available models
models = genai.list_models()

for model in models:
    print(model.name)
