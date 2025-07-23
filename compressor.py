import string


release_name = "beta"
version = "0.9.0"

def file_to_binary(input_file_path, sep=""):
    """"""
    try:
        # Шаг 1: Читаем файл
        with open(input_file_path, 'rb') as file:
            byte_code = file.read()
        
        # Шаг 2: Преобразуем байт-код в бинарное представление
        # Каждый байт преобразуем в его бинарное представление
        binary_representation = sep.join(format(byte, '08b') for byte in byte_code)
        
        return binary_representation
    
    
    except FileNotFoundError:
        raise Exception(f"File {input_file_path} not find")
    except Exception as e:
        raise e

def compress(path: str):
    """..."""

    def count_control(count):
        """..."""
        lst = string.ascii_letters
        if count % 10 == 0:
            return lst[(count // 10) - 1]
        else:
            return str(count)


    bin_code = file_to_binary(path)

    first_bit = bin_code[0]

    new_bin_code = first_bit
    this_bit = first_bit
    count = 1
    #
    for iter in range(1, len(bin_code)):
        if bin_code[iter] == this_bit:
            count += 1
        else:
            new_bin_code += count_control(count)
            this_bit = bin_code[iter]
            count = 1
        
        # #
        if iter == len(bin_code) - 1 and count != 0:
            new_bin_code += count_control(count)

    return new_bin_code


def decompress(path: str):
    """..."""
    return None