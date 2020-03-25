import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors, output_file):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors, output_file)
        return main(language_file, encoding, errors, output_file)


def print_line(line, encoding, errors, output_file):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
    output_string = str(raw_bytes) + " <===> " + str(cooked_string) + "\n"
    output_file.write(output_string)


languages = open("languages.txt", encoding="utf-8")
output_file = open("output.txt", 'w', encoding="utf-8")

main(languages, input_encoding, error, output_file)
