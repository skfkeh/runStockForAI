import requests

# Colab에서 "파일 → 노트북 공유" URL을 가져와서 수정
colab_url = "https://colab.research.google.com/drive/1xRykXVb3hQJFO1LpYI7U8FvuDrMV8D8g?usp=sharing"

# Colab을 직접 실행하는 방법은 제한적이므로, 
# Google Drive API 또는 nbconvert 실행을 추천

# 예: Colab에서 생성한 "실행용 링크" 호출
response = requests.get(colab_url)
if response.status_code == 200:
    print("Colab notebook triggered successfully.")
else:
    print("Failed to trigger notebook:", response.status_code)
