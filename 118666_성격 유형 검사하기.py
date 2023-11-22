def judge(results):
    answer = ''

    if results['R'] >= results['T']:
        answer += 'R'
    else:
        answer += 'T'

    if results['C'] >= results['F']:
        answer += 'C'
    else:
        answer += 'F'

    if results['J'] >= results['M']:
        answer += 'J'
    else:
        answer += 'M'

    if results['A'] >= results['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer


def solution(survey, choices):
    n = len(survey)

    results = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0, }

    first_scores = [3, 2, 1, 0, 0, 0, 0]
    second_scores = [0, 0, 0, 0, 1, 2, 3]

    for i in range(n):
        f, s = survey[i][0], survey[i][1]
        c = choices[i] - 1
        results[f] += first_scores[c]
        results[s] += second_scores[c]

    return judge(results)