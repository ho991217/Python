# 리스트 자료형 시간 복잡도

# index -> ls[index] 인덱스로 값 찾기 : 시간 복잡도 O(1)
# Store -> ls[index] = 0 : 인덱스로 데이터 저장 O(1)
# length -> len(ls) O(1)
# append -> ls.append(index) O(1)

# Slicing -> ls[a:b] -> O(nlog) : 잘라내는 리스트의 길이가 클 수록 오래 걸림
# insert -> ls.insert(index, value) : O(n) -> 중간에 삽입되면 그 뒤 인덱스들이 밀리기 때문에 반복이 들어감
# delete -> ls.remove(index) O(n) -> 값을 찾는데 반복이 들어가기 때문에
# sorting -> ls.sort() O(nlogn)

# --------------------------------------

# 딕셔너리 자료형 시간 복잡도  -> 리스트보다 대부분 빠름
# 값 저장 -> O(1)
# delete -> O(1)
# 대부분 함수 O(1)

# for k in dic:  -> O(n)

# List 삽입, 제거, 탐색 포함여부, 확인, 대부분 O(n)
# 딕셔너리, Set 삽입, 제거, 탐색, 포함 여부 확인 O(1)

