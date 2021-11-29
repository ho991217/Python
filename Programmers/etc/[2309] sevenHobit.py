h = [int(input()) for i in range(9)]

tot = sum(h)
for i in h:
    for j in h:
        if i != j:
            if tot - (i + j) == 100:
                h.remove(i)
                h.remove(j)
                h.sort()
                for i in h:
                    print(i)
                break


    # if len(h) < 9:
    #     break
