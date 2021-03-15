
def separate_by_tag(tag, txt):
    tag_s = f'<{tag}'
    tag_e = f'</{tag}>'

    separated_elements = []
    while txt.find(tag_s) != -1:
        i = 0
        separated = txt[txt.find(tag_s) + i:txt.find(tag_e) + len(tag_e)]
        while not (separated.find(tag_s) == 0 and separated.count(tag_s) == 1):
            separated = txt[txt.find(tag_s) + i:txt.find(tag_e) + len(tag_e)]
            i += 1
        separated_elements.append(separated)
        txt = txt.replace(separated, '')

    return separated_elements


if __name__ == '__main__':
    text = '<div 1><div 2><div 3>penis</div></div></div>'
    separate_by_tag('div', text)
