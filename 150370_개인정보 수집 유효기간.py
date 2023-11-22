def string_to_int(date):
    y, m, d = map(int, date.split("."))
    return (y - 2000) * 12 * 28 + m * 28 + d


def solution(today, terms, privacies):
    answer = []
    today = string_to_int(today)

    myterms = {}
    for term in terms:
        category, month = term.split()
        myterms[category] = int(month) * 28

    for i in range(len(privacies)):
        date, category = privacies[i].split()
        date = string_to_int(date)
        if today >= date + myterms[category]:
            answer.append(i + 1)

    answer.sort()
    return answer