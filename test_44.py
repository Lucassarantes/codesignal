def solution(address):
    domain = address.split("@")
    return domain[len(domain) - 1]
