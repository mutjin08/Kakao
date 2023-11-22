def solution(alp, cop, problems):
    INF = int(1e9)

    max_alp_req, max_cop_req = 0, 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp_req = max(max_alp_req, alp_req)
        max_cop_req = max(max_cop_req, cop_req)

    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)

    dp = [[INF for _ in range(max_cop_req + 1)] for _ in range(max_alp_req + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):

            if i + 1 <= max_alp_req:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)

            if j + 1 <= max_cop_req:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp_req)
                    new_cop = min(j + cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[max_alp_req][max_cop_req]