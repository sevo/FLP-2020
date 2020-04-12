def print_decorator(fct):
    """dento dekorator pouzivam, na to aby som dokazal testovat aj vypisy na standardny vystup"""
    original_fct = fct
    output = []
    def wrapper(*args):
        output.append((args))
        return original_fct(*args)
    return wrapper

print = print_decorator(print) # dekoratorom nahradzam originalny print za moj upraveny, ktory zapsiuje svoje parametre do premennej

def simple(string): # ak test na tuto funkciu prechadza tak moj dekorator funguje spravne
    print(string)