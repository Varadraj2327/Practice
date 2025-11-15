# *args = allows you to pass mmultiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#           1. positional  2. default 3. keyword 4. ARBITRARY


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street= "783 king St.", 
              city= "Jomberg", 
              state="Narnia")