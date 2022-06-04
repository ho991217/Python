class Category:
    def __init__(self):
        self.category = [
            {"title": "홈", "type": "path", "subPath": [
                {"title": "패션의류 / 잡화", "type": "path", "subPath": []},
                {"title": "출산 / 유아동", "type": "path", "subPath": []},
                {"title": "주방용품", "type": "path", "subPath": [
                    {"title": "냄비 / 후라이팬", "type": "path", "subPath": [
                        {"title": "A후라이팬", "type": "merch", "state": 0, "location": "a-1"},
                        {"title": "B후라이팬", "type": "merch", "state": 10, "location": "a-2"},
                    ]},
                    {"title": "그릇 / 홈세트", "type": "path", "subPath": []},
                    {"title": "밀폐저장 / 도시락", "type": "path", "subPath": []},
                    {"title": "수저 / 커트러리", "type": "path", "subPath": []}
                ]},
                {"title": "홈인테리어", "type": "path", "subPath": []},
            ]}
        ]

        self.currentCategory = self.category[0]

    def getCategory(self):
        print("현재 카테고리 : " + self.currentCategory["title"])
        for i in range(len(self.currentCategory["subPath"])):
            print(str(i + 1) + " : " + self.currentCategory["subPath"][i]["title"])

    def moveCategory(self, nav):
        self.currentCategory = self.currentCategory["subPath"][nav - 1]
        if self.currentCategory["type"] == "path":
            pass
        elif self.currentCategory["type"] == "merch":
            print("상품 정보 : " + self.currentCategory["title"])
            if self.currentCategory["state"] <= 0:
                print("이 상품은 품절입니다.")
            else:
                print("상품 재고 : " + str(self.currentCategory["state"]))
            print("상품 위치 : " + self.currentCategory["location"])
            self.currentCategory = self.category[0]



c = Category()

while True:
    c.getCategory()
    command = int(input("카테고리를 입력하세요: "))
    c.moveCategory(command)
    print()