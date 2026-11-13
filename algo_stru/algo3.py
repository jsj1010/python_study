# 삽입(insertion) 정렬 : 앞에서 부터 하나씩 꺼내 자기자리 찾아 끼워넣는 정렬
# 배열의 앞에서부터 차례대로 이미 정렬된 부분과 비교하여, 자신의 위치를 찾아 삽입하는 방식의 정렬 알고리즘

# 방법1 : 이해용 - 추가 공간이 있음
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        # v값이 i번 위치값 보다 작으면 
        if v < r[i]:
            return i 
        
    # 적정한 위치를 못찾은 경우 맨 뒤에 삽입
    return len(r)

def  ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        print('a(d) : ', a)
        print('result :', result)

    return result

d = [2,4,5,1,3]
# print(find_ins_idx(d, 1))
print(ins_sort(d))


# 방법2 : 일반적 : 추가 공간이 거의 없음
