from collections import deque


def solution(queue1, queue2):
    answer = 0

    target = (sum(queue1) + sum(queue2)) // 2
    q1, q2 = deque(queue1), deque(queue2)

    s1 = sum(q1)
    while target != s1:
        if s1 > target:
            item = q1.popleft()
            s1 -= item
        elif s1 < target:
            item = q2.popleft()
            s1 += item
            q1.append(item)

        if not q2:
            return -1
        answer += 1
    return answer