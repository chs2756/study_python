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
  
