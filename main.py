from compressor import *


def main():
    image_data = "img.webp"    # Исходный файл


    a_file = file_to_binary(image_data, sep="")
    b_file = compress(image_data)
    print(a_file, b_file, sep="\n")
    print(len(b_file) / len(a_file) * 100)

if __name__ == "__main__":
    main()