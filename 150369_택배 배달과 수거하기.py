def solution(cap, n, deliveries, pickups):
    answer = 0
    trunk = [0, 0]

    for i in range(n - 1, -1, -1):
        trunk[0] += deliveries[i]
        trunk[1] += pickups[i]

        while trunk[0] > 0 or trunk[1] > 0:
            trunk[0] -= cap
            trunk[1] -= cap

            answer += (i + 1) * 2
    return answer