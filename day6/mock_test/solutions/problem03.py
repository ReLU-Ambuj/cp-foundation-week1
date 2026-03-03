def is_rotation(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    # If B is a rotation of A, it must be an organic substring of A+A
    return b in (a + a)

if __name__ == "__main__":
    print(is_rotation("hello", "llohe")) # True\n