# from openai import OpenAI
# from settings import *
# import os

# # Configuration Parameters
# temperature = 0.9
# top_p = 0.9
# max_tokens = 2048
# stream = True
# llm_name = "Meta-Llama"

# monster_client = OpenAI(
#     base_url="https://llm.monsterapi.ai/v1/",
#     api_key=str(MONSTER_API_KEY)
# )

# monster_ai_model_name = {
#     "Google-Gemma": "google/gemma-2-9b-it",
#     "Mistral": "mistralai/Mistral-7B-Instruct-v0.2",
#     "Microsoft-Phi": "microsoft/Phi-3-mini-4k-instruct",
#     "Meta-Llama": "meta-llama/Meta-Llama-3.1-8B-Instruct",
# }

# # Financial Data Input
# message = [
#     {"role": "system", "content": "You are a financial assistant specializing in data analysis and forecasting."},
#     {"role": "user", "content": "Here is the financial data for Q1 2024:\n\nRevenue: $1,200,000\nExpenses: $800,000\nNet Profit: $400,000\nCash Flow: $350,000\n\nCan you provide insights on how to improve profitability in Q2 2024?"}
# ]

# response = monster_client.chat.completions.create(
#     model=monster_ai_model_name[llm_name],
#     messages=message,
#     temperature=temperature,
#     top_p=top_p,
#     max_tokens=max_tokens,
#     stream=stream
# )

# # Process and Print the Generated Text
# generated_text = ""
# for chunk in response:
#     if chunk.choices[0].delta.content is not None:
#         generated_text += chunk.choices[0].delta.content

# print(generated_text)


from openai import OpenAI
from settings import *
import os

# Configuration Parameters
temperature = 0.9
top_p = 0.9
max_tokens = 2048
stream = True
llm_name = "Meta-Llama"

monster_client = OpenAI(
    base_url="https://llm.monsterapi.ai/v1/",
    api_key=str(MONSTER_API_KEY)
)

monster_ai_model_name = {
    "Google-Gemma": "google/gemma-2-9b-it",
    "Mistral": "mistralai/Mistral-7B-Instruct-v0.2",
    "Microsoft-Phi": "microsoft/Phi-3-mini-4k-instruct",
    "Meta-Llama": "meta-llama/Meta-Llama-3.1-8B-Instruct",
}

# Function to determine the mode of operation
def determine_mode(user_query):
    keywords = {
        "personal finance": ["investment", "expenses", "budget", "savings"],
        "student budgeting": ["pocket money", "track spending", "cashback", "student discounts"],
        "stock market": ["stock trading", "financial terms", "market trends", "P/E ratio", "dividends"]
    }
    
    for mode, mode_keywords in keywords.items():
        if any(keyword in user_query.lower() for keyword in mode_keywords):
            return mode
    return None

# User Input
user_query = input("Enter your question: ")

mode = determine_mode(user_query)

if mode:
    # Define system prompts based on the mode
    system_prompt = {
        "personal finance": "You are a financial mentor specializing in personal finance. Provide advice on investments, expense tracking, and budgeting.",
        "student budgeting": "You are a student budget mentor. Help manage pocket money, track expenses, and suggest discounts or cashback opportunities.",
        "stock market": "You are a stock market mentor. Explain trading basics, financial terms, and market trends to beginners."
    }

    # Messages to feed the model
    message = [
        {"role": "system", "content": system_prompt[mode]},
        {"role": "user", "content": user_query}
    ]

    # Get AI response
    response = monster_client.chat.completions.create(
        model=monster_ai_model_name[llm_name],
        messages=message,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        stream=stream
    )

    # Process and Print the Generated Text
    generated_text = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            generated_text += chunk.choices[0].delta.content

    print(f"Mode: {mode.capitalize()}")
    print("AI Response:")
    print(generated_text)

else:
    print("This AI specializes in financial mentoring. Please ask a question related to personal finance, student budgeting, or the stock market.")
