from openai import OpenAI
from dotenv import load_dotenv
import os

from tools import search_company
from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def run_agent(user_query):

    try:

        # Extract company name
        company_name = (
            user_query
            .replace("Research", "")
            .split("and")[0]
            .strip()
        )

        print(f"\nResearching: {company_name}\n")

        # Tool call
        research_data = search_company(company_name)

        if len(research_data) < 50:
            return "Company information not found."

        # Final LLM prompt
        final_prompt = f"""
        USER QUERY:
        {user_query}

        RESEARCH DATA:
        {research_data}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": final_prompt
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"