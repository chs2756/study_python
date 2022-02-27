dic = {3 : 'test', 'a' : 'ate'}

# Dic Key 값 List로 출력
key_list = list(dic.keys())
print(key_list)

# Dic key 값 검색하기 1
if 3 in key_list:
    print('3 is existed')

# Dic Key 값 검색하기 2
if 3 in dic: # 3 in dic is Ture
    print('a')

# dic 값 목록 List로 출력
value_list = list(dic.values())
print(value_list)

# dic 값 검색하기
if 'test' in value_list:
    print('test is existed in dic')



