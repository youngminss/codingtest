def solution(words):
    alpha = [0] * 26
    for word in words:
        alpha[ord(word) - ord('a')] += 1
    return alpha

if __name__ == '__main__':
    words = input()
    result = solution(words)
    [print(data, end=' ') for data in result]


# [문자열] 3살 엘리스 토끼
# [실행시간] O(len(words))

# 엘리스 토끼는 영어를 배워 모든 알파벳을 알게 되었습니다. 
# 알파벳에 흥미를 느낀 엘리스 토끼는 단어를 주면 각 알파벳이 단어에 몇 개가 포함되어 있는지 개수를 셉니다.
# 예를 들어 apple이라는 단어가 주어질 때 a가 1개, e가 1개, p가 2개, l이 1개로 개수를 셉니다.
# 단어를 줬을 때 각 알파벳이 단어에 몇 개가 포함되어 있는지 출력하는 프로그램을 작성하세요.

# [입력]
# 첫 번째 줄에 엘리스 토끼에게 주어진 영어 단어를 입력합니다. 영어 단어는 소문자로만 구성되어있으며 길이는 1,000을 넘지 않습니다.
# [출력]
# 첫 번째 줄에 단어에 포함된 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력합니다.

# [입력 예시]
# apple
# [출력 예시]
# 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 2 0 0 0 0 0 0 0 0 0 0

# [문제출처] : 엘리스 AI 트랙