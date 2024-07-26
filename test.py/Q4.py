'''
[Question 4] = (40점, 부분점수 있음)
다른 추천 동영상 목록 API 데이터 videos와 본인의 실제 시청 기록 views 데이터가 주어질 때 다음 질문에 답하시오.
단, 비디오의 장르(카테고리)는 1~5까지의 자연수만 있다고 가정한다.

(1) 추천 동영상 목록 videos에서 몇 개의 동영상 데이터를 응답 받았는지 구하시오. (동영상 정보는 results) (10점)
(2) 내가 시청한 동영상(views)들의 평점의 평균을 구하시오. (10점)
(3) 내가 시청한 동영상(views)들 중 가장 많이 시청한 장르를 구하시오. (10점)
(4) 내가 가장 많이 시청한 장르 중 추천 비디오 데이터 베이스에서 평점이 가장 높은 동영상의 제목을 출력하시오. (10점)
'''

# 추천 동영상 목록
videos = {
    'response': 'Success',
    'current_page': 1,
    'results': [
        {'title': '갑', 'video_genre': 2, 'rating': 1.423},
        {'title': '을', 'video_genre': 3, 'rating': 5.225},
        {'title': '병', 'video_genre': 1, 'rating': 6.814},
        {'title': '정', 'video_genre': 2, 'rating': 7.137},
        {'title': '무', 'video_genre': 2, 'rating': 5.576},
        {'title': '기', 'video_genre': 3, 'rating': 6.754},
        {'title': '경', 'video_genre': 1, 'rating': 8.339},
        {'title': '신', 'video_genre': 3, 'rating': 9.127},
        {'title': '임', 'video_genre': 2, 'rating': 8.934},
        {'title': '계', 'video_genre': 1, 'rating': 5.147},
        {'title': '자', 'video_genre': 2, 'rating': 2.996},
        {'title': '축', 'video_genre': 2, 'rating': 3.842},
        {'title': '인', 'video_genre': 2, 'rating': 7.123},
        {'title': '묘', 'video_genre': 5, 'rating': 5.465},
        {'title': '진', 'video_genre': 2, 'rating': 8.846},
        {'title': '사', 'video_genre': 4, 'rating': 3.157},
        {'title': '오', 'video_genre': 3, 'rating': 8.752},
        {'title': '미', 'video_genre': 4, 'rating': 6.936},
        {'title': '신', 'video_genre': 2, 'rating': 9.998},
        {'title': '유', 'video_genre': 2, 'rating': 5.246},
        {'title': '술', 'video_genre': 2, 'rating': 2.502},
        {'title': '해', 'video_genre': 3, 'rating': 4.478},
    ]
}

# 내 시청기록 (title 제외)
views = [
    {'video_genre': 1, 'rating': 7.226},
    {'video_genre': 3, 'rating': 2.442},
    {'video_genre': 2, 'rating': 8.683},
    {'video_genre': 2, 'rating': 9.676},
    {'video_genre': 3, 'rating': 4.213},
    {'video_genre': 2, 'rating': 3.724},
    {'video_genre': 2, 'rating': 5.553},
    {'video_genre': 4, 'rating': 9.155},
    {'video_genre': 3, 'rating': 4.667},
    {'video_genre': 5, 'rating': 5.972},
    {'video_genre': 5, 'rating': 6.374},
    {'video_genre': 1, 'rating': 3.826},
    {'video_genre': 2, 'rating': 1.732},
    {'video_genre': 1, 'rating': 7.945},
    {'video_genre': 2, 'rating': 1.337},
]



## 로직
# 1번 풀이 #
print(len(videos['results']))


# 2번 풀이 #
total_rating = 0
total_views = len(views)
for view in views:
    total_rating += view['rating']
avg = total_rating/total_views
print(avg)


# 3번 풀이 #
view_count = []
for view in views:
    view_count.append(view['video_genre'])
# print(view_count)

max_genre = 0
for i in view_count:
    if view_count.count(i) > max_genre:
        max_genre = view_count.count(i)
        fav_genre = i
print(f'가장 많이 시청하신 장르 유형은 {fav_genre} 입니다.')


# 4번 풀이 #
videos['results'].sort(key=lambda x:-x['rating'])
# print(videos['results'])
top1 = videos['results'][:1]
for name in top1:
    print(f"평점이 가장 높은 동영상의 제목은 '{name['title']}'입니다.")

print("==========================문제를 똑바로 읽어라==================================")
fav_videos = []
for result in videos['results']:
    if result['video_genre'] == fav_genre:
        fav_videos.append(result)
# print(fav_videos)

fav_videos.sort(key=lambda x:-x['rating'])
top1 = fav_videos[:1]
print(top1)
for name in top1:
    print(name['title'])