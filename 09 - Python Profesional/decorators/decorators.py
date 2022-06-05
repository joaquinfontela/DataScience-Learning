from src.cyphers.caesar.caesar import caesar_cypher
from copy import copy


def encrypt_string_params(encrypt_function, *enc_args, **enc_kwargs):
    def encrypt(func):
        def wrapper(*args, **kwargs):
            new_args = []
            new_kwargs = copy(kwargs)
            for arg in args:
                if isinstance(arg, str):
                    new_args.append(
                        cypher(arg, encrypt_function, *enc_args, **enc_kwargs))
                else:
                    new_args.append(arg)
            for k in new_kwargs:
                if isinstance(new_kwargs[k], str):
                    new_kwargs[k] = cypher(
                        new_kwargs[k], encrypt_function, *enc_args, **enc_kwargs)
            func(*new_args, **new_kwargs)
        return wrapper
    return encrypt


def cypher(string, cypher_function, *args, **kwargs):
    return cypher_function(string, *args, **kwargs)


@encrypt_string_params(caesar_cypher, 4)
def print_func_params(_id, name, last_name, age=None, password=None):
    print(_id)
    print(name)
    print(last_name)
    print(age)
    print(password)


print_func_params(42341390, 'Joaquin', 'Fontela', 22, password='abc123')
