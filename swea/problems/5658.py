"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
5658. [모의 SW 역량테스트] 보물상자 비밀번호

5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
20 14
88F611AE414A751A767B
24 16
044D3EBA6A647B2567A91D0E
28 11
8E0B7DD258D4122317E3ADBFEA99
"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    numbers = input()

    rotations = N // 4

    passwords = set()
    for i in range(rotations):
        for j in range(4):
            passwords.add(numbers[rotations * j : rotations * (j + 1)])
        numbers = numbers[-1] + numbers[0:-1]

    passwords = sorted([int(p, 16) for p in passwords], reverse=True)

    print(f"#{test_case} {passwords[K-1]}")
    # ///////////////////////////////////////////////////////////////////////////////////
