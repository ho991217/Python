"""
[[60, 50], [30, 70], [60, 30], [80, 40]]
"""

def solution(sizes):
    sizes = [sorted(i) for i in sizes]
    hori, vert = [i[0] for i in sizes], [i[1] for i in sizes]

    return max(hori) * max(vert)


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))