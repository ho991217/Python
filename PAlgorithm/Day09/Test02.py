# 문자열을 입력받아 문자열 거꾸로 출력

# Stack 이용

class Stack:
    def __init__(self, text):
        self.text = text
        print(self.text)
        print(self.text[4])
        self.data = []


    def revTXT(self):
        print(len(self.text))
        for i in range(len(self.text), 0, -1):
            self.data.append(self.text[i - 1])

    def printTXT(self):
        print(self.data)



st = Stack('Hello')
st.revTXT()
st.printTXT()