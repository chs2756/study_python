''' https://yunaaaas.tistory.com/5 '''

''' 리스트 정렬 '''
#list 정렬
a = [1, 10, 5, 7, 6]
a.reverse() # [6, 7, 5, 10, 1]

a = [1, 10, 5, 7, 6]
a.sort()  # [1, 5, 6, 7, 10]

a = [1, 10, 5, 7, 6]
a.sort(reverse=True)  # [10, 7, 6, 5, 1]

m = ['나는', '파이썬을', '잘하고', '싶다']
m.sort(key=len)  # ['나는', '싶다', '잘하고', '파이썬을'] # key : 지정된 함수 결과에 따라 정렬 lambda에 사용

#List 정렬된 결과를 반환, 리스트 본체는 변형되지 않는다.
x = [1 ,11, 2, 3]
y = sorted(x) # x - [1,11,2,3]
y  # [1, 2, 3, 11]

x = [1 ,11, 2, 3]
y = reversed(x) # x - [1,11,2,3]
y # <list_reverseiterator object at 0x1060c9fd0>
list(y) # [3, 2, 11, 1]

''' Dictionary 정렬 '''
#key 기준으로 정렬 : List 형으로 반환
dic = {
 	1 : 'b',
    	3 : 'c',
    	5 : 'd',
    	2 : 'a',
    	4 : 'e'
}
dic2 = sorted(dic.keys()) # [ 1,2,3,4,5 ]
dic3 = sorted(dic.items()) # [ (1,'b'), (2,'a'), (3,'c'), (4,'e'), (5,'d') ], Items를 사용하면 key, value 모두 반환(튜플형태)
#내림차순 적용
dic = {
 	1 : 'b',
    	3 : 'c',
    	5 : 'd',
    	2 : 'a',
    	4 : 'e'
}

dic2 = sorted(dic.keys() , reverse = True) # [ 5,4,3,2,1 ]
dic3 = sorted(dic.items() , reverse = True) # [ (5,'d'), (4,'e'), (3,'c'), (2,'a'), (1,'b') ]


#value 기준으로 정렬 : List 형으로 반환
dic = {
 	1 : 'b',
    	3 : 'c',
    	5 : 'd',
    	2 : 'a',
    	4 : 'e'
}

# [ (2,'a'),(1,'b'),(3,'c'),(5,'d'),(4,'e') ]
dic2 = sorted(dic.items(), key = lambda item : item[1])
''' value 값은 item[1]이기 때문에 기순을 위와 같이 설정'''

#lambda를 사용하여 key값으로 정렬
dic = {
 	1 : 'b',
    	3 : 'c',
    	5 : 'd',
    	2 : 'a',
    	4 : 'e'
}

# [ (1,'b'), (2,'a'), (3,'c'), (4,'e'), (5,'d') ]
dic2 = sorted(dic.items(), key = lambda item : item[0])

#lambda 사용하여 응용 정렬
student = [
	{'name':'kim', 'age' : 20},
    	{'name':'park', 'age' : 10},
        {'name':'lee', 'age' : 13},
        {'name':'choi', 'age' : 25},
        {'name':'park', 'age' : 25},
        {'name':'lee', 'age' : 33}
 ]
tu_sorted = sorted(student, key = lambda item : (-item['age'], item['name']))

'''
[ {'name':'lee', 'age' : 33},
    {'name':'choi', 'age' : 25},
    {'name':'park', 'age' : 25},
    {'name':'kim', 'age' : 20},
    {'name':'lee', 'age' : 13},
    {'name':'park', 'age' : 10} ]
'''

#sorted와 itemgetter 를 이용하여 정렬하기
'''age 오름차순 정렬 후, name으로 오름차순 정렬'''
from operator import itemgetter

stu_sorted = sorted(student, key = itemgetter('age','name'))

'''
[ {'name':'park', 'age' : 10},
{'name':'lee', 'age' : 13},
{'name':'kim', 'age' : 20},
{'name':'choi', 'age' : 25},
{'name':'park', 'age' : 25},
{'name':'lee', 'age' : 33} ]
'''
