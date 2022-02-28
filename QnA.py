#2차원 배열안에 값 확인


#dict 가 list보다 in 으로 안에 있는 값을 검색할 때 훨씬 빠르다(위가 더 빠름)
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True

def solution(phone_book):
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in phone_book and temp != phone_number:
                return False
    return True
  
#List 생성시 for, if 사용하기
test_list = [x for i in range(100) if x%3 ==0]

#sorting 시 key로 lambda 사용하기
test_List = sorted(key=lambda x : x[1])
