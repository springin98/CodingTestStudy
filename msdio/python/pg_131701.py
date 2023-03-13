from collections import deque

def solution(elements):
    dq = deque(elements)
    ans = set()
    
    for i in range(len(elements)):
        for j in range(1, len(elements)+1):
            temp = list(dq)
            ans.add(sum(temp[0:j]))
            
        dq.append(dq.popleft())
        
    return len(ans)
