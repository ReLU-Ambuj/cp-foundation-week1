# Problem: Count words returning integer
def count_words(s: str) -> int:
    return len([w for w in s.split(" ") if w])

if __name__ == "__main__":
    print(count_words("   hello world   ")) # 2\n