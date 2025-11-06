# Python
from google import genai
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# API 키를 명시적으로 전달
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words."
)
print(response.text)