def solution(words):
    finger = [0,0,0,0,0,0,0,0]
    areas = [
        ['1','Q','A','Z'],
        ['2','W','S','X'],
        ['3','E','D','C'],
        ['4','R','F','V','5','T','G','B'],
        ['6','Y','H','N','7','U','J','M'],
        ['8','I','K',','],
        ['9','O','L','.'],
        ['0','P',';','/','-','[',"'",']','=']
        ]
    for word in words:
        for i in range(len(areas)):
            if word in areas[i]:
                finger[i] += 1
                break
    return finger

if __name__ == '__main__':
    words = input()
    result = solution(words)
    [print(n) for n in result]


# [구현] 타자 연습하기

# 도도새는 두 검지 손가락만으로 키보드를 치는 ‘독수리 타법’으로 컴퓨터 키보드를 입력해왔습니다.
# 그런데 이번에 코딩을 배울 때 영타를 쳐야하는데, 독수리 타법으로 치기에는 속도가 너무 느려 제대로 된 타자 방식을 배우려고 합니다.
# 키보드 자판의 배열은 위의 그림과 같습니다.

# ‘A’는 왼손 소지, ‘S’는 왼손 약지 ‘D’는 왼손 중지, ‘F’는 왼손 검지이며, 
# ‘J’는 오른손 검지, ‘K’는 오른손 중지, ‘L’은 오른손 약지, ‘;’는 오른손 소지로 입력을 하므로
# 총 8개의 손가락으로 전체 자판을 입력할 수 있습니다. 
# 또한 같은 색상의 자판은 같은 손가락으로 입력을 합니다.

# [입력]
# 첫 번째 줄에 위의 키보드 자판에 적혀있는 글자로 이루어진 문자열을 공백없이 입력합니다.
# 문자열의 길이는 1 이상 50 이하입니다.
# [출력]
# 여덟 줄에 각 손가락이 키보드를 누른 횟수를 출력합니다.
# 각 줄은 왼손 소지, 왼손 약지, 왼손 중지, 왼손 검지, 오른손 검지, 오른손 중지, 오른손 약지, 오른손 소지입니다.
# 키보드의 입력이 주어졌을 때, 각 손가락이 몇 번 움직여야 하는지 출력하는 프로그램을 작성하세요.

# [입력 예시]
# ELICE,DODO[FRIEND]
# [출력 예시]
# 0
# 0
# 7
# 2
# 1
# 3
# 3
# 2

# [문제출처] 엘리스 AI 트랙
