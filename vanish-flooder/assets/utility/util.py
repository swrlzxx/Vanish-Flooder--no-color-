import os

def load_tokens():
    with open("input/tokens.txt", "r") as f:
        tokens = f.readlines()
        bt = [token.strip() for token in tokens if token.strip().startswith(('MT'))]
        return bt

tokens = load_tokens()

def emo():
    with open('assets/get/emojis.txt', 'r', encoding='utf-8') as file:
        em = [line.strip() for line in file.readlines()]
        return em

emojis = emo()

def center(var: str, space: int = None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
    return "\n".join((' ' * int(space)) + line for line in var.splitlines())

def set_t(t):
    # Replace this with a placeholder if you're not using a title function
    print(f"Set title: {t}")

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    nm = center("""
                                                      
___    __             _____       ______  
__ |  / /_____ __________(_)_________  /_ 
__ | / /_  __ `/_  __ \_  /__  ___/_  __ \
__ |/ / / /_/ /_  / / /  / _(__  )_  / / /
_____/  \__,_/ /_/ /_//_/  /____/ /_/ /_/                                         
    """)
    print(nm)
    print("""
                                            [1] Dm Spam     [2] Exit
    """)
