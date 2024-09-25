def solution(queue1, queue2):
    """
    완전탐색 -> 여기서 더 최적화 가능한지 생각해보기
    완전탐색 : 
    [3 2 7 2] 14 [4 6 5 1] 11
    [2 7 2] 11 [4 6 5 1 3] 19
    [2 7 2 4] 15 [6 5 1 3] 15
    """
    if (sum(queue1) + sum(queue2)) % 2: return -1
    n = len(queue1) + len(queue2)
    
    q = queue1.copy() + queue2.copy()
    q1, q2 = sum(queue1), sum(queue2)
    p1, p2 = 0, len(queue1)
    answer = 0
    visited = set([f"{p1} {p2}"])
    while True:
        """
        더 큰 값 갖는 qi 의 pi +1 하고, pi가 가리키고 있던 값 pi에서빼고 !pi에 더해준다.
        """
        if q1 < q2: 
            q1 += q[p2]
            q2 -= q[p2]
            p2 = (p2 + 1) % n
        elif q1 > q2:
            q1 -= q[p1]
            q2 += q[p1]
            p1 = (p1 + 1) % n
        else:
            return answer
        
        snapshot = f"{p1} {p2}"
        if snapshot in visited: break
        visited.add(snapshot)
        answer += 1
            
    return -1