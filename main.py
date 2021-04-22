import xml.etree.ElementTree as xml
from time import gmtime, strftime

from FTP_connection.transfer import *
from XML.create_XML import create_XML
from XML.preview_html import preview_html
from collecting_data.collect_data_from_sites import collect_data_from_sites
from collecting_data.collect_data_oyo import collect_data_oyo
from imgs_processing.download_imgs_and_replace_links import download_imgs_and_replace_links

if __name__ == '__main__':
    """ HARD CODE ALERT """
    products = """52189	Basen z daszkiem Żabka/Biedronka 97x66 cm	6942138914122	9999	BESTWAY	AB	
51104	Basen dmuchany Trzy kolory 102 x 25 cm	6942138915815	9999	BESTWAY	AB	
52211	Basen dmuchany Statek 140 x 130 x 104 cm	6942138982473	9999	BESTWAY	AB	
51103	Basen dmuchany Trzy kolory 152 x 30 cm	6942138915808	9999	BESTWAY	AB	
53071	Basen ze zjeżdżalnią Słoneczna kraina	6942138952179	9999	BESTWAY	AB	
54118	Basen dmuchany Familijny 262x157x46cm	6942138951486	9999	BESTWAY	AB	
91007	Basen dmuchany Myszka Miki i przyjaciele	6942138906141	9999	BESTWAY	AB	
98018	Basen dmuchany okrągły Spider Man	6942138921403	9999	BESTWAY	AB	
53067	Basen dmuchany ze zjeżdżalnią Morskie życie	6942138926101	9999	BESTWAY	AB	
53052	Basen Dmuchany Plac zabaw ze zjeżdżalnią	6942138973686	9999	BESTWAY	AB	
91079	Basen dmuchany Myszka Minnie 122x25cm	6942138968170	9999	BESTWAY	AB	
51121	Basen dmuchany Szeroka Krawędź 152x51cm	6942138973693	9999	BESTWAY	AB	
53092	Dmuchany Basen plac zabaw ze zjeżdżalnią	6942138968873	9999	BESTWAY	AB	
53097	Dmuchany Basen ze zjeżdżalnią Jednorożec	6942138968842	9999	BESTWAY	AB	
53089	Basen dmuchany Żyrafa 266x157x127cm	6942138968149	9999	BESTWAY	AB	
55031	Basen rozporowy dla dzieci 244x46cm	6942138913781	9999	BESTWAY	AB	
51024	Basen dmuchany 102 x 25 cm	6942138915648	9999	BESTWAY	AB	
52192	Basen z daszkiem Rafa koralowa 1.40 x1.40 x1.14 m	6942138951448	9999	BESTWAY	AB	
51008	Basen dla dzieci Rybki 102 x 25cm	6942138900347	9999	BESTWAY	AB	
56283	Basen stelażowy okrągły dla dzieci 152 x 38cm	6942138920192	9999	BESTWAY	AB	
53093	Dmuchany basen ze zjeżdżalnią Leśna polana	6942138968088	9999	BESTWAY	AB	
53069	Dmuchany Basen ze zjeżdżalnią Wulkan	6942138926125	9999	BESTWAY	AB	
51115	Basenik dmuchany 165x104x25cm 51115	6942138910414	9999	BESTWAY	AB	
55029	Basenik rozporowy Burta statku 152 x 25 cm	6942138981872	9999	BESTWAY	AB	
52378	Basenik z sorterem kształtów i Bańka wodna	6942138983906	9999	BESTWAY	AB	
57326	Basenik rozporowy z pierścieniem i spryskiwaczem	6942138936865	9999	BESTWAY	AB	
57241	Basenik rozporowy z dmuchanym pierścieniem	6942138974980	9999	BESTWAY	AB	
52331	Basenik z daszkiem Owocowy Domek 94 x 89 x 79 cm	6942138972078	9999	BESTWAY	AB	
51033	Mini Basenik Różowy/Niebieski 70 x 30 cm	6942138900422	9999	BESTWAY	AB	
56217	Mini Basenik Stelażowy 122 x 122 x 30.5 cm	6942138974973	9999	BESTWAY	AB	
58278	Siatka do czyszczenia basenu 43x21cm	6942138948578	9999	BESTWAY	AB	
58253	Pokrywa solarna do basenu 4,57m	6942138918953	9999	BESTWAY	AB	
58105	Pokrywa do basenu prostokątnego 2.59m x 1.70m	6942138918489	9999	BESTWAY	AB	
58210	58072 Pływajacy dozownik chemii basenowej	6942138918731	9999	BESTWAY	AB	
51061	Mikro basenik brodzik 61x15cm	6942138915693	9999	BESTWAY	AB	
52261	Dmuchany Basenik z piłkami Lew 111x98x61	6942138961959	9999	BESTWAY	AB	
58103	Pokrywa do basenu prostokątnego 2.21m x 1.50m	6942138918465	9999	BESTWAY	AB	
58319	Pokrywa Flowclear do basenu 262x175x51cm	6942138923551	9999	BESTWAY	AB	
58038	Pokrywa Flowclear do basenu okrągłego 4,57m	6942138951653	9999	BESTWAY	AB	
93538	Dmuchany helikopter Fisher Price z piłkami	6942138961935	9999	BESTWAY	AB	
34103	Łódeczka z daszkiem mix-auto	6942138933925	9999	BESTWAY	AB	
93537	Dmuchany pociąg Fisher Price z piłkami	6942138961942	9999	BESTWAY	AB	
98009	Łódka Spiderman 112 x 71 cm	6942138911763	9999	BESTWAY	AB	
32050	Siedzisko do nauki pływania kwadrat 76 x 76 cm	6942138949667	9999	BESTWAY	AB	
98003	Kółko dmuchane do pływania Spider-Man	6942138919585	9999	BESTWAY	AB	
36057	Kółko do pływania Okulary 76 cm	6942138949780	9999	BESTWAY	AB	
52254	Ślizgawka pojedyncza z rampą 5,49 m	6942138954135	9999	BESTWAY	AB	
91040	Kółko dmuchane do pływania Minnie	6942138917581	9999	BESTWAY	AB	
98001	Rękawki do nauki pływania Spiderman 23x15 cm	6942138919561	9999	BESTWAY	AB	
32033	Rękawki do nauki pływania M Żółte 25x15 cm	6942138915754	9999	BESTWAY	AB	
91081	Duży dmuchany Flaming Disney 173x170cm	6942138969078	9999	BESTWAY	AB	
36239	Koło dmuchane do pływania 119cm Palmy	6942138982053	9999	BESTWAY	AB	
91003	Łódka Minnie&Miki 102x69 cm	6942138906103	9999	BESTWAY	AB	
91070	Dmuchana kamizelka do nauki pływania Minnie 51x46 cm	6942138927658	9999	BESTWAY	AB	
52258	Ślizgawka H2Go Potrójna z fontanną 5,49m	6942138954159	9999	BESTWAY	AB	
91002	Dmuchane rękawki do pływania Miki/Mini 23x15 cm	6942138919486	9999	BESTWAY	AB	
43124	Dmuchany kolorowy materac 185x69cm	6942138934298	9999	BESTWAY	AB	
52320	Ślizgawka H2Go podwójna wyścig Lam 4,88	6942138968897	9999	BESTWAY	AB	
52329	Ślizgawka H2Go Potrójna 4,88m	6942138969092	9999	BESTWAY	AB	
32034	Kamizelka do nauki pływania żółta 51x46 cm	6942138915761	9999	BESTWAY	AB	
98014	Dmuchana kamizelka do nauki pływania Spiderman 51x46 cm	6942138913514	9999	BESTWAY	AB	
51134	Wanienka plażowa	6942138951424	9999	BESTWAY	AB	
41032	Dmuchany niebieski Rekin 157x71cm	6942138966817	9999	BESTWAY	AB	
91043	Koło dmuchane Princess 56cm	6942138908664	9999	BESTWAY	AB	
36024	Kółko do pływania Neon 76cm Zieleń/Pomarańcz	6942138981520	9999	BESTWAY	AB	
43413	Materac plażowy Syrenka 193x101cm 43413	6942138985184	9999	BESTWAY	AB	
36118	Koło dmuchane do pływania Donat 107cm	6942138939064	9999	BESTWAY	AB	
91042	91042 Piłka plażowa Disney Princess 51cm	6942138981407	9999	BESTWAY	AB	
31036	Piłka plażowa 31036 51cm Mix kolor	6942138967142	9999	BESTWAY	AB	
36237	Koło dmuchane do pływania 119cm Kwiaty	6942138982183	9999	BESTWAY	AB	
91004	Kółko do pływania Minnie/Miki 56cm	6942138919493	9999	BESTWAY	AB	
36022	Kółko do pływania przezroczyste 51cm	6942138975307	9999	BESTWAY	AB	
36240	Kółko do pływania opalizujące 107cm	6942138985177	9999	BESTWAY	AB	
44007	Materac plażowy matowy 183x69 cm	6942138940480	9999	BESTWAY	AB	
36025	Kółko do pływania Neon 91cm Zieleń/Pomarańcz	6942138981575	9999	BESTWAY	AB	""".split('\n')

    send_via_FTP = True
    print_result = True
    yes_to_all = True
    """ HARD CODE ALERT """

    # define an XML file to write products data inside
    root = xml.Element('Products')
    tree = None
    declined = []
    marked = []
    for product in products:
        # (1) gather all necessary data On Your Own (OYO)
        full_product = collect_data_oyo(product.split('\t'))
        print(f"=============== {full_product['name']} ===============")

        # (2) gather all necessary data from given page(s)
        collect_data_from_sites(full_product)

        # (3) preview description
        preview_result = preview_html(full_product, full_product['sku'], yes_to_all)
        if preview_result == -1:
            declined.append(full_product['sku'])
            continue
        elif preview_result == 1:
            marked.append(full_product['sku'])

        # (4) download imgs from description and replace links
        download_imgs_and_replace_links(full_product)

        # (5) create XML out of collected data
        tree = create_XML(root, full_product)

        if print_result:
            print('PRINTING SCRAPPED DESCRIPTIONS...')
            print(full_product["descriptions"][0])
            print('-' * 15)
            print(full_product["descriptions"][1])
            print('-' * 15)
            print(full_product["descriptions"][2])

    if send_via_FTP and tree is not None:
        xml_file_name = f'Products_{strftime("%Y%m%d%H%M%S", gmtime())}.xml'

        with open(f'bin\\{xml_file_name}', 'wb') as file:
            tree.write(file)

        folders = [folder for folder in os.listdir('bin') if
                   not folder.endswith('.xml') and len(folder.split(' - ')) == 2]

        for folder in folders:
            f = folder.split(' - ')
            FTP = make_FTP_connection()
            send_description_imgs_via_FTP(FTP, f[0], f[1])  # send description images via FTP
            send_products_imgs_via_FTP(FTP, folder)  # send product images via FTP
            send_XML_via_FTP(FTP, xml_file_name)  # send XML via FTP
            close_FTP_connection(FTP)

    if marked:
        print(f'Marked by user: ')
        [print(f"{i}. {ele}") for i, ele in enumerate(marked)]

    if declined:
        print(f'Declined by user: ')
        [print(f"{i}. {ele}") for i, ele in enumerate(declined)]
    else:
        print('All products were added')
