scores = {}

# 점수 입력 받기
for i in range(1, 9):
    scores[i] = int(input())

top_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
total_score = sum([value for key, value in top_scores])

top_problems = sorted([key for key, value in top_scores])

print(total_score)
print(' '.join(map(str, top_problems)))
