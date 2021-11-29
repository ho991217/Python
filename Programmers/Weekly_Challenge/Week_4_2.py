table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]


languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

def solution(table, languages, preference):
    answer = ''

    for i in range(len(table)): table[i] = table[i].split(' ')

    print(table)


    return answer


solution(table, languages, preference)