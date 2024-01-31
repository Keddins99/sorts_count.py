def bubble_count(a_list):
    comparisons = 0
    exchanges = 0
    for i in range(len(a_list)):
        for j in range(len(a_list) - 1 - i):
            comparisons += 1
            if a_list[j] > a_list[j + 1]:
                exchanges += 1
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return (comparisons, exchanges)

def insertion_count(a_list):
    comparisons = 0
    exchanges = 0
    for i in range(1, len(a_list)):
        value = a_list[i]
        pos = i
        while pos > 0 and a_list[pos - 1] > value:
            comparisons += 1
            exchanges += 1
            a_list[pos] = a_list[pos - 1]
            pos -= 1
        comparisons += 1
        a_list[pos] = value
    return (comparisons, exchanges)
