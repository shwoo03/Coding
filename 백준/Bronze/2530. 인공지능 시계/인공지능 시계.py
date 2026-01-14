# 입력: 시, 분, 초 및 조리 시간(초)
# 출력: 종료되는 시각 시, 분, 초

hour, minute, second = map(int, input().split())
cooking_time = int(input())

# 1. 초 단위로 변환 
total_seconds = hour * 3600 + minute * 60 + second + cooking_time

# 2. 24시간 형식으로 변환
total_seconds %= 86400  # 하루는 86400초
end_hour = total_seconds // 3600
total_seconds %= 3600
end_minute = total_seconds // 60
end_second = total_seconds % 60

# 3. 결과 출력
print(end_hour, end_minute, end_second)