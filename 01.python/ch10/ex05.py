dic ={
    'boy' : '소년',
    'school' : '학교',
    'book' : '책',

}

dic['boy'] = '남자아이' # key가 존재하면 수정
dic['girl'] = '소녀'    # key가 존재하지 않으면 추가
del dic['book']     # 기존 키에 해당하는 element 삭제

print(dic)

# del dic['abc']  # 존재하지 않는 key에 대한 삭제는 에러

del dic.get['book']