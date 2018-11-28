with open('parseddata', 'r') as f:
    read_data = f.readlines()

# strip empty lines
lines = [line for line in read_data if line.strip() != '']

new_dict = {}
book_title = ''
for line in lines:
    if "BOOK:" in line:
        book_title = line
        new_dict[book_title] = []
    else:
        if "-ebook" in line and line.startswith('https://www.amazon.com/'):
            new_dict[book_title].append(line.rstrip('\n'))

with open('extracted_first_links', 'w') as f:
    for key, values in new_dict.items():
        f.write(key)
        try:
            f.write(values[0])
        except:
            f.write('KINDLE VERSION NOT FOUND!')
        f.write('\n\n')
