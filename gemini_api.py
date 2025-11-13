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

# 현재 세션의 대화 기록 (메모리)
conversation_history = []

def show_recent_history(count=3):
    """최근 대화 기록 표시"""
    recent = conversation_history[-count:]
    if recent:
        print("\n📝 이번 세션의 질문들:")
        for i, question in enumerate(recent, 1):
            print(f"  {i}. {question[:60]}...")
        print()

print("🤖 Gemini API 채팅 시작 (종료하려면 'exit' 입력)\n")

# 사용자 입력을 받고 모델에 전송하는 루프
while True:
    user_input = input("당신의 질문을 입력하세요: ").strip()
    if user_input.lower() == 'exit':
        print("대화를 종료합니다.")
        break
    
    if not user_input:
        print("⚠️  빈 입력입니다. 다시 시도해주세요.\n")
        continue
    
    # 대화 기록에 저장
    conversation_history.append(user_input)
    
    # API에 요청
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_input
    )
    
    print(f"\n🤖 응답:\n{response.text}\n")
    
    # 최근 기록 표시
    show_recent_history()
