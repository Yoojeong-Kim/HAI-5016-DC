# Python
from google import genai
from dotenv import load_dotenv
import os
from datetime import date

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# API 키 확인
if not api_key:
    raise RuntimeError("GEMINI_API_KEY가 설정되어 있지 않습니다. .env 파일을 확인하세요.")

# API 키를 명시적으로 전달
client = genai.Client(api_key=api_key)

# 오늘 날짜를 가져와서 프롬프트에 포함
today = date.today().isoformat()  # YYYY-MM-DD
prompt = f"As of {today}, how many days until Christmas?"

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
)
print(response.text)