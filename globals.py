import os

STARTING_DIRECTORY = os.getcwd()


def func_name(func):
    def wrapper(*args, **kwargs):
        print(f"INFO: {func.__name__} func was picked")
        func(*args, **kwargs)

    return wrapper


def separate_by_tag(tag, txt):
    tag_s = f'<{tag}'
    tag_e = f'</{tag}>'

    repetition = 0
    separated_elements = []
    while txt.find(tag_s) != -1:
        i = 0
        separated = txt[txt.find(tag_s) + i:txt.find(tag_e) + len(tag_e)]
        while not (separated.find(tag_s) == 0 and separated.count(tag_s) == 1):
            separated = txt[txt.find(tag_s) + i:txt.find(tag_e) + len(tag_e)]
            i += 1

            repetition += 1
            if repetition > 20000:
                break
        separated_elements.append(separated)
        txt = txt.replace(separated, '')

        repetition += 1
        if repetition > 20000:
            break

    return separated_elements


def join_strip(text):
    return ''.join(text).strip()
