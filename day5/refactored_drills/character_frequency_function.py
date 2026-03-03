# Problem: Reusable dictionary builder
def get_char_frequencies(s: str) -> dict:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    print(get_char_frequencies("hello")) # {'h':1, 'e':1, 'l':2, 'o':1}\n