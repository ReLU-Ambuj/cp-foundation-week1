def parse_key_values(records: list) -> list:
    master_dict = {}
    
    for record in records:
        # Split by comma
        pairs = record.split(',')
        for pair in pairs:
            if '=' in pair:
                k, v = pair.split('=', 1) # Split strictly on FIRST '='
                k = k.strip()
                v = v.strip()
                if k: # Valid Guard
                    master_dict[k] = v
                    
    # Return sorted keys
    return sorted(master_dict.keys())

if __name__ == "__main__":
    print(parse_key_values(["a=1,b=2", "c=1,=5", "d=foo=bar"])) 
    # ['a', 'b', 'c', 'd']\n