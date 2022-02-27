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

''' https://yunaaaas.tistory.com/46 '''

#[] 기호 사용해 원소 가져오기

dict = {'하이': 300, '헬로': 180, 3: 5}
dict['헬로'] # 180

# get 메소드를 아용해 원소 가져오기 1
# 딕셔너리에 해당 key가 없을때 Key Error 를 내는 대신, 특정한 값을 가져온다.

dict = {'하이': 300, '헬로': 180}
dict.get('동동', 0) # 0

# get 메소드를 아용해 원소 가져오기 2
# 물론, 딕셔너리에 해당 key가 있는 경우 대응하는 value를 가져온다.

dict = {'하이': 300, '헬로': 180}
dict.get('헬로', 0) # 180

# 값 집어넣기

dict = {'김철수': 300, 'Anna': 180}
dict['홍길동'] = 100
dict #{'Anna': 180, '김철수': 300, '홍길동': 100}

# 값 수정하기1

dict = {'김철수': 300, 'Anna': 180}
dict['김철수'] = 500
dict # {'Anna': 180, '김철수': 500}

# 값 수정하기2

dict = {'김철수': 300, 'Anna': 180}
dict['김철수'] += 500
dict # {'Anna': 180, '김철수': 800}

# del 이용하기 - 키가 있는 경우
dict = {'김철수': 300, 'Anna': 180}
del dict['김철수']

dict #{'Anna': 180}

# del 이용하기 - 키가 없는 경우 raise KeyError
my_dict = {'김철수': 300, 'Anna': 180}
del my_dict['홍길동']
'''
keyError 발생!
'''

# pop 이용하기 - 키가 있는 경우 대응하는 value 리턴
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.pop('김철수', 180) # 300

# pop 이용하기 - 키가 없는 경우 대응하는 default 리턴
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.pop('홍길동', 180) # 180

# key로만 순회
dict = {'김철수': 300, 'Anna': 180}
for key in dict:
    print(key)
    # 이 경우 value를 찾고 싶으면 dict[key] 와 같이 접근을 따로 해주어야.

'''
김철수
Anna
'''

# key-value 동시 순회

dict = {'김철수': 300, 'Anna': 180}
for key, value in dict.items():
    print(key, value)

'''
김철수 300
Anna 180
'''

# 특정 Key 가 딕셔너리에 있는지 조회
dict = {'김철수': 300, 'Anna': 180}
print("김철수" in dict) #True
print("김철수" not in dict) # False

# key를 extract - keys 사용
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.keys() # dict_keys(['김철수', 'Anna'])

# value를 extract - values 사용
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.values() # dict_values([300, 180])

# key, value 쌍을 extract - items 사용
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.items() # dict_items([('김철수', 300), ('Anna', 180)])

