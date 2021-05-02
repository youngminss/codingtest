def solution(n,students):
    results = [0] * n 
    
    for i in range(3):
        checkDict = {}
        for j in range(n):
            if not students[j][i] in checkDict:
                checkDict[students[j][i]] = 1
            else :
                checkDict[students[j][i]] += 1
        for j in range(n):
            if checkDict[students[j][i]] == 1:
                results[j] += students[j][i]
    
    return results


if __name__ == '__main__':
    n = int(input())
    students = [list(map(int,input().split())) for _ in range(n)]
    results = solution(n,students)
    [print(result) for result in results]


# - [구현] 남들과 달라야 한다.
# - [실행시간] O(n)
# - [해결방법] 
# 매 차례, 첫 반복문에서, 빈 딕셔너리를 이용해서, 한 회차 시험 중복체크를 위해 값들을 조사하면서 카운팅한다.
# 두 번째 반복문에서, 카운팅 된 점수 정보가 1(유일하게 받은 점수)이면, 결과 리스트의 값을 누적한다.

# 엘리스 토끼와 친구들은 서로 똑같은 것을 정말 싫어합니다.
# 이런 친구들끼리 만들어 새로운 놀이를 만들었습니다.
# 그 게임은 다음과 같습니다.
# 각 친구는 1 이상 100 이하의 정수를 카드에 적어 제출합니다. 
# 각 친구는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻습니다.
# 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없게 됩니다.
# 예를 들어 5명의 친구들이 다음과 같이 적어서 냈을 경우

# 100 99 98
# 100 97 92
# 63 89 63
# 99 99 99
# 89 97 98

# 각자 아래와 같이 점수를 얻게 됩니다.
# 플레이어 1 : 0 + 0 + 0 = 0
# 플레이어 2 : 0 + 0 + 92 = 92
# 플레이어 3 : 63 + 89 + 63 = 215
# 플레이어 4 : 99 + 0 + 99 = 198
# 플레이어 5 : 89 + 0 + 0 = 89
# 엘리스 토끼와 친구들은 이 게임을 3번 했습니다.
# 각 친구가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 참가자의 수인 정수 N을 입력합니다.
# (2 ≤ N ≤ 200)
# 둘째 줄부터 N개 줄에는 각 플레이어가 1번째, 2번째, 3번째 게임에서 쓴 수를 공백으로 구분하여 입력합니다.
# [출력]
# 각 플레이어가 3번의 게임에서 얻은 총 점수를 입력으로 주어진 순서대로 출력합니다.

# [입력 예시]
# 5
# 100 99 98
# 100 97 92
# 63 89 63
# 99 99 99
# 89 97 98
# [출력 예시]
# 0
# 92
# 215
# 198
# 89