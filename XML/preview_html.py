import os
from time import sleep

import keyboard


def add_mm_css(desc):
    desc = """
    <html>

        <head>
            <link rel="stylesheet" type="text/css" href="https://matrixmedia.pl/skin/frontend/matrixmedia/default/css/_style.css" media="all" />
            <link rel="stylesheet" type="text/css" href="https://matrixmedia.pl/media/css_secure/73ec7298151200cd64f20af5ccdf70da.css" media="all" />
            <link rel="stylesheet" type="text/css" href="https://matrixmedia.pl/skin/frontend/matrixmedia/default/css/style_alan.css" media="all" />
            <link rel="stylesheet" type="text/css" href="https://matrixmedia.pl/skin/frontend/matrixmedia/default/css/style_dkcode.css" media="all" />
        </head>
        
        <style>
            body{width:1180px; margin:auto;}
        </style>
        
        <body>  
    """ + desc + """
        </body>
    </html>

    """

    return desc


def preview_html(desc, ean, yes_to_all):
    while 'src="//' in desc:
        desc = desc.replace('src="//', 'src="https://')

    with open('preview.html', 'w', encoding="utf-8") as preview:
        # add MatrixMedia CSS files
        preview.write(add_mm_css(desc))

    os.startfile('preview.html')  # open "preview.html" file
    sleep(1)  # let the file being opened before it is removed

    if yes_to_all is False:
        print('Zatwierdź klawiszem "Enter" lub odrzuć klawiszem "Esc"')

        # wait for a user to confirm it
        while True:
            if keyboard.is_pressed('Enter'):
                print(f'Zatwierdzono: {ean}')
                return 0
            elif keyboard.is_pressed('Esc'):
                print(f'Odrzucono: {ean}')
                return -1
    else:
        print(f'Zatwierdzono automatycznie: {ean}')

    os.remove('preview.html')  # remove "preview.html" file
