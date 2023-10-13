# 산악 구조를 위한 로봇이 있습니다. 

# 이 로봇은 연료 소모를 최대한 적게 하면서 조난자에게 이동하여 구출하려고 합니다. 

 

# 산악 구조는 N x N 크기의 지도로 정보가 주어집니다.

# 각 칸의 값은 땅의 높이를 표현하며, 구조 로봇은 상, 하, 좌, 우 방향으로만 이동이 가능합니다. 

 

# 구조 로봇의 연료 소모량은 다음과 같습니다. 

#     내리막길 (현재 위치에서 더 낮은 곳으로 이동할 때)에서는 연료가 소모되지 않습니다. 
#     오르막길 (현재 위치에서 더 높은 곳으로 이동할 때)에서는 높이 차이의 2배가 소모됩니다.
#     평지 (현재 위치에서 같은 높이로 이동할 때)에서는 1의 연료가 소모됩니다.

 

# 해당 산에는 많은 조난자가 발생하여, M개의 터널을 만들었습니다.

# 각 터널은 두 위치 A, B를 C의 연료만큼 소모하여 자유롭게 이동할 수 있습니다.

# 단, 터널을 이용하기 시작하면 반대편 위치까지 도착하기 전에 터널을 벗어날 수 없습니다.

# (무조건 A->B, B->A로만 갈 수 있습니다.)

 

# 구조 로봇의 출발지는 항상 (1, 1)로 고정되어 있으며, 조난자의 위치는 (N, N)으로 고정되어 있습니다.

# 조난자의 위치까지 최소 연료를 소비하는 경로를 찾고, 소모된 연료 값을 출력하는 프로그램을 작성하시오. 

# [제약 사항] 

 

# 1. 지도의 가로, 세로 길이 N은 4이상 30이하의 정수입니다. (4 ≤ N ≤ 30) 

# 2. 터널의 개수 M은 30이하의 정수입니다. (1 ≤ M ≤ 30)

# 3. 땅의 높이는 0이상 9이하의 정수입니다.

# 4. 로봇은 상, 하, 좌, 우 방향, 그리고 터널을 활용해서만 이동이 가능합니다. 

# 5. 터널은 양방향으로 이동가능하며, 방향과 상관없이 터널을 사용할 때의 연료 소모량은 동일합니다.

# 6. 한 위치에 여러 개의 터널이 뚫려있는 경우도 존재할 수 있습니다.

# 입력

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어집니다. 

# 각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 길이 N과 터널의 개수 M이 주어집니다. 

# 다음 개의 줄에는 N개의 정수들의 공백으로 분리되어 산악 구조의 정보가 주어집니다.

# 마지막 M개의 줄에는 터널이 연결된 좌표 A의 위치 (Ay, Ax), B의 위치(By, Bx) 그리고 해당 터널을 이용할 때의 연료 소모량 C가 공백으로 구분되어 주어집니다.

# 출력

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력합니다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작합니다.)

import heapq

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dijkstra(sy, sx, ey, ex):
    pq = [(0, sy, sx)]
    dp = [[float('INF') for _ in range(N)] for _ in range(N)]
    dp[sy][sx] = 0
    
    while pq:
        # 현재 위치와 누적된 비용
        fu, cy, cx = heapq.heappop(pq)

        if fu > dp[cy][cx]:
            continue
        
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                now = board[cy][cx]
                new = board[ny][nx]
                nextv = fu + (0 if now > new else (1 if now == new else 2 * (new - now)))
                
                if nextv < dp[ny][nx]:
                    dp[ny][nx] = nextv
                    heapq.heappush(pq, (nextv, ny, nx))
        
        # 터널이 존재하는지 확인
        if (cy, cx) in tunnel_dict:
            ny, nx, cost = tunnel_dict[(cy, cx)]
            nextv = fu + cost
            
            # 터널을 이용한 이동이 더 적은 비용이면 업데이트
            if nextv < dp[ny][nx]:
                dp[ny][nx] = nextv
                heapq.heappush(pq, (nextv, ny, nx))
                
    return dp[ey][ex]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    tunnel_dict = {}
    
    for _ in range(M):
        ay, ax, by, bx, c = map(int, input().split())
        tunnel_dict[(ay - 1, ax - 1)] = (by - 1, bx - 1, c)
        tunnel_dict[(by - 1, bx - 1)] = (ay - 1, ax - 1, c)
    
    ans = dijkstra(0, 0, N-1, N-1)
    print(f'#{tc} {ans}')
