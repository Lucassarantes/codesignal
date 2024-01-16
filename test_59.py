def solution(code):
    segments = [code[i:i+8] for i in range(0, len(code), 8)]

    decoded_message = ''.join([chr(int(segment, 2)) for segment in segments])

    return decoded_message
