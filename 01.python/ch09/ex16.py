# 리스트와 검색 값을 인수로 받아서,
# 검색 값이 있는 해당 값이 있는 인덱스를 반환하고,
# 검색 값이 없으면 -1을 리턴하는 find_value() 함수를 작성하세요.

# 순차 검색
def find_value(datas, value):
    ix = 0
    for data in datas:
        if data == value:  #리스트의 요소값이 검색값과 일치하면
           #ix ? data의 index
           return ix
        ix += 1
    
    # for 루프를 다 돌았다는 의미 ---< 찾는 값이 리스트에 없음
    return -1  # 데이터가 없으면 -1 리턴, -1의 뜻 인덱스가 가질 수 없는 수


score = [88,95,70,100,99,88,78,50]

ix = find_value(score, 99)
print(f'88의 인덱스 {ix}')



