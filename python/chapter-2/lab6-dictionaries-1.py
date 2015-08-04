def build_successors_table(tokens):
    table = {}
    prev = '.'
    for word in tokens:
        if prev in table:
            table[prev] = table[prev] + [word]
        else:
            table[prev] = [word]
        prev = word
    return table


text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
table = build_successors_table(text)
print(table)
