# Problem: Is Anagram abstraction
def build_freq(s: str) -> dict:
    f = {}
    for c in s: f[c] = f.get(c, 0) + 1
    return f

def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False
    return build_freq(s1) == build_freq(s2)

if __name__ == "__main__":
    print(is_anagram("ab", "ba")) # True\n