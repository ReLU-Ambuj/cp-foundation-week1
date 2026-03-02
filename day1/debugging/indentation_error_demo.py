# Problem: Syntax Error due to bad indentation
# Expected Error: IndentationError: expected an indented block

def bad_function():
# BUG: Code block must be indented
# Fix: Indent `print` by 4 spaces
print("This won't work")

if __name__ == "__main__":
    try:
        bad_function()
    except Exception as e:
        # Note: IndentationErrors are often caught before the script even runs!
        pass
