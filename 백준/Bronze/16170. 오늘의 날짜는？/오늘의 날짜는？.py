from datetime import datetime, timezone

# 현재 시각을 UTC로 가져옵니다.
now_utc = datetime.now(timezone.utc)

# 연도, 월, 일을 순서대로 출력합니다.
print(now_utc.year)
print(f"{now_utc.month:02d}")
print(f"{now_utc.day:02d}")
