def most_frequent_word(s: str) -> str:
    # 1. Cleanse string of punctuation natively
    clean = ""
    for char in s:
        if char.isalnum() or char.isspace():
            clean += char.lower()
        else:
            clean += " " # Replace punct with space
            
    # 2. Extract words
    words = clean.split()
    
    # 3. Frequency map
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
        
    # 4. Dictionary resolution mapping to max
    if not freq: return ""
    max_count = -1
    max_word = ""
    
    for w, count in freq.items():
        if count > max_count or (count == max_count and w < max_word):
            max_count = count
            max_word = w
            
    return max_word

if __name__ == "__main__":
    print(most_frequent_word("Hello world. Hello Python!")) # hello\n