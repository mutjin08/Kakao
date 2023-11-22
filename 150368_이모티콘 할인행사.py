from itertools import product


def solution(users, emoticons):
    answer = [0, 0]  # 총 가입자수, 총 매출액

    n, m = len(users), len(emoticons)

    # 각 케이스에 대해
    for discounts in product([10, 20, 30, 40], repeat=m):
        temp_answer = [0, 0]

        # 각 유저에 대해
        for min_discount, min_total in users:
            pay = 0

            # 각 이모티콘에 대해
            for i in range(m):
                if discounts[i] >= min_discount:
                    pay += emoticons[i] * (100 - discounts[i]) // 100
            if pay >= min_total:
                temp_answer[0] += 1
                pay = 0
            temp_answer[1] += pay

        if answer[0] > temp_answer[0]:
            continue
        if answer[0] == temp_answer[0] and answer[1] > temp_answer[1]:
            continue

        answer[0], answer[1] = temp_answer[0], temp_answer[1]

    return answer