def solution(votes, k):
    if k == 0:
        if votes.count(max(votes)) > 1:
            return 0
        else:
            return 1
    
    candidates_w_chances = []
    max_votes = max(votes)
    
    for vote in votes:
        if vote + k > max_votes:
            candidates_w_chances.append(vote + k)
            
    return len(candidates_w_chances)