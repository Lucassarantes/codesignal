def solution(young, beautiful, loved):
    return (young and beautiful and not loved) or (loved and young and not beautiful) or (loved and beautiful and not young) or (loved and not young and not beautiful)
