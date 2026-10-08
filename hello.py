def greet(name):
    """返回问候语。"""
    return f"Hello, {name}!"

def farewell(name):
    """返回告别语。"""
    return f"Goodbye, {name}!"
    
if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))