from collections import deque
#a = "Sit on a potato pan Otis"
b = input("Enter your phrase to check if it is polyndrome  ")
def poly(a):
    p_string = "".join(p.lower() for p in a if a.isalpha())
    p = deque(p_string)
    while len(p)>1:
        if p.popleft() != p.pop():
            return False
        
    return True

print(poly(b))