import os
from time import sleep

import keyboard

from globals import timeit


def add_mm_css(full_product):
    html = """<html lang="pl" id="top" class=" js no-touch localstorage no-ios js no-touch localstorage no-ios js no-touch localstorage no-ios js no-touch localstorage no-ios js no-touch localstorage no-ios" style=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">


<script src="./materials1 (25)_files/1730222507228304" async=""></script><script src="./materials1 (25)_files/129386579048568" async=""></script><script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W9VLJJP');</script>

<script src="./materials1 (25)_files/polyfill.min.js"></script>

<link rel="shortcut icon" href="https://matrixmedia.pl/media/favicon/default/favicon-matrix.png" type="image/x-icon">

<link rel="stylesheet" type="text/css" href="./materials1 (25)_files/d7330a78482586cb91f4ada26ab357e7.css" media="all">
<link rel="stylesheet" type="text/css" href="./materials1 (25)_files/ad8c8ff0ccf41376067f12760409631e.css">
<script type="text/javascript" src="./materials1 (25)_files/8725a98f833f54afe25389fd15a1e88d.js"></script>
<script type="text/javascript" src="./materials1 (25)_files/ff0d1756ed9c8b415e21fb08ca5cc3ea.js" defer=""></script>
<link rel="stylesheet" href="./materials1 (25)_files/css">
<link rel="stylesheet" href="./materials1 (25)_files/jquery.modal.min.css">
<link rel="canonical" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html">


<link rel="stylesheet" type="text/css" href="./materials1 (25)_files/82f4a1024c684a2850f163ec5052316c.css" media="all">


<script type="text/javascript">
//<![CDATA[
Mage.Cookies.path     = '/';
Mage.Cookies.domain   = '.matrixmedia.pl';
//]]>
</script>
<meta name="viewport" content="initial-scale=1.0, width=device-width">

<script type="text/javascript">
//<![CDATA[
optionalZipCountries = ["HK","IE","MO","PA"];
//]]>
</script>
    
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=129386579048568&ev=PageView&noscript=1&a=exmagento-1.9.4.3-2.6.0"
/></noscript>

<script type="text/javascript">//<![CDATA[
        var Translator = new Translate({"HTML tags are not allowed":"Znaczniki HTML są niedozwolone","Please select an option.":"Prosimy o wybranie opcji.","This is a required field.":"To pole jest wymagane.","Please enter a valid number in this field.":"Prosimy o wprowadzenie poprawnego numeru w tym polu.","The value is not within the specified range.":"Wartość nie znajduje się w podanym zakresie.","Please use numbers only in this field. Please avoid spaces or other characters such as dots or commas.":"Prosimy o używanie tylko liczb w tym polu. Prosimy o unikanie spacji, przecinków lub kropek.","Please use letters only (a-z or A-Z) in this field.":"Prosimy o używanie jedynie liter (a-z lub A-Z) w tym polu.","Please use only letters (a-z), numbers (0-9) or underscore(_) in this field, first character should be a letter.":"Prosimy o używanie jedynie liter (a-z), cyfr (0-9) lub podkreślnika (_) w tym polu, pierwszy znak powinien być literą.","Please use only letters (a-z or A-Z) or numbers (0-9) only in this field. No spaces or other characters are allowed.":"Prosimy o używanie jedynie liter (a-z lub A-Z) lub cyfr (0-9) w tym polu. Spacje i inne znaki nie są dozwolone.","Please use only letters (a-z or A-Z) or numbers (0-9) or spaces and # only in this field.":"Prosimy o używanie jedynie liter (a-z lub A-Z), cyfr (0-9) lub spacji i # w tym polu.","Please enter a valid phone number. For example (123) 456-7890 or 123-456-7890.":"Prosimy o wprowadzenie poprawnego numeru telefonu. Dla przykładu: (012) 345 67 89 lub 012 345 6789.","Please enter a valid fax number. For example (123) 456-7890 or 123-456-7890.":"Prosimy o wprowadzenie poprawnego numeru faksu. Dla przykładu: (012) 345 67 89 lub 012 345 6789.","Please enter a valid date.":"Prosimy o wprowadzenie poprawnej daty.","The From Date value should be less than or equal to the To Date value.":"Data początkowa nie może być późniejsza niż data końcowa","Please enter a valid email address. For example johndoe@domain.com.":"Prosimy o wprowadzenie poprawnego adresu e-mail. Dla przykładu: jankowalski@domena.pl.","Please use only visible characters and spaces.":"Prosimy używać tylko widocznych znaków i spacji.","Please make sure your passwords match.":"Prosimy upewnić się, że hasła psują do siebie.","Please enter a valid URL. Protocol is required (http:\/\/, https:\/\/ or ftp:\/\/)":"Prosimy o wprowadzenie poprawnego URL. Wymagany jest protokół (http:\/\/, https:\/\/ lub ftp:\/\/)","Please enter a valid URL. For example http:\/\/www.example.com or www.example.com":"Prosimy o wprowadzenie poprawnego URL. Dla przykładu: http:\/\/www.strona.pl lub www.strona.pl","Please enter a valid URL Key. For example "example-page", "example-page.html" or "anotherlevel\/example-page".":"Prosimy o wprowadzenie poprawnego klucza URL. Dla przykładu: "przykladowa-strona" lub "przykladowa-strona.html" lub "innypoziom\/przykladowa-strona".","Please enter a valid XML-identifier. For example something_1, block5, id-4.":"Prosimy o wprowadzenie poprawnego identyfikatora XML. Na przykład cos_1, blok5, id-4","Please enter a valid social security number. For example 123-45-6789.":"Prosimy o wprowadzenie poprawnego numeru ubezpieczenia społecznego. Dla przykładu: 123-45-6789.","Please enter a valid zip code. For example 90602 or 90602-1234.":"Prosimy o wprowadzenie poprawnego kodu pocztowego. Dla przykładu: 90602 lub 90-602.","Please enter a valid zip code.":"Prosimy o wprowadzenie poprawnego kodu pocztowego.","Please use this date format: dd\/mm\/yyyy. For example 17\/03\/2006 for the 17th of March, 2006.":"Prosimy o użycie następującego formatu daty: dd\/mm\/rrrr. Dla przykładu: 17\/03\/2006.","Please enter a valid $ amount. For example $100.00.":"Prosimy o wprowadzenie poprawnej kwoty w $. Na przykład $100.00.","Please select one of the above options.":"Prosimy o wybór jednej z powyższych opcji.","Please select one of the options.":"Prosimy o wybór jednej z opcji.","Please select State\/Province.":"Prosimy o wybór regionu.","Please enter a number greater than 0 in this field.":"Prosimy o podanie numeru większego od 0 w tym polu.","Please enter a number 0 or greater in this field.":"Prosimy o podanie cyfry 0 lub większej w tym polu.","Please enter a valid credit card number.":"Prosimy o wprowadzenie poprawnego numeru karty kredytowej.","Credit card number does not match credit card type.":"Numer karty nie zgadza się z podanym typem karty.","Card type does not match credit card number.":"Typ karty nie zgadza się z podanym numerem karty.","Incorrect credit card expiration date.":"Nieprawidłowa data wygaśnięcia karty.","Please enter a valid credit card verification number.":"Prosimy o wprowadzenie poprawnego weryfikacyjnego numeru karty kredytowej.","Please use only letters (a-z or A-Z), numbers (0-9) or underscore(_) in this field, first character should be a letter.":"Prosimy o używanie jedynie liter (a-z lub A-Z), cyfr (0-9) lub podkreślnika (_) w tym polu, pierwszy znak powinien być literą.","Please input a valid CSS-length. For example 100px or 77pt or 20em or .5ex or 50%.":"Prosimy o wprowadzenie poprawnej długości CSS. Na przykład 100px lub 77pt lub 20em lub .5ex lub 50%.","Text length does not satisfy specified text range.":"Nieprawidłowa ilość znaków.","Please enter a number lower than 100.":"Prosimy o podanie liczby mniejszej niż 100.","Please select a file":"Wybierz plik","Please enter issue number or start date for switch\/solo card type.":"Prosimy o podanie numeru wydania lub daty rozpoczęcia dla kart typu switch\/solo.","Please wait, loading...":"Prosimy czekać, trwa ładowanie...","This date is a required value.":"Data jest polem wymaganym.","Please enter a valid day (1-%d).":"Prosimy wpisać poprawny dzień (1-%d).","Please enter a valid month (1-12).":"Prosimy wpisać poprawny miesiąc (1-12).","Please enter a valid year (1900-%d).":"Prosimy wpisać poprawny rok (1900-%d).","Please enter a valid full date":"Prosimy o wprowadzenie poprawnej pełnej daty","Please enter a valid date between %s and %s":"Prosimy o wprowadzenie poprawnej daty pomiędzy %s i %s","Please enter a valid date equal to or greater than %s":"Prosimy o wprowadzenie poprawnej daty równej lub większej niż %s","Please enter a valid date less than or equal to %s":"Prosimy o wprowadzenie poprawnej daty mniejszej lub równej niż %s","Complete":"Zakończone","Add Products":"Dodaj produkty","Please choose to register or to checkout as a guest":"Prosimy o rejestrację lub złożenie zamówienia jako gość","Your order cannot be completed at this time as there is no shipping methods available for it. Please make necessary changes in your shipping address.":"Twoje zamówienie nie może zostać zrealizowane, w chwili obecnej nie mamy dla niego odpowiedniej metody dostawy. Prosimy wprowadzić odpowiednie zmiany do swojego adresu dostawy.","Please specify shipping method.":"Prosimy o wybór metody dostawy.","Your order cannot be completed at this time as there is no payment methods available for it.":"Twoje zamówienie nie może zostać zrealizowane, w chwili obecnej nie mamy dla niego odpowiedniej metody płatności.","Please specify payment method.":"Prosimy o wybór metody płatności.","Add to Cart":"Do koszyka","In Stock":"Dostępny","Out of Stock":"Zapytaj o produkt"});
        //]]></script>    <meta property="og:title" content="Telewizor SONY KD-77AG9">
    <meta property="og:image" content="https://matrixmedia.pl/media/catalog/product/optimized/9/3/93ceefbf18bbb03edeadff6ae370fe5d/ag91_1_1.jpg">
<style>
.menu.hidden-s3 {
display: flex;
}
@media all and (max-width: 991px) {
#headerlinks {
display: flex;
}
}
.product-view .sticker-container-top-right {
right: 0;
}
#lp22 iframe{
    height: 1900px;
border: 0;
width: 100%;
}

#lp22.ios{
    overflow-y: auto;
    -webkit-overflow-scrolling:touch !important;
    height: 100%;
}

#lp22.ios iframe{
    height: 100%;
    min-width: 100%;
    width: 100px;
    *width: 100%;
}
@media all and (max-width: 460px) {
#lp22 iframe {
height: 2250px;
}
}

.cms-brand-samsung .magestore-bannerslider.pos-side-right,
 .cms-brand-miele .magestore-bannerslider.pos-side-right, .cms-brand-karcher .magestore-bannerslider.pos-side-right, .cms-brand-sony .magestore-bannerslider.pos-side-right, .cms-brand-apple .magestore-bannerslider.pos-side-right, .cms-brand-samsung .magestore-bannerslider.pos-side-left, .cms-brand-miele .magestore-bannerslider.pos-side-left, .cms-brand-karcher .magestore-bannerslider.pos-side-left, .cms-brand-sony .magestore-bannerslider.pos-side-left, .cms-brand-apple .magestore-bannerslider.pos-side-left {
display: none !important;
}
.our-stores .stores-grid .single-store .store-img div {
left: auto !important;
top: auto !important;
right: 30px;
bottom: 30px;
}
.brand-home-index .pos-side-right, .brand-home-index .pos-side-left, .pos-all-side-right, .pos-all-side-left  {
top:0 !important;
margin-top:3px !important;
}
.brand-home-index .pos-side-right.sticky, .brand-home-index .pos-side-left.sticky, .pos-all-side-right.sticky, .pos-all-side-left.sticky {
margin-top: 0 !important;
position: fixed !important;
}
.brand-home-index .pos-side-right.sticky-bottom, .brand-home-index .pos-side-left.sticky-bottom, .pos-all-side-right.sticky-bottom, .pos-all-side-left.sticky-bottom {
margin-top: 0 !important;
position: fixed !important;
bottom: 0 !important;
top: auto !important;
}
.footer {
position: relative;
}
h2.product-name, h3.product-name, h4.product-name, h5.product-name, p.product-name {
height: auto;
}
.five-products-special-slick .productbox-product, .five-products-small .productbox-product {
padding: 0 10px;
}
.five-products-special-slick .productbox-product   
 .product-image, .five-products-small .productbox-product .product-image {
padding: 0 40px;
}
.pos-all-side-left {
  left: 0;
}
.pos-all-side-right {
  right: 0;
}
.pos-all-side-right, .pos-all-side-left {
display: none;
position: absolute;
}
.pos-all-side-right img, .pos-all-side-left img, .pos-side-right img, .pos-side-left img {
height: auto !important;
}
.pos-all-side-right .jquery-slider-navigation, .pos-all-side-left .jquery-slider-navigation {
display: none;
}
.footer {
z-index:2;
}
.pos-category-side-left, .pos-category-side-right{
z-index:1;
}
..popup__basket--accessories {
min-height: none;
}
.products-grid:after {
position: inherit;
}
.single-page .col-1-2  {
	width: 50%;
	float: left;
}
.single-page .col-1-4 {
	width: 25%;
	float: left;
}
.single-page .col-1-3 {
	width: 33.333%;
	float: left;
}
.single-page .text-center {
	text-align: center;
}
.single-page .row::after {
	content: " ";
	display: block;
	clear: both;
}

.single-page h2, .testimonials h2 {
	color: #000 !important;
	text-transform: none;
	font-size: 18px;
	padding-bottom: 20px;
	border-bottom: 1px solid #f2f2f2;
	margin-bottom: 40px !important;
}
.single-page h4 {
	font-size: 16px;
	color: #000;
	margin-bottom: 10px;
	font-weight: bold;
}
.single-page .icons p {
	margin-bottom: 80px;
}
.single-page .col img {
	margin-bottom: 20px;
}
@media all and (max-width: 767px) {
	.col {
		padding-left: 10px !important;
		padding-right: 10px !important;
		width: 100% !important;
	}
	.single-page .icons p {
		margin-bottom: 40px;
	}
}

.testimonials {
	padding: 40px 15px;
	background: #f8f7f7;
	margin-top: 50px;
}
.testimonials p {
	font-size: 14px;

}
.testimonials .item {
	border-left: 8px solid #b71d25;
	background: #FFF;
	width: 100%;
	margin-bottom: 20px;
	padding: 40px 90px 10px 90px;
	position: relative;
}
.testimonials .item::before {
	content: " ";
	display: block;
	width: 28px;
	height: 22px;
	background: url('https://matrixmedia.pl/media/wysiwyg/podstrony/bezpieczenstwo/quotation.png');
	position: absolute;
	top: 26px;
	left: 28px;
}
.testimonials .item .author {
	text-align: right;
}
.testimonials .item .author span {
	color: #808080;
}
.single-page .special-border h4, .single-page .special-border h5{
	color: #b71d25;
	font-size: 18px;
	font-weight: 400;
	margin-bottom: 0;
	margin-top: 0;
}
.single-page .special-border {
	max-width: 560px;
	border: 1px solid #b71d25;
	text-align: center;
	margin: 80px auto;
}
.single-page .special-border h4 {
	padding-left: 30px;
	padding-right: 30px;
	background: #FFF;
	display: inline-block;
	position: relative;
	top: -15px;
}
.single-page .special-border h5 {
	margin-top: -15px;
	margin-bottom: 10px;
}
.single-page .buttons {
	padding-bottom: 60px;
}
.single-page .buttons .button {
	float: none;
display: inline-block;
margin-bottom: 10px;
}
.single-page .bg-gray {
	background: #f8f7f7;
	padding: 50px 15px;
}
.huawei-map {
margin-top: 60px;
}
.huawei-map__left {
width: 35%;
float: left;
padding-right: 20px;
}
.huawei-map__right {
width: 65%;
float: left;
}
.huawei-map::after {
content: " ";
display: block;
clear: both;
}
@media all and (max-width: 480px) {
.huawei-map__left, .huawei-map__right {
width: 100%;
}
}
</style>

<script type="text/javascript"></script>

<link rel="manifest" href="https://matrixmedia.pl/manifest.json">

<script type="text/javascript"></script><script src="./materials1 (25)_files/sw.js" type="text/javascript"></script><noscript><a href="https://www.ceneo.pl/1310-0a" rel="nofollow" target="_blank">Opinie o Nas</a></noscript>
<meta name="google-site-verification" content="i-o8cccJ-wHAZu0-LcN4XpVXjGs693AJG4vuYtuzkgk">



<script async="" src="./materials1 (25)_files/js"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-879551894');
</script><script src="./materials1 (25)_files/f(1).txt"></script><style></style><style>
    #callpage.cp-callpage [data-brand-color="border"],
    #callpage.cp-callpage [data-brand-color^="border |"],
    #callpage.cp-callpage [data-brand-color$="| border"],
    #callpage.cp-callpage [data-brand-color*="| border |"] {
      border-color: #b71d25 !important;
    }
    #callpage.cp-callpage [data-brand-color="stroke"],
    #callpage.cp-callpage [data-brand-color^="stroke |"],
    #callpage.cp-callpage [data-brand-color$="| stroke"],
    #callpage.cp-callpage [data-brand-color*="| stroke |"] {
      stroke: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color="stroke-color"],
    #callpage.cp-callpage [data-brand-color^="stroke-color |"],
    #callpage.cp-callpage [data-brand-color$="| stroke-color"],
    #callpage.cp-callpage [data-brand-color~="stroke-color"] {
      stroke: #b71d25 !important;
      stroke-width: 2px !important;
    }

    #callpage.cp-callpage [data-brand-color="color"],
    #callpage.cp-callpage [data-brand-color^="color |"],
    #callpage.cp-callpage [data-brand-color$="| color"],
    #callpage.cp-callpage [data-brand-color*="| color |"] {
      color: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color="fill"],
    #callpage.cp-callpage [data-brand-color^="fill |"],
    #callpage.cp-callpage [data-brand-color$="| fill"],
    #callpage.cp-callpage [data-brand-color*="| fill |"] {
      fill: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color="fill-inactive"],
    #callpage.cp-callpage [data-brand-color^="fill-inactive |"],
    #callpage.cp-callpage [data-brand-color$="| fill-inactive"],
    #callpage.cp-callpage [data-brand-color*="| fill-inactive |"] {
      fill: #6b6b6b !important;
    }

    #callpage.cp-callpage [data-brand-color="&:checked + background"]:checked + *,
    #callpage.cp-callpage [data-brand-color^="&:checked + background |"]:checked + *,
    #callpage.cp-callpage [data-brand-color$="| &:checked + background"]:checked + *,
    #callpage.cp-callpage [data-brand-color*="| &:checked + background |"]:checked + * {
      background: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color~="background"] {
      background-color: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color~="active-color"] {
      color: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color~="border:focus"]:focus {
      border-color: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color="&:focus + fill"]:focus + *,
    #callpage.cp-callpage [data-brand-color^="&:focus + fill |"]:focus + *,
    #callpage.cp-callpage [data-brand-color$="| &:focus + fill"]:focus + *,
    #callpage.cp-callpage [data-brand-color*="| &:focus + fill |"]:focus + * {
      fill: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color="&:focus + border"]:focus + *,
    #callpage.cp-callpage [data-brand-color^="&:focus + border |"]:focus + *,
    #callpage.cp-callpage [data-brand-color$="| &:focus + border"]:focus + *,
    #callpage.cp-callpage [data-brand-color*="| &:focus + border |"]:focus + * {
      border-color: #b71d25 !important;
    }

    #callpage.cp-callpage [data-brand-color="&:focus svg{fill}"]:focus svg,
    #callpage.cp-callpage [data-brand-color^="&:focus svg{fill} |"]:focus svg,
    #callpage.cp-callpage [data-brand-color$="| &:focus svg{fill}"]:focus svg,
    #callpage.cp-callpage [data-brand-color*="| &:focus svg{fill} |"]:focus svg {
      fill: #b71d25 !important;
    }

    #callpage.cp-callpage .flatpickr-day.selected,
    #callpage.cp-callpage .flatpickr-day.startRange,
    #callpage.cp-callpage .flatpickr-day.endRange,
    #callpage.cp-callpage .flatpickr-day.selected.inRange,
    #callpage.cp-callpage .flatpickr-day.startRange.inRange,
    #callpage.cp-callpage .flatpickr-day.endRange.inRange,
    #callpage.cp-callpage .flatpickr-day.selected:focus,
    #callpage.cp-callpage .flatpickr-day.startRange:focus,
    #callpage.cp-callpage .flatpickr-day.endRange:focus,
    #callpage.cp-callpage .flatpickr-day.selected:hover,
    #callpage.cp-callpage .flatpickr-day.startRange:hover,
    #callpage.cp-callpage .flatpickr-day.endRange:hover,
    #callpage.cp-callpage .flatpickr-day.selected.prevMonthDay,
    #callpage.cp-callpage .flatpickr-day.startRange.prevMonthDay,
    #callpage.cp-callpage .flatpickr-day.endRange.prevMonthDay,
    #callpage.cp-callpage .flatpickr-day.selected.nextMonthDay,
    #callpage.cp-callpage .flatpickr-day.startRange.nextMonthDay,
    #callpage.cp-callpage .flatpickr-day.endRange.nextMonthDay {
      background: #b71d25 !important;
      border-color: #b71d25 !important;
    }

    #callpage.cp-callpage .flatpickr-prev-month:hover svg,
    #callpage.cp-callpage .flatpickr-next-month:hover svg {
      fill: #b71d25 !important;
    }
  </style><link id="cp-styles" href="./materials1 (25)_files/callpage-callback.default.css" rel="stylesheet" type="text/css"><style type="text/css" id="cp-custom-styles">null</style><script src="https://googleads.g.doubleclick.net/pagead/viewthroughconversion/879551894/?random=1619006891212&amp;cv=9&amp;fst=1619006891212&amp;num=1&amp;bg=ffffff&amp;guid=ON&amp;resp=GooglemKTybQhCsO&amp;eid=2505059650&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_his=1&amp;u_tz=120&amp;u_java=false&amp;u_nplug=4&amp;u_nmime=2&amp;gtm=2oa472&amp;sendb=1&amp;ig=1&amp;data=event%3Dgtag.config&amp;frm=0&amp;url=file%3A%2F%2F%2FC%3A%2FUsers%2Fuser%2FPycharmProjects%2FXMLbot%2Fmaterials1%2520(25).html&amp;tiba=Telewizor%20SONY%20KD-77AG9%20%7C%20MatrixMedia.pl&amp;hn=www.googleadservices.com&amp;async=1&amp;rfmt=3&amp;fmt=4"></script></head>

<body class=" catalog-product-view catalog-product-view product-telewizor-sony-kd-77ag9" style="zoom: 1;" cz-shortcut-listen="true"><div id="chat-application" style="display: block; z-index: 2147483647; position: fixed; overflow: hidden; bottom: 24px; left: initial; right: 11px; max-height: 56px; max-width: 200px; height: 56px; width: 200px; background: transparent;"><iframe id="chat-application-iframe" title="Smartsupp" aria-hidden="true" style="width: 100%; height: 100%; border: none; z-index: 10000001;" src="./materials1 (25)_files/saved_resource.html"></iframe></div>

    <div class="modal-fade animate_opacity" style="display: none;">
</div>
<div class="modal-fade-popup animate_opacity">
</div>
    <div class="wrapper">

            <noscript>
        <div class="global-site-notice noscript">
            <div class="notice-inner">
                <p>
                    <strong>Wygląda na to, że JavaScript jest wyłączony w twojej przeglądarce.</strong><br />
                    Musisz mieć uruchomioną obsługę JavaScript w przeglądarce, żeby korzystać z tej witryny.                </p>
            </div>
        </div>
    </noscript>

        <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W9VLJJP"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->


<div id="matrixmedia-popup" class="modal modal-home-matrixmedia">
  <p><img class="main__banner main__banner__desktop" src="./materials1 (25)_files/popup1.png"><img class="main__banner main__banner__mobile" src="./materials1 (25)_files/mobile-popup.png"></p>
  <div class="modal__content">
    <h1>MASZ PYTANIE?</h1>
    <h2>ZADZWOŃ <strong>DO NAS</strong></h2>
    <div class="modal__contact">
      <a href="tel:616427742">61 642 77 42 / </a><a href="tel:519060334">519 060 334</a>
    </div>
    <a class="contact--mail" href="mailto:sklep@matrixmedia.pl">LUB <span>NAPISZ:</span>sklep@matrixmedia.pl</a>
    <div class="contact__content--interactive">
      <div class="modal__contact__single modal__contact__column">
        <span class="js-callback"><img src="./materials1 (25)_files/callbackmatrix.png"></span>
        <div class="socials">
          <span class="js-chat"><img src="./materials1 (25)_files/czatmatrix.png"></span>
          <a target="_blank" href="https://www.facebook.com/matrixmediapl/"><img src="./materials1 (25)_files/messmatrix.png"></a>
        </div>
      </div>
    </div>
  </div>
</div>
<p><a class="js-open-modal" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#matrixmedia-popup" rel="modal:open"></a></p>

<div style="margin-top: 0px;" id="header">
    <div class="container">
        <div class="logo-container">

    
    <a href="https://matrixmedia.pl/" title="">
        <img src="./materials1 (25)_files/logo.png" alt="">
    </a>

    </div>
        <div class="header-container full-s2">

            
            <div class="contact">
    <div class="phone">
        <a href="tel:+48616427742">
            <i class="icon icon-telefon"></i>
            <span>61 642 77 42</span>
        </a>
        <span class="separator hidden-s1">|</span>
        <a class="hidden-s1" href="tel:+48">
            <span></span>
        </a>
    </div>

    <div class="email">
        <a href="mailto:sklep@matrixmedia.pl">
            <i class="icon icon-koperta"></i>
            <span>sklep@matrixmedia.pl</span>
        </a>
    </div>

    <div class="cart-icon">
        <a href="https://matrixmedia.pl/checkout/cart/">
            <i class="icon icon-koszyk"></i>
             <strong></strong>
        </a>
    </div>
</div>

<div class="account">

    <div class="helper__wrapper">
        <img src="./materials1 (25)_files/call-center2.png">
        <span class="help__title">Pomoc i kontakt</span>
        <div class="sub-menu">
          <h4>Popularne tematy</h4>
          <ul>
            <a href="https://matrixmedia.pl/raty/"><li>Jak kupić na raty</li></a>
            <a href="https://matrixmedia.pl/jak-zamowic/"><li>Jak zamówić</li></a>
            <a href="https://matrixmedia.pl/statuszamowien/"><li>Status zamówienia</li></a>
            <a href="https://matrixmedia.pl/sposoby-dostawy/"><li>Sposoby dostawy</li></a>
            <a href="https://matrixmedia.pl/jak-zaplacic/"><li>Jak zapłacić</li></a>
            <a href="https://matrixmedia.pl/gwarancja/"><li>gwarancja</li></a>
          </ul>
          <h4 class="secound">Skontaktuj się z nami</h4>
          <ul class="secound__ul">
            <a href="https://matrixmedia.pl/punkt-odbioru/"><img src="./materials1 (25)_files/redpin.png"><li>Punkty odbioru</li></a>
            <a href="https://matrixmedia.pl/contacts/"><i class="icon icon-telefon"></i><li>Kontakt</li></a>
            <a href="mailto:sklep@matrixmedia.pl"><i class="icon icon-koperta"></i><li>sklep@matrixmedia.pl</li></a>
            <a href="tel:616427742"><i class="icon icon-telefon"></i><li>61 642 77 42</li></a>
          </ul>
        </div>
    </div>

    
    <a href="https://matrixmedia.pl/customer/account/login/">zaloguj się</a>
    <span class="separator">lub</span>
    <a href="https://matrixmedia.pl/customer/account/create/">załóż konto</a>

    
</div>
            <div class="search-container">
                
<form id="search_mini_form" action="https://matrixmedia.pl/catalogsearch/result/" method="get">

    
<input id="search" autocomplete="off" type="text" name="q" value="" class="input-text required-entry" maxlength="128" placeholder="Szukaj tutaj w całym sklepie...">
    <span class="search-border hidden-s3"></span>

    <button class="button">
        <span class="icon icon-lupa"></span>
    </button>

</form>

<select class="hidden-s3" name="qcat" id="search_category" form="search_mini_form">
    <option value="0">wszystkie</option>
        <option value="303">TV i akcesoria RTV</option>
        <option value="383">AGD małe</option>
        <option value="406">Foto i Video</option>
        <option value="431">Smartfony i GPS</option>
        <option value="478">Gaming</option>
        <option value="479">Komputery i Laptopy</option>
        <option value="886">&gt;&gt; Outlet &lt;&lt;</option>
        <option value="1145">Sport i rekreacja</option>
        <option value="1236">Lego</option>
        <option value="1416">AGD</option>
        <option value="1552">Audio</option>
        <option value="1557">Dom i ogród</option>
    </select>
<div class="search-more">T</div>

<div id="SolrSearchList"></div>

<script type="text/javascript">
    jQuery('#search').focus(function () {
        jQuery('.search-container').css('z-index', '9999');
        jQuery(".modal-fade").show();
        if (jQuery(".modal-fade").hasClass('fade-out')) {
            setTimeout(function () {
                jQuery(".modal-fade").show();
            },500);
        }
        jQuery("#SolrSearchList").show();
        jQuery(".modal-fade").click(function () {
            jQuery('.search-container').css('z-index', '99');
            jQuery("#SolrSearchList").hide();
        })
    });
</script>

            </div>

            <div class="wishlist-link hidden-s4">
                <a href="https://matrixmedia.pl/wishlist/" class="fa fa-star-o">
                                    </a>
            </div>

            <div class="compare-icon">
                <a href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#" id="button-compare" compare_url="https://matrixmedia.pl/catalog/product_compare/index/uenc/aHR0cHM6Ly9tYXRyaXhtZWRpYS5wbC90ZWxld2l6b3Itc29ueS1rZC03N2FnOS5odG1s/">
                                    </a>
            </div>

            

<div class="header-minicart">
    <a class="minibasket-link" href="https://matrixmedia.pl/checkout/cart/">
        <i class="icon icon-koszyk"></i>
        <span class="basket-qty count">0</span>
        <span class="basket-label hidden-s4">
            <span class="title">Twój koszyk</span>
            <span class="info-content">
                                    Koszyk jest pusty
                            </span>
        </span>
    </a>
    </div>

            
            <div class="clr"></div>

        </div>

        <div class="clr"></div>

        <!-- Navigation -->

        <div id="headerlinks" class="container">

            <div class="categories">
                <div class="categories-main">
                    <span class="hidden-s2">produkty </span>
                    <div class="hamburger">
                        <i class="icon icon-menu"></i>
                    </div>
                </div>
                
            </div>

              	
	    	
	
	    
	
	    	
	    						<div class="menu hidden-s3">
						<!-- <div class=""><a class="promo-text" href="https://matrixmedia.pl/promocje2/">promocje</a></div> -->
							<div class="expandable">
								<a class="promo-text mpr" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#">strefy marek</a>
									<div>
																																																																			<div class=""><a href="https://matrixmedia.pl/miele/">miele</a></div>
																																																																		</div>
							</div>
							<style><!--
#headerlinks a{font-size: 12px;}
--></style>
<div style="background-color: #b71d25;"><a class="promo-text mpr" href="https://matrixmedia.pl/black-sales/rtv" style="color: #fff;">Jakaś wyprzedaż</a></div>
<div><a class="promo-text mpr" href="https://matrixmedia.pl/sposob-zamawiania">Sposoby zamawiania i rezerwacji</a></div>
<div><a class="promo-text mpr" href="https://matrixmedia.pl/raty">Raty 0 %</a></div>
<div><a class="promo-text mpr" href="https://matrixmedia.pl/contacts">kontakt</a></div>
<div><a class="promo-text mpr" href="https://matrixmedia.pl/punkt-odbioru">Punkty odbioru</a></div>							<!-- <div class="" style="background-color: #b71D25"><a style="color: #FFF;" class="promo-text mpr" href="/oferta-haloween/rtv">WYPRZEDAŻ</a></div>
							<div class=""><a class="promo-text mpr" href="https://matrixmedia.pl/sposob-zamawiania/">Sposoby zamawiania i rezerwacji</a></div>
							<div class=""><a class="promo-text mpr" href="https://matrixmedia.pl/raty/">Raty 0 %</a></div>
							<div class=""><a class="promo-text mpr" href="https://matrixmedia.pl/contacts/">kontakt</a></div>
							<div class=""><a class="promo-text mpr" href="https://matrixmedia.pl/punkt-odbioru/">Punkty odbioru</a></div> -->
					</div>
				<div class="clr">
				</div>
     
 
	
	





        </div>
    </div>
</div>

<div id="header-mobile">
    <div class="container">
                <div class="categories">
            <div class="categories-main">
                <div class="hamburger">
                    <i class="icon icon-menu"></i>
                </div>
            </div>
        </div>
        <div class="logo-container">

    
    <a href="https://matrixmedia.pl/" title="">
        <img src="./materials1 (25)_files/logo.png" alt="">
    </a>

    </div>        <div class="account-nav">
            <div class="account-icon">
                                    <a href="https://matrixmedia.pl/customer/account/login/"><i class="fa fa-user"></i></a>
                            </div>

            <div class="wishlist-icon">
                <a href="https://matrixmedia.pl/wishlist/" class="fa fa-star-o">
                                    </a>
            </div>

            <div class="cart-icon">
                <a href="https://matrixmedia.pl/checkout/cart/" class="fa fa-shopping-cart">
                    <strong></strong>
                </a>
            </div>
        </div>
        <div class="clr"></div>
        <!-- Navigation -->

        <div id="headerlinks" class="container">

            <div class="categories">
                <div id="menu" class="close-on-fade-click" style="">
                    <div class="menu-container">
                        <ul class="mobfirst"><!-- <li class="level0 nav-custom parent mobpage"><a class="mobtext" href="<?php echo $this->getUrl('promocje2') ?>">promocje</a></li> -->
<li class="level0 nav-custom parent mobpage"><a class="mobtext" href="https://matrixmedia.pl/black-sales/rtv">Wiosenne Wyprzedaże</a></li>
<li class="level0 nav-custom parent mobpage"><a class="mobtext" href="https://matrixmedia.pl/nowosci">Nowości</a></li>
<li class="level0 nav-custom parent mobpage"><a class="mobtext" href="https://matrixmedia.pl/statuszamowien">Status zamówienia</a></li>
</ul><ul>       
<li class="level0 nav-1 first parent"><a href="https://matrixmedia.pl/tv.html" title="TV i akcesoria RTV" class="level0 has-children">TV i akcesoria RTV</a><ul class="level0" style=""><li class="level1 nav-1-1 first parent"><a href="https://matrixmedia.pl/tv/telewizory.html" title="Telewizory" class="level1 has-children">Telewizory</a><ul class="level1"><li class="level2 nav-1-1-1 first"><a href="https://matrixmedia.pl/tv/telewizory/do-32-cali.html" title="Do 32 cali" class="level2 ">Do 32 cali</a></li><li class="level2 nav-1-1-2"><a href="https://matrixmedia.pl/tv/telewizory/33-43.html" title="33-43" class="level2 ">33-43</a></li><li class="level2 nav-1-1-3"><a href="https://matrixmedia.pl/tv/telewizory/44-50.html" title="44-50" class="level2 ">44-50</a></li><li class="level2 nav-1-1-4"><a href="https://matrixmedia.pl/tv/telewizory/51-74.html" title="51-74" class="level2 ">51-74</a></li><li class="level2 nav-1-1-5 last"><a href="https://matrixmedia.pl/tv/telewizory/powyzej-75.html" title="Powyżej 75" class="level2 ">Powyżej 75</a></li></ul></li><li class="level1 nav-1-2 last parent"><a href="https://matrixmedia.pl/tv/akcesoria-rtv.html" title="Akcesoria RTV" class="level1 has-children">Akcesoria RTV</a><ul class="level1"><li class="level2 nav-1-2-1 first"><a href="https://matrixmedia.pl/tv/akcesoria-rtv/uchwyty-do-telewizorow.html" title="Uchwyty do telewizorów" class="level2 ">Uchwyty do telewizorów</a></li><li class="level2 nav-1-2-2"><a href="https://matrixmedia.pl/tv/akcesoria-rtv/panele-rtv-stoliki-pod-telewizory.html" title="Panele RTV" class="level2 ">Panele RTV</a></li><li class="level2 nav-1-2-3"><a href="https://matrixmedia.pl/tv/akcesoria-rtv/maskownice.html" title="Maskownice" class="level2 ">Maskownice</a></li><li class="level2 nav-1-2-4"><a href="https://matrixmedia.pl/tv/akcesoria-rtv/kable-przejsciowki-do-tv.html" title="Kable, przejściówki do tv" class="level2 ">Kable, przejściówki do tv</a></li><li class="level2 nav-1-2-5 last"><a href="https://matrixmedia.pl/tv/akcesoria-rtv/inne.html" title="Inne" class="level2 ">Inne</a></li></ul></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/telewizor-sony-kd-65xf8505.html/"><img src="./materials1 (25)_files/65xf8505.png"></a></div></li></ul></li><li class="level0 nav-2 parent"><a href="https://matrixmedia.pl/audio.html" title="Audio" class="level0 has-children">Audio</a><ul class="level0" style=""><li class="level1 nav-2-1 first parent"><a href="https://matrixmedia.pl/audio/kino-domowe.html" title="Kino domowe" class="level1 has-children">Kino domowe</a><ul class="level1"><li class="level2 nav-2-1-1 first"><a href="https://matrixmedia.pl/audio/kino-domowe/odtwarzacze-blu-ray.html" title="Odtwarzacze Blu-Ray" class="level2 ">Odtwarzacze Blu-Ray</a></li><li class="level2 nav-2-1-2"><a href="https://matrixmedia.pl/audio/kino-domowe/soundbary.html" title="Soundbary" class="level2 ">Soundbary</a></li><li class="level2 nav-2-1-3"><a href="https://matrixmedia.pl/audio/kino-domowe/zestawy-kina-domowego.html" title="Zestawy kina domowego" class="level2 ">Zestawy kina domowego</a></li><li class="level2 nav-2-1-4 last"><a href="https://matrixmedia.pl/audio/kino-domowe/amplitunery.html" title="Amplitunery" class="level2 ">Amplitunery</a></li></ul></li><li class="level1 nav-2-2 parent"><a href="https://matrixmedia.pl/audio/glosniki.html" title="Głośniki" class="level1 has-children">Głośniki</a><ul class="level1"><li class="level2 nav-2-2-1 first"><a href="https://matrixmedia.pl/audio/glosniki/podlogowe.html" title="Podłogowe" class="level2 ">Podłogowe</a></li><li class="level2 nav-2-2-2"><a href="https://matrixmedia.pl/audio/glosniki/podstawkowe.html" title="Podstawkowe" class="level2 ">Podstawkowe</a></li><li class="level2 nav-2-2-3"><a href="https://matrixmedia.pl/audio/glosniki/centralne.html" title="Centralne" class="level2 ">Centralne</a></li><li class="level2 nav-2-2-4"><a href="https://matrixmedia.pl/audio/glosniki/subwoofery.html" title="Subwoofery" class="level2 ">Subwoofery</a></li><li class="level2 nav-2-2-5"><a href="https://matrixmedia.pl/audio/glosniki/dolby-atmos.html" title="Dolby Atmos" class="level2 ">Dolby Atmos</a></li><li class="level2 nav-2-2-6 last"><a href="https://matrixmedia.pl/audio/glosniki/zestawy.html" title="Zestawy" class="level2 ">Zestawy</a></li></ul></li><li class="level1 nav-2-3 parent"><a href="https://matrixmedia.pl/audio/stereo.html" title="Stereo" class="level1 has-children">Stereo</a><ul class="level1"><li class="level2 nav-2-3-1 first"><a href="https://matrixmedia.pl/audio/stereo/wzmacniacze.html" title="Wzmacniacze" class="level2 ">Wzmacniacze</a></li><li class="level2 nav-2-3-2"><a href="https://matrixmedia.pl/audio/stereo/gramofony.html" title="Gramofony" class="level2 ">Gramofony</a></li><li class="level2 nav-2-3-3"><a href="https://matrixmedia.pl/audio/stereo/amplitunery.html" title="Amplitunery" class="level2 ">Amplitunery</a></li><li class="level2 nav-2-3-4"><a href="https://matrixmedia.pl/audio/stereo/odtwarzacze-cd-i-sieciowe.html" title="Odtwarzacze CD i sieciowe" class="level2 ">Odtwarzacze CD i sieciowe</a></li><li class="level2 nav-2-3-5 last"><a href="https://matrixmedia.pl/audio/stereo/zestawy.html" title="Zestawy" class="level2 ">Zestawy</a></li></ul></li><li class="level1 nav-2-4 parent"><a href="https://matrixmedia.pl/audio/sluchawki.html" title="Słuchawki" class="level1 has-children">Słuchawki</a><ul class="level1"><li class="level2 nav-2-4-1 first"><a href="https://matrixmedia.pl/audio/sluchawki/nauszne.html" title="Nauszne" class="level2 ">Nauszne</a></li><li class="level2 nav-2-4-2"><a href="https://matrixmedia.pl/audio/sluchawki/douszne.html" title="Douszne" class="level2 ">Douszne</a></li><li class="level2 nav-2-4-3"><a href="https://matrixmedia.pl/audio/sluchawki/przewodowe.html" title="Przewodowe" class="level2 ">Przewodowe</a></li><li class="level2 nav-2-4-4"><a href="https://matrixmedia.pl/audio/sluchawki/bezprzewodowe.html" title="Bezprzewodowe" class="level2 ">Bezprzewodowe</a></li><li class="level2 nav-2-4-5 last"><a href="https://matrixmedia.pl/audio/sluchawki/sportowe.html" title="Sportowe" class="level2 ">Sportowe</a></li></ul></li><li class="level1 nav-2-5 last parent"><a href="https://matrixmedia.pl/audio/audio-przenosne.html" title="Audio przenośne" class="level1 has-children">Audio przenośne</a><ul class="level1"><li class="level2 nav-2-5-1 first"><a href="https://matrixmedia.pl/audio/audio-przenosne/glosniki.html" title="Głośniki" class="level2 ">Głośniki</a></li><li class="level2 nav-2-5-2"><a href="https://matrixmedia.pl/audio/audio-przenosne/mp3-mp4.html" title="MP3/MP4" class="level2 ">MP3/MP4</a></li><li class="level2 nav-2-5-3 last"><a href="https://matrixmedia.pl/audio/audio-przenosne/dyktafony.html" title="Dyktafony" class="level2 ">Dyktafony</a></li></ul></li></ul></li><li class="level0 nav-3 parent"><a href="https://matrixmedia.pl/agd-1.html" title="AGD" class="level0 has-children">AGD</a><ul class="level0" style=""><li class="level1 nav-3-1 first parent"><a href="https://matrixmedia.pl/agd-1/wolnostojace.html" title="Wolnostojące" class="level1 has-children">Wolnostojące</a><ul class="level1"><li class="level2 nav-3-1-1 first"><a href="https://matrixmedia.pl/agd-1/wolnostojace/pralki.html" title="Pralki" class="level2 ">Pralki</a></li><li class="level2 nav-3-1-2"><a href="https://matrixmedia.pl/agd-1/wolnostojace/suszarki.html" title="Suszarki" class="level2 ">Suszarki</a></li><li class="level2 nav-3-1-3"><a href="https://matrixmedia.pl/agd-1/wolnostojace/pralko-suszarki.html" title="Pralko-suszarki" class="level2 ">Pralko-suszarki</a></li><li class="level2 nav-3-1-4"><a href="https://matrixmedia.pl/agd-1/wolnostojace/lodowki.html" title="Lodówki" class="level2 ">Lodówki</a></li><li class="level2 nav-3-1-5"><a href="https://matrixmedia.pl/agd-1/wolnostojace/kuchnie-wolnostojace.html" title="Kuchnie wolnostojące" class="level2 ">Kuchnie wolnostojące</a></li><li class="level2 nav-3-1-6"><a href="https://matrixmedia.pl/agd-1/wolnostojace/zmywarki.html" title="Zmywarki " class="level2 ">Zmywarki </a></li><li class="level2 nav-3-1-7 last"><a href="https://matrixmedia.pl/agd-1/wolnostojace/kuchnie-mikrofalowe.html" title="Kuchnie mikrofalowe" class="level2 ">Kuchnie mikrofalowe</a></li></ul></li><li class="level1 nav-3-2 parent"><a href="https://matrixmedia.pl/agd-1/do-zabudowy.html" title="Do zabudowy" class="level1 has-children">Do zabudowy</a><ul class="level1"><li class="level2 nav-3-2-1 first"><a href="https://matrixmedia.pl/agd-1/do-zabudowy/lodowki.html" title="Lodówki" class="level2 ">Lodówki</a></li><li class="level2 nav-3-2-2"><a href="https://matrixmedia.pl/agd-1/do-zabudowy/zmywarki.html" title="Zmywarki" class="level2 ">Zmywarki</a></li><li class="level2 nav-3-2-3"><a href="https://matrixmedia.pl/agd-1/do-zabudowy/piekarniki.html" title="Piekarniki" class="level2 ">Piekarniki</a></li><li class="level2 nav-3-2-4"><a href="https://matrixmedia.pl/agd-1/do-zabudowy/plyty.html" title="Płyty" class="level2 ">Płyty</a></li><li class="level2 nav-3-2-5"><a href="https://matrixmedia.pl/agd-1/do-zabudowy/kuchenki-mikrofalowe.html" title="Kuchenki mikrofalowe" class="level2 ">Kuchenki mikrofalowe</a></li><li class="level2 nav-3-2-6 last"><a href="https://matrixmedia.pl/agd-1/do-zabudowy/okapy-kuchenne.html" title="Okapy kuchenne" class="level2 ">Okapy kuchenne</a></li></ul></li><li class="level1 nav-3-3 last parent"><a href="https://matrixmedia.pl/agd-1/akcesoria-agd.html" title="Akcesoria AGD" class="level1 has-children">Akcesoria AGD</a><ul class="level1"><li class="level2 nav-3-3-1 first"><a href="https://matrixmedia.pl/agd-1/akcesoria-agd/chemia.html" title="Chemia" class="level2 ">Chemia</a></li><li class="level2 nav-3-3-2 last"><a href="https://matrixmedia.pl/agd-1/akcesoria-agd/inne.html" title="Inne" class="level2 ">Inne</a></li></ul></li></ul></li><li class="level0 nav-4 parent"><a href="https://matrixmedia.pl/agd-male.html" title="AGD małe" class="level0 has-children">AGD małe</a><ul class="level0" style=""><li class="level1 nav-4-1 first parent"><a href="https://matrixmedia.pl/agd-male/sprzatanie.html" title="Sprzątanie" class="level1 has-children">Sprzątanie</a><ul class="level1"><li class="level2 nav-4-1-1 first"><a href="https://matrixmedia.pl/agd-male/sprzatanie/odkurzacze.html" title="Odkurzacze" class="level2 ">Odkurzacze</a></li><li class="level2 nav-4-1-2"><a href="https://matrixmedia.pl/agd-male/sprzatanie/odkurzacze-automatyczne.html" title="Odkurzacze automatyczne" class="level2 ">Odkurzacze automatyczne</a></li><li class="level2 nav-4-1-3"><a href="https://matrixmedia.pl/agd-male/sprzatanie/parownice-i-mopy-parowe.html" title="Parownice i mopy parowe" class="level2 ">Parownice i mopy parowe</a></li><li class="level2 nav-4-1-4"><a href="https://matrixmedia.pl/agd-male/sprzatanie/oczyszczacze.html" title="Oczyszczacze" class="level2 ">Oczyszczacze</a></li><li class="level2 nav-4-1-5"><a href="https://matrixmedia.pl/agd-male/sprzatanie/myjki.html" title="Myjki" class="level2 ">Myjki</a></li><li class="level2 nav-4-1-6"><a href="https://matrixmedia.pl/agd-male/sprzatanie/prasowalnice.html" title="Prasowalnice" class="level2 ">Prasowalnice</a></li><li class="level2 nav-4-1-7"><a href="https://matrixmedia.pl/agd-male/sprzatanie/nianie-i-dzwonki.html" title="Nianie i dzwonki" class="level2 ">Nianie i dzwonki</a></li><li class="level2 nav-4-1-8"><a href="https://matrixmedia.pl/agd-male/sprzatanie/inne.html" title="Inne" class="level2 ">Inne</a></li><li class="level2 nav-4-1-9 last"><a href="https://matrixmedia.pl/agd-male/sprzatanie/worki-i-akcesoria-do-odkurzaczy.html" title="Worki i akcesoria do odkurzaczy" class="level2 ">Worki i akcesoria do odkurzaczy</a></li></ul></li><li class="level1 nav-4-2 parent"><a href="https://matrixmedia.pl/agd-male/kuchnia.html" title="Kuchnia" class="level1 has-children">Kuchnia</a><ul class="level1"><li class="level2 nav-4-2-1 first"><a href="https://matrixmedia.pl/agd-male/kuchnia/ekspresy.html" title="Ekspresy" class="level2 ">Ekspresy</a></li><li class="level2 nav-4-2-2"><a href="https://matrixmedia.pl/agd-male/kuchnia/krajalnice.html" title="Krajalnice" class="level2 ">Krajalnice</a></li><li class="level2 nav-4-2-3"><a href="https://matrixmedia.pl/agd-male/kuchnia/tostery.html" title="Tostery" class="level2 ">Tostery</a></li><li class="level2 nav-4-2-4"><a href="https://matrixmedia.pl/agd-male/kuchnia/mlynki.html" title="Młynki" class="level2 ">Młynki</a></li><li class="level2 nav-4-2-5"><a href="https://matrixmedia.pl/agd-male/kuchnia/blendery-reczne.html" title="Blendery ręczne" class="level2 ">Blendery ręczne</a></li><li class="level2 nav-4-2-6 last"><a href="https://matrixmedia.pl/agd-male/kuchnia/czajniki.html" title="Czajniki" class="level2 ">Czajniki</a></li></ul></li><li class="level1 nav-4-3 parent"><a href="https://matrixmedia.pl/agd-male/uroda-i-zdrowie.html" title="Uroda i zdrowie" class="level1 has-children">Uroda i zdrowie</a><ul class="level1"><li class="level2 nav-4-3-1 first"><a href="https://matrixmedia.pl/agd-male/uroda-i-zdrowie/pielegnacja-wlosow.html" title="Pielęgnacja włosów" class="level2 ">Pielęgnacja włosów</a></li><li class="level2 nav-4-3-2"><a href="https://matrixmedia.pl/agd-male/uroda-i-zdrowie/golenie-i-strzyzenie.html" title="Golenie i strzyżenie" class="level2 ">Golenie i strzyżenie</a></li><li class="level2 nav-4-3-3"><a href="https://matrixmedia.pl/agd-male/uroda-i-zdrowie/alkomaty.html" title="Alkomaty" class="level2 ">Alkomaty</a></li><li class="level2 nav-4-3-4"><a href="https://matrixmedia.pl/agd-male/uroda-i-zdrowie/wentylatory-i-klimatyzatory.html" title="Wentylatory i klimatyzatory" class="level2 ">Wentylatory i klimatyzatory</a></li><li class="level2 nav-4-3-5 last"><a href="https://matrixmedia.pl/agd-male/uroda-i-zdrowie/szczoteczki-soniczne.html" title="Szczoteczki soniczne" class="level2 ">Szczoteczki soniczne</a></li></ul></li><li class="level1 nav-4-4 last"><a href="https://matrixmedia.pl/agd-male/lodowki-turystyczne.html" title="Lodówki turystyczne" class="level1 ">Lodówki turystyczne</a></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/odkurzacz-miele-blizzard-cx1-ecoline.html/"><img src="./materials1 (25)_files/miele-cx1-blizzard.png"></a></div></li></ul></li><li class="level0 nav-5 parent"><a href="https://matrixmedia.pl/smartfony-i-gps.html" title="Smartfony i GPS" class="level0 has-children">Smartfony i GPS</a><ul class="level0" style=""><li class="level1 nav-5-1 first parent"><a href="https://matrixmedia.pl/smartfony-i-gps/smartfony.html" title="Smartfony" class="level1 has-children">Smartfony</a><ul class="level1"><li class="level2 nav-5-1-1 first"><a href="https://matrixmedia.pl/smartfony-i-gps/smartfony/smartfony-z-androidem.html" title="Smartfony z Androidem" class="level2 ">Smartfony z Androidem</a></li><li class="level2 nav-5-1-2 last"><a href="https://matrixmedia.pl/smartfony-i-gps/smartfony/smartfony-z-ios.html" title="Smartfony z iOS" class="level2 ">Smartfony z iOS</a></li></ul></li><li class="level1 nav-5-2 parent"><a href="https://matrixmedia.pl/smartfony-i-gps/smartwatche-i-opaski-sportowe.html" title="Smartwatche i Opaski sportowe" class="level1 has-children">Smartwatche i Opaski sportowe</a><ul class="level1"><li class="level2 nav-5-2-1 first"><a href="https://matrixmedia.pl/smartfony-i-gps/smartwatche-i-opaski-sportowe/smartwatche.html" title="Smartwatche" class="level2 ">Smartwatche</a></li><li class="level2 nav-5-2-2"><a href="https://matrixmedia.pl/smartfony-i-gps/smartwatche-i-opaski-sportowe/zegarki-sportowe.html" title="Zegarki sportowe" class="level2 ">Zegarki sportowe</a></li><li class="level2 nav-5-2-3 last"><a href="https://matrixmedia.pl/smartfony-i-gps/smartwatche-i-opaski-sportowe/opaski-sportowe.html" title="Opaski sportowe" class="level2 ">Opaski sportowe</a></li></ul></li><li class="level1 nav-5-3"><a href="https://matrixmedia.pl/smartfony-i-gps/smarthome.html" title="Smarthome" class="level1 ">Smarthome</a></li><li class="level1 nav-5-4 parent"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm.html" title="Akcesoria GSM" class="level1 has-children">Akcesoria GSM</a><ul class="level1"><li class="level2 nav-5-4-1 first"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/etui-i-obudowy.html" title="Etui i obudowy" class="level2 ">Etui i obudowy</a></li><li class="level2 nav-5-4-2"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/ladowarki.html" title="Ładowarki" class="level2 ">Ładowarki</a></li><li class="level2 nav-5-4-3"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/szkla-hartowane-i-folie-ochronne.html" title="Szkła hartowane i folie ochronne" class="level2 ">Szkła hartowane i folie ochronne</a></li><li class="level2 nav-5-4-4"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/karty-pamieci.html" title="Karty pamięci" class="level2 ">Karty pamięci</a></li><li class="level2 nav-5-4-5"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/powerbanki.html" title="Powerbanki" class="level2 ">Powerbanki</a></li><li class="level2 nav-5-4-6"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/glosniki-przenosne.html" title="Głośniki przenośne" class="level2 ">Głośniki przenośne</a></li><li class="level2 nav-5-4-7"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/sluchawki-do-rozmow.html" title="Słuchawki do rozmów" class="level2 ">Słuchawki do rozmów</a></li><li class="level2 nav-5-4-8"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/okulary-vr.html" title="Okulary VR" class="level2 ">Okulary VR</a></li><li class="level2 nav-5-4-9"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/uchwyty-samochodowe.html" title="Uchwyty samochodowe" class="level2 ">Uchwyty samochodowe</a></li><li class="level2 nav-5-4-10"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/akcesoria-do-smartwatchy-i-opasek.html" title="Akcesoria do Smartwatchy i opasek" class="level2 ">Akcesoria do Smartwatchy i opasek</a></li><li class="level2 nav-5-4-11 last parent"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/akcesoria-do-tabletow.html" title="Akcesoria do tabletów" class="level2 has-children">Akcesoria do tabletów</a><ul class="level2"><li class="level3 nav-5-4-11-1 first"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/akcesoria-do-tabletow/etui-na-tablety.html" title="Etui na tablety" class="level3 ">Etui na tablety</a></li><li class="level3 nav-5-4-11-2"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/akcesoria-do-tabletow/karty-pamieci-do-tabletow.html" title="Karty pamięci do tabletów" class="level3 ">Karty pamięci do tabletów</a></li><li class="level3 nav-5-4-11-3 last"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-gsm/akcesoria-do-tabletow/powerbanki-do-tabletow.html" title="Powerbanki do tabletów" class="level3 ">Powerbanki do tabletów</a></li></ul></li></ul></li><li class="level1 nav-5-5 parent"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-samochodowe.html" title="Akcesoria samochodowe" class="level1 has-children">Akcesoria samochodowe</a><ul class="level1"><li class="level2 nav-5-5-1 first"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-samochodowe/alkomaty.html" title="Alkomaty" class="level2 ">Alkomaty</a></li><li class="level2 nav-5-5-2"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-samochodowe/rejestratory-jazdy.html" title="Rejestratory jazdy" class="level2 ">Rejestratory jazdy</a></li><li class="level2 nav-5-5-3 last parent"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-samochodowe/nawigacje-gps.html" title="Nawigacje GPS" class="level2 has-children">Nawigacje GPS</a><ul class="level2"><li class="level3 nav-5-5-3-1 first"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-samochodowe/nawigacje-gps/nawigacje-samochodowe.html" title="Nawigacje samochodowe" class="level3 ">Nawigacje samochodowe</a></li><li class="level3 nav-5-5-3-2 last"><a href="https://matrixmedia.pl/smartfony-i-gps/akcesoria-samochodowe/nawigacje-gps/nawigacje-turystyczne.html" title="Nawigacje turystyczne" class="level3 ">Nawigacje turystyczne</a></li></ul></li></ul></li><li class="level1 nav-5-6 last"><a href="https://matrixmedia.pl/smartfony-i-gps/telefony-komorkowe.html" title="Telefony komórkowe" class="level1 ">Telefony komórkowe</a></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/smartfon-samsung-galaxy-s10-sm-g973f-128gb-prism-green.html/"><img src="./materials1 (25)_files/g970.png"></a></div></li></ul></li><li class="level0 nav-6 parent"><a href="https://matrixmedia.pl/komputery.html" title="Komputery i Laptopy" class="level0 has-children">Komputery i Laptopy</a><ul class="level0" style=""><li class="level1 nav-6-1 first"><a href="https://matrixmedia.pl/komputery/tablet-y.html" title="Tablety" class="level1 ">Tablety</a></li><li class="level1 nav-6-2"><a href="https://matrixmedia.pl/komputery/monitory.html" title="Monitory" class="level1 ">Monitory</a></li><li class="level1 nav-6-3"><a href="https://matrixmedia.pl/komputery/laptopy.html" title="Laptopy" class="level1 ">Laptopy</a></li><li class="level1 nav-6-4"><a href="https://matrixmedia.pl/komputery/aio.html" title="AIO" class="level1 ">AIO</a></li><li class="level1 nav-6-5"><a href="https://matrixmedia.pl/komputery/dyski.html" title="Dyski" class="level1 ">Dyski</a></li><li class="level1 nav-6-6 last parent"><a href="https://matrixmedia.pl/komputery/akcesoria-do-komputerow.html" title="Akcesoria do komputerów" class="level1 has-children">Akcesoria do komputerów</a><ul class="level1"><li class="level2 nav-6-6-1 first"><a href="https://matrixmedia.pl/komputery/akcesoria-do-komputerow/klawiatury-komputerowe.html" title="Klawiatury komputerowe" class="level2 ">Klawiatury komputerowe</a></li><li class="level2 nav-6-6-2"><a href="https://matrixmedia.pl/komputery/akcesoria-do-komputerow/myszki-komputerowe.html" title="Myszki komputerowe" class="level2 ">Myszki komputerowe</a></li><li class="level2 nav-6-6-3 last parent"><a href="https://matrixmedia.pl/komputery/akcesoria-do-komputerow/akcesoria-gamingowe.html" title="Akcesoria Gamingowe" class="level2 has-children">Akcesoria Gamingowe</a><ul class="level2"><li class="level3 nav-6-6-3-1 first"><a href="https://matrixmedia.pl/komputery/akcesoria-do-komputerow/akcesoria-gamingowe/gamepady.html" title="Gamepady" class="level3 ">Gamepady</a></li><li class="level3 nav-6-6-3-2"><a href="https://matrixmedia.pl/komputery/akcesoria-do-komputerow/akcesoria-gamingowe/joysticki.html" title="Joysticki" class="level3 ">Joysticki</a></li><li class="level3 nav-6-6-3-3 last"><a href="https://matrixmedia.pl/komputery/akcesoria-do-komputerow/akcesoria-gamingowe/kierownice.html" title="Kierownice" class="level3 ">Kierownice</a></li></ul></li></ul></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/laptop-lenovo-ideapad-13-3-720s-13ikb-i7-8550-8gb-256gb-win10-81bv002tpb.html/"><img src="./materials1 (25)_files/ideapad-720s.png"></a></div></li></ul></li><li class="level0 nav-7 parent"><a href="https://matrixmedia.pl/sport-i-rekreacja.html" title="Sport i rekreacja" class="level0 has-children">Sport i rekreacja</a><ul class="level0" style=""><li class="level1 nav-7-1 first"><a href="https://matrixmedia.pl/sport-i-rekreacja/deskorolki.html" title="Deskorolki elektryczne" class="level1 ">Deskorolki elektryczne</a></li><li class="level1 nav-7-2"><a href="https://matrixmedia.pl/sport-i-rekreacja/hulajnogi-elektryczne.html" title="Hulajnogi elektryczne" class="level1 ">Hulajnogi elektryczne</a></li><li class="level1 nav-7-3 parent"><a href="https://matrixmedia.pl/sport-i-rekreacja/kamery-sportowe.html" title="Kamery sportowe" class="level1 has-children">Kamery sportowe</a><ul class="level1"><li class="level2 nav-7-3-1 first last"><a href="https://matrixmedia.pl/sport-i-rekreacja/kamery-sportowe/akcesoria-do-kamer-sportowych.html" title="Akcesoria do kamer sportowych" class="level2 ">Akcesoria do kamer sportowych</a></li></ul></li><li class="level1 nav-7-4 parent"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria.html" title="Drony i akcesoria" class="level1 has-children">Drony i akcesoria</a><ul class="level1"><li class="level2 nav-7-4-1 first"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria/drony.html" title="Drony" class="level2 ">Drony</a></li><li class="level2 nav-7-4-2 last parent"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria/akesoria-do-dronow.html" title="Akcesoria do dronów" class="level2 has-children">Akcesoria do dronów</a><ul class="level2"><li class="level3 nav-7-4-2-1 first"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria/akesoria-do-dronow/akcesoria-ochronne-i-obudowy.html" title="Akcesoria ochronne i obudowy" class="level3 ">Akcesoria ochronne i obudowy</a></li><li class="level3 nav-7-4-2-2"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria/akesoria-do-dronow/etui-walizki-i-pokrowce.html" title="Etui, walizki i pokrowce" class="level3 ">Etui, walizki i pokrowce</a></li><li class="level3 nav-7-4-2-3"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria/akesoria-do-dronow/filtry.html" title="Filtry" class="level3 ">Filtry</a></li><li class="level3 nav-7-4-2-4"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria/akesoria-do-dronow/smigla.html" title="Śmigła" class="level3 ">Śmigła</a></li><li class="level3 nav-7-4-2-5 last"><a href="https://matrixmedia.pl/sport-i-rekreacja/drony-i-akcesoria/akesoria-do-dronow/pozostale.html" title="Pozostałe" class="level3 ">Pozostałe</a></li></ul></li></ul></li><li class="level1 nav-7-5"><a href="https://matrixmedia.pl/sport-i-rekreacja/akcesoria.html" title="Akcesoria do deskorolek elektrycznych" class="level1 ">Akcesoria do deskorolek elektrycznych</a></li><li class="level1 nav-7-6"><a href="https://matrixmedia.pl/sport-i-rekreacja/gimbale-i-stabilizatory.html" title="Gimbale i stabilizatory" class="level1 ">Gimbale i stabilizatory</a></li><li class="level1 nav-7-7"><a href="https://matrixmedia.pl/sport-i-rekreacja/sluchawki-sportowe.html" title="Słuchawki sportowe" class="level1 ">Słuchawki sportowe</a></li><li class="level1 nav-7-8"><a href="https://matrixmedia.pl/sport-i-rekreacja/zegarki-sportowe.html" title="Zegarki sportowe" class="level1 ">Zegarki sportowe</a></li><li class="level1 nav-7-9"><a href="https://matrixmedia.pl/sport-i-rekreacja/audio-przenosne.html" title="Audio przenośne" class="level1 ">Audio przenośne</a></li><li class="level1 nav-7-10"><a href="https://matrixmedia.pl/sport-i-rekreacja/samochody-elektryczne.html" title="Samochody elektryczne" class="level1 ">Samochody elektryczne</a></li><li class="level1 nav-7-11 last"><a href="https://matrixmedia.pl/sport-i-rekreacja/zabawki.html" title="Zabawki" class="level1 ">Zabawki</a></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/deskorolka-skymaster-wheels-11-bt-glosnik-smart-dual-2019-czarno-czerwona.html/"><img src="./materials1 (25)_files/sport-i-rekreacja.png"></a></div></li></ul></li><li class="level0 nav-8 parent"><a href="https://matrixmedia.pl/gaming.html" title="Gaming" class="level0 has-children">Gaming</a><ul class="level0" style=""><li class="level1 nav-8-1 first parent"><a href="https://matrixmedia.pl/gaming/playstation.html" title="PlayStation" class="level1 has-children">PlayStation</a><ul class="level1"><li class="level2 nav-8-1-1 first"><a href="https://matrixmedia.pl/gaming/playstation/konsole.html" title="Konsole" class="level2 ">Konsole</a></li><li class="level2 nav-8-1-2"><a href="https://matrixmedia.pl/gaming/playstation/gry.html" title="Gry" class="level2 ">Gry</a></li><li class="level2 nav-8-1-3 last"><a href="https://matrixmedia.pl/gaming/playstation/akcesoria.html" title="Akcesoria" class="level2 ">Akcesoria</a></li></ul></li><li class="level1 nav-8-2 parent"><a href="https://matrixmedia.pl/gaming/nintendo.html" title="Nintendo" class="level1 has-children">Nintendo</a><ul class="level1"><li class="level2 nav-8-2-1 first"><a href="https://matrixmedia.pl/gaming/nintendo/konsole.html" title="Konsole" class="level2 ">Konsole</a></li><li class="level2 nav-8-2-2"><a href="https://matrixmedia.pl/gaming/nintendo/gry-na-switch.html" title="Gry na Switch" class="level2 ">Gry na Switch</a></li><li class="level2 nav-8-2-3"><a href="https://matrixmedia.pl/gaming/nintendo/gry-na-3ds.html" title="Gry na 3DS" class="level2 ">Gry na 3DS</a></li><li class="level2 nav-8-2-4"><a href="https://matrixmedia.pl/gaming/nintendo/figurki-amiibo.html" title="Figurki Amiibo" class="level2 ">Figurki Amiibo</a></li><li class="level2 nav-8-2-5 last"><a href="https://matrixmedia.pl/gaming/nintendo/akcesoria.html" title="Akcesoria" class="level2 ">Akcesoria</a></li></ul></li><li class="level1 nav-8-3 last parent"><a href="https://matrixmedia.pl/gaming/xbox.html" title="Xbox" class="level1 has-children">Xbox</a><ul class="level1"><li class="level2 nav-8-3-1 first"><a href="https://matrixmedia.pl/gaming/xbox/konsole.html" title="Konsole" class="level2 ">Konsole</a></li><li class="level2 nav-8-3-2 last"><a href="https://matrixmedia.pl/gaming/xbox/akcesoria.html" title="Akcesoria" class="level2 ">Akcesoria</a></li></ul></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/konsola-nintendo-switch-red-blue-joy-con.html/"><img src="./materials1 (25)_files/switch-neon.png"></a></div></li></ul></li><li class="level0 nav-9 parent"><a href="https://matrixmedia.pl/fotov2.html" title="Foto i Video" class="level0 has-children">Foto i Video</a><ul class="level0" style=""><li class="level1 nav-9-1 first parent"><a href="https://matrixmedia.pl/fotov2/aparaty-cyfrowe.html" title="Aparaty cyfrowe" class="level1 has-children">Aparaty cyfrowe</a><ul class="level1"><li class="level2 nav-9-1-1 first"><a href="https://matrixmedia.pl/fotov2/aparaty-cyfrowe/kompaktowe.html" title="Kompaktowe" class="level2 ">Kompaktowe</a></li><li class="level2 nav-9-1-2"><a href="https://matrixmedia.pl/fotov2/aparaty-cyfrowe/lustrzanki.html" title="Lustrzanki" class="level2 ">Lustrzanki</a></li><li class="level2 nav-9-1-3 last"><a href="https://matrixmedia.pl/fotov2/aparaty-cyfrowe/bezlusterkowce.html" title="Bezlusterkowce" class="level2 ">Bezlusterkowce</a></li></ul></li><li class="level1 nav-9-2 parent"><a href="https://matrixmedia.pl/fotov2/kamery.html" title="Kamery" class="level1 has-children">Kamery</a><ul class="level1"><li class="level2 nav-9-2-1 first"><a href="https://matrixmedia.pl/fotov2/kamery/cyfrowe.html" title="Cyfrowe" class="level2 ">Cyfrowe</a></li><li class="level2 nav-9-2-2 last"><a href="https://matrixmedia.pl/fotov2/kamery/360st.html" title="360st." class="level2 ">360st.</a></li></ul></li><li class="level1 nav-9-3 parent"><a href="https://matrixmedia.pl/fotov2/optyka.html" title="Optyka" class="level1 has-children">Optyka</a><ul class="level1"><li class="level2 nav-9-3-1 first"><a href="https://matrixmedia.pl/fotov2/optyka/obiektywy.html" title="Obiektywy" class="level2 ">Obiektywy</a></li><li class="level2 nav-9-3-2"><a href="https://matrixmedia.pl/fotov2/optyka/filtry.html" title="Filtry" class="level2 ">Filtry</a></li><li class="level2 nav-9-3-3 last"><a href="https://matrixmedia.pl/fotov2/optyka/oslony.html" title="Osłony" class="level2 ">Osłony</a></li></ul></li><li class="level1 nav-9-4 last parent"><a href="https://matrixmedia.pl/fotov2/akcesoria-do-foto-i-kamer.html" title="Akcesoria do foto i kamer" class="level1 has-children">Akcesoria do foto i kamer</a><ul class="level1"><li class="level2 nav-9-4-1 first"><a href="https://matrixmedia.pl/fotov2/akcesoria-do-foto-i-kamer/karty-pamieci.html" title="Karty pamięci" class="level2 ">Karty pamięci</a></li><li class="level2 nav-9-4-2"><a href="https://matrixmedia.pl/fotov2/akcesoria-do-foto-i-kamer/torby.html" title="Torby" class="level2 ">Torby</a></li><li class="level2 nav-9-4-3"><a href="https://matrixmedia.pl/fotov2/akcesoria-do-foto-i-kamer/statywy-trojnogi.html" title="Statywy, trójnogi" class="level2 ">Statywy, trójnogi</a></li><li class="level2 nav-9-4-4"><a href="https://matrixmedia.pl/fotov2/akcesoria-do-foto-i-kamer/akumulatory.html" title="Akumulatory" class="level2 ">Akumulatory</a></li><li class="level2 nav-9-4-5"><a href="https://matrixmedia.pl/fotov2/akcesoria-do-foto-i-kamer/ladowarki.html" title="Ładowarki" class="level2 ">Ładowarki</a></li><li class="level2 nav-9-4-6 last"><a href="https://matrixmedia.pl/fotov2/akcesoria-do-foto-i-kamer/inne.html" title="Inne" class="level2 ">Inne</a></li></ul></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/aparat-sony-ilce-7m3.html/"><img src="./materials1 (25)_files/sony-ilce7m3.png"></a></div></li></ul></li><li class="level0 nav-10 parent"><a href="https://matrixmedia.pl/dom-i-ogrod.html" title="Dom i ogród" class="level0 has-children">Dom i ogród</a><ul class="level0" style=""><li class="level1 nav-10-1 first last parent"><a href="https://matrixmedia.pl/dom-i-ogrod/ogrod.html" title="Ogród" class="level1 has-children">Ogród</a><ul class="level1"><li class="level2 nav-10-1-1 first parent"><a href="https://matrixmedia.pl/dom-i-ogrod/ogrod/elektronarzedzia.html" title="Elektronarzędzia" class="level2 has-children">Elektronarzędzia</a><ul class="level2"><li class="level3 nav-10-1-1-1 first"><a href="https://matrixmedia.pl/dom-i-ogrod/ogrod/elektronarzedzia/akumulatorowe.html" title="Akumulatorowe" class="level3 ">Akumulatorowe</a></li><li class="level3 nav-10-1-1-2 last"><a href="https://matrixmedia.pl/dom-i-ogrod/ogrod/elektronarzedzia/przewodowe.html" title="Przewodowe" class="level3 ">Przewodowe</a></li></ul></li><li class="level2 nav-10-1-2 last"><a href="https://matrixmedia.pl/dom-i-ogrod/ogrod/narzedzia-spalinowe.html" title="Narzędzia spalinowe" class="level2 ">Narzędzia spalinowe</a></li></ul></li></ul></li><li class="level0 nav-11 parent"><a href="https://matrixmedia.pl/lego.html" title="Lego" class="level0 has-children">Lego</a><ul class="level0" style=""><li class="level1 nav-11-1 first last"><a href="https://matrixmedia.pl/lego/lego-technic.html" title="Lego Technic" class="level1 ">Lego Technic</a></li></ul></li><li class="level0 nav-12 last parent"><a href="https://matrixmedia.pl/outlet-2.html" title=">> Outlet <<" class="level0 has-children">&gt;&gt; Outlet &lt;&lt;</a><ul class="level0" style=""><li class="level1 nav-12-1 first"><a href="https://matrixmedia.pl/outlet-2/telefony-i-tablety.html" title="Smartfony i tablety" class="level1 ">Smartfony i tablety</a></li><li class="level1 nav-12-2 last parent"><a href="https://matrixmedia.pl/outlet-2/telewizory.html" title="Telewizory i RTV" class="level1 has-children">Telewizory i RTV</a><ul class="level1"><li class="level2 nav-12-2-1 first last"><a href="https://matrixmedia.pl/outlet-2/telewizory/telewizory.html" title="Telewizory" class="level2 ">Telewizory</a></li></ul></li><li class="menubanner menubanner-0"><div><a href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html"><img src="./materials1 (25)_files/transparent.png"></a></div></li></ul></li><div class="hidden-md-up">
    
<li class="level0 nav-custom nav-strefa-marek parent">
        <a class="wkwww" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#">strefy marek</a>
        <ul class="" style="display: none;">
                            <li class=""><a href="https://matrixmedia.pl/samsung/">samsung</a></li>
                            <li class=""><a href="https://matrixmedia.pl/sony/">sony</a></li>
                            <li class=""><a href="https://matrixmedia.pl/miele/">miele</a></li>
                            <li class=""><a href="https://matrixmedia.pl/apple/">apple</a></li>
                            <li class=""><a href="https://matrixmedia.pl/dji/">dji</a></li>
                    </ul>
    </li>
    <li class="level0 nav-custom parent"><a class="wkwww" href="https://matrixmedia.pl/contacts/">kontakt</a></li>
   
    <li class="level0 nav-custom parent"><a class="wkwww" href="https://matrixmedia.pl/punkt-odbioru/">punkty odbioru</a></li>
 </div>
    </ul>
   
			
				<div style="background:#f5f4f5!important;" class="menu-promo">
			<a href="https://matrixmedia.pl/contacts"><img src="./materials1 (25)_files/desktopglowny2.png"></a>
<!--<a href="/swieta/rtv"><lottie-player src="/files/home/wielkanoc.json" background="transparent" speed="1" style="width: 100%; height: auto;" loop autoplay></lottie-player></a>
-->

<!--<a href="#"><img src="https://matrixmedia.pl/media/wysiwyg/pasage/negocjacje.png" /></a>--><!-- 			<video width="962" height="348" muted autoplay loop>
				<source src="/files/movie/matrix.mp4" type="video/mp4">
			</video> -->
		</div>
				
	                    </div>
                </div>
            </div>
        </div>
        <div class="search hidden-md-up">
            
<form id="search_mini_form" action="https://matrixmedia.pl/catalogsearch/result/" method="get">

    
<input id="search" autocomplete="off" type="text" name="q" value="" class="input-text required-entry mobile" maxlength="128" placeholder="Szukaj tutaj w całym sklepie...">
    <span class="search-border hidden-s3"></span>

    <button class="button">
        <span class="icon icon-lupa"></span>
    </button>

</form>


<select class="hidden-s3" name="qcat" id="search_category" form="search_mini_form">
    <option value="0">wszystkie</option>
        <option value="303">TV i akcesoria RTV</option>
        <option value="383">AGD małe</option>
        <option value="406">Foto i Video</option>
        <option value="431">Smartfony i GPS</option>
        <option value="478">Gaming</option>
        <option value="479">Komputery i Laptopy</option>
        <option value="886">&gt;&gt; Outlet &lt;&lt;</option>
        <option value="1145">Sport i rekreacja</option>
        <option value="1236">Lego</option>
        <option value="1416">AGD</option>
        <option value="1552">Audio</option>
        <option value="1557">Dom i ogród</option>
    </select>
<div class="search-more">T</div>

<div id="SolrSearchList"></div>

<script type="text/javascript">
    showSearch();
    jQuery(window).resize(function() {
        showSearch();
    });
    function showSearch() {
        if(jQuery('#header:visible').length == 0){
            jQuery('#header .search-container').hide();
        } else {
            jQuery('#header .search-container').show();
        }
    }
    jQuery('#search.mobile').focus(function () {
        jQuery('#header-mobile .search').css('z-index', '9999');
        jQuery(".modal-fade").show();
        if (jQuery(".modal-fade").hasClass('fade-out')) {
            setTimeout(function () {
                jQuery(".modal-fade").show();
            },500);
        }
        jQuery("#header-mobile  #SolrSearchList").show();
        jQuery(".modal-fade").click(function () {
            jQuery('#header-mobile .search').css('z-index', '99');
            jQuery("#header-mobile #SolrSearchList").hide();
        })
    });
</script>


        </div>
								


    </div>
</div>	
		  
		  
<script>
    pageFocus();
    function pageFocus() {
        // check if browser window has focus
        var notIE = (document.documentMode === undefined),
                isChromium = window.chrome;

        if (notIE && !isChromium) {

            // checks for Firefox and other  NON IE Chrome versions
            jQuery(window).on("focusin", function () {

                // tween resume() code goes here
                setTimeout(function () {
                    brandStoreCookie()
                }, 300);

            })

        } else {

            // checks for IE and Chromium versions
            if (window.addEventListener) {

                // bind focus event
                window.addEventListener("focus", function (event) {

                    // tween resume() code goes here
                    setTimeout(function () {
                        brandStoreCookie()
                    }, 300);

                }, false);

            } else {

                // bind focus event
                window.attachEvent("focus", function (event) {

                    // tween resume() code goes here
                    setTimeout(function () {
                        brandStoreCookie()
                    }, 10);

                });
            }
        }
    }
    function brandStoreCookie() {

        setTimeout(function () {
            var archiveCookie = "";
            var actualCookie = Cookies.get('brandstore_id') != undefined ? Cookies.get('brandstore_id') : '';
            if (archiveCookie != actualCookie) {
                location.href = 'https://matrixmedia.pl/';
            }
        }, 300);
    }

    function addComparedDataMobile(data) {
        jQuery('#header-mobile').append(data);
        jQuery('#products-comparison').slideDown(700);
    }

    function addComparedData(data) {
        jQuery('#header').append(data);
        jQuery('#products-comparison').slideDown(700);
    }

    jQuery('#header-mobile #button-compare').click(function () {
        jQuery('.modal-fade').show();
        jQuery('html, body').animate({scrollTop: 0}, 1500);
        jQuery.ajax({
            url: 'https://matrixmedia.pl/catalog/product_compare/index/uenc/aHR0cHM6Ly9tYXRyaXhtZWRpYS5wbC90ZWxld2l6b3Itc29ueS1rZC03N2FnOS5odG1s/',
            success: function (data) {
                addComparedDataMobile(data);
            }
        });
    })

    jQuery('#header #button-compare').click(function () {
        jQuery('.modal-fade').show();
        jQuery('html, body').animate({scrollTop: 0}, 1500);
        jQuery.ajax({
            url: 'https://matrixmedia.pl/catalog/product_compare/index/uenc/aHR0cHM6Ly9tYXRyaXhtZWRpYS5wbC90ZWxld2l6b3Itc29ueS1rZC03N2FnOS5odG1s/',
            success: function (data) {
                addComparedData(data);
            }
        });
    })
</script>
		
        <div class="container">
            <div class="breadcrumbs">
    <ul>
                                    <li class="home">
                    <a href="https://matrixmedia.pl/"><i class="icon icon-beadcrumbs-domek"></i></a>
                </li>
                                        <i class="icon icon-strzalka"></i>
                        
                                    <li class="TV i akcesoria RTV">
                                    <a href="https://matrixmedia.pl/tv.html" title="TV i akcesoria RTV">TV i akcesoria RTV</a>
                                                        <i class="icon icon-strzalka"></i>
                        </li>
                                    <li class="Telewizory">
                                    <a href="https://matrixmedia.pl/tv/telewizory.html" title="Telewizory">Telewizory</a>
                                                        <i class="icon icon-strzalka"></i>
                        </li>
                                    <li class="Powyżej 75">
                                    <a href="https://matrixmedia.pl/tv/telewizory/powyzej-75.html" title="Powyżej 75">Powyżej 75</a>
                                                        <i class="icon icon-strzalka"></i>
                        </li>
                                    <li class="Telewizor SONY KD-77AG9">
                                    Telewizor SONY KD-77AG9                                                    </li>
            </ul>
</div>
 </div>
	



        <div class="container">

                                </div>

        <div class="container col1-layout">
         
 

<script type="text/javascript">
    var optionsPrice = new Product.OptionsPrice([]);
</script>
<div id="messages_product_view"></div>
<style>

#menu {
display: none;
}
@media (min-width: 621px) {
    .bundle-discount-container:nth-child(-n+3) {
        border-width: 2px;
        height: auto !important;
        opacity: 1 !important;
        overflow: hidden;
    }
.leaselinkCalucalteButtonContainerPRO a::after{display:none !important;}
.leaselinkCalucalteButtonContainerPRO {padding:0 !important;}
</style><div class="product-view">

    
    <div class="product-essential">
        <form action="https://matrixmedia.pl/checkout/cart/add/uenc/aHR0cHM6Ly9tYXRyaXhtZWRpYS5wbC90ZWxld2l6b3Itc29ueS1rZC03N2FnOS5odG1sP19fX1NJRD1V/product/18787/form_key/ymiCK4gdBaA2WB1b/" method="post" id="product_addtocart_form">

            <div class="product-top">
                <div class="product-name">
                    <h1 class="h1">""" + full_product['name'] + """</h1>
</div>
<div class="ratings">
<div class="stars">
<div class="active_stars_wrapper" style="width:0%">
<div class="active_stars"></div>
</div>
</div>
<p class="rating-links">
<a class="link_users_review" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#reviews">Opinie użytkowników (0)</a>
<span class="separator">|</span>
<a class="link_add_review" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#productreview">Dodaj opinię</a>
</p>
</div>

<div class="product-share">
<p class="share-text">Podziel się</p>
<ul class="sharing-links">

<li>
<a href="http://www.facebook.com/sharer.php?s=100&amp;p[url]=https%3A%2F%2Fmatrixmedia.pl%2Ftelewizor-sony-kd-77ag9.html%3F___SID%3DU&amp;p[images][0]=https%3A%2F%2Fmatrixmedia.pl%2Fmedia%2Fcatalog%2Fproduct%2Fcache%2F1%2Fimage%2F85e4522595efc69f496374d01ef2bf13%2Fa%2Fg%2Fag91_1_1.jpg&amp;p[title]=Telewizor+SONY+KD-77AG9&amp;p[summary]=%3Cul%3E%3Cbr+%2F%3E%0D%0A%3Cli%3E4K+High+Dynamic+Range%3C%2Fli%3E%3Cbr+%2F%3E%0D%0A%3Cli%3EProcesor+obrazu+X1%26trade%3B+Ultimate%3C%2Fli%3E%3Cbr+%2F%3E%0D%0A%3Cli%3EAcoustic+Surface+Audio%2B%26trade%3B%3C%2Fli%3E%3Cbr+%2F%3E%0D%0A%3Cli%3EAndroid+TV%26trade%3B%3C%2Fli%3E%3Cbr+%2F%3E%0D%0A%3C%2Ful%3E" target="_blank" title="Share on Facebook" class="link-facebook">
Udostępnij na Facebooku            </a>
</li>
<li>
<a href="http://twitter.com/home?status=Telewizor+SONY+KD-77AG9+https%3A%2F%2Fmatrixmedia.pl%2Ftelewizor-sony-kd-77ag9.html%3F___SID%3DU" target="_blank" title="Udostępnij na Twitterze" class="link-twitter">Udostępnij na Twitterze</a>
</li>
</ul>
</div>
</div>

<input name="form_key" type="hidden" value="ymiCK4gdBaA2WB1b">
<div class="no-display">
<input type="hidden" name="product" value="18787">
<input type="hidden" name="related_product" id="related-products-field" value="">
</div>

<div class="">

<div class="product-img-box">
<div class="product-image product-image-zoom zoom-available">
<div class="product-image-gallery">
""" + f"""<img id="image-main" class="gallery-image visible" src="./bin/{full_product['product_folder_name_in']}/product_imgs/{full_product['imgs'][0]}" alt="Telewizor SONY KD-77AG9" title="Telewizor SONY KD-77AG9"> """ + """

""" + f"""<img id="image-0" class="gallery-image" src="./bin/{full_product['product_folder_name_in']}/product_imgs/{full_product['imgs'][0]}" data-zoom-image="./bin/{full_product['product_folder_name_in']}/product_imgs/{full_product['imgs'][0]}">""" + """
<img id="image-1" class="gallery-image" src="./materials1 (25)_files/ag93_1_1.jpg" data-zoom-image="https://matrixmedia.pl/media/catalog/product/optimized/0/1/01f58fc041cf14e55804e0dee8c0f782/ag93_1_1.jpg">
<img id="image-2" class="gallery-image" src="./materials1 (25)_files/ag92_1_1.jpg" data-zoom-image="https://matrixmedia.pl/media/catalog/product/optimized/0/1/01f58fc041cf14e55804e0dee8c0f782/ag92_1_1.jpg">
<img id="image-3" class="gallery-image" src="./materials1 (25)_files/ag94_1_1.jpg" data-zoom-image="https://matrixmedia.pl/media/catalog/product/optimized/0/1/01f58fc041cf14e55804e0dee8c0f782/ag94_1_1.jpg">
</div>
</div>

<div class="more-views">
<ul class="product-image-thumbs slick-initialized slick-slider"><div aria-live="polite" class="slick-list draggable"><div class="slick-track" role="listbox" style="opacity: 1; width: 388px; left: 0px;">

""" + f"""
    <div class="slick-slide slick-current slick-active" data-slick-index="0" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide00" style="width: 97px;">
    <div><li style="width: 100%; display: inline-block;">
    <a class="thumb-link" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#" title="" data-image-index="0" tabindex="0">
    <img src="./bin/{full_product['product_folder_name_in']}/product_imgs/{full_product['imgs'][0]}"></a>
    </li></div></div>
    """ + ''.join([f"""<div class="slick-slide slick-active" data-slick-index="{i}" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide01" style="width: 97px;"><div><li style="width: 100%; display: inline-block;"><a class="thumb-link" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#" title="" data-image-index="1" tabindex="0"><img src="./bin/{full_product['product_folder_name_in']}/product_imgs/{full_product['imgs'][i]}"></a></li></div></div>
    """ for i in range(1, len(full_product['imgs']))]) + """

</div></div></ul>
</div>

<div class="sticker-container-bottom-left stickers">
</div>

<div class="sticker-container-bottom-right stickers">
</div>            </div>

<div class="product-right-box">			

<div class="product-shop">


<div class="price-info">

<div class="price-box">

<p class="old-price">
<span class="price-label">Normalna cena:</span>

</p>

<p class="special-price">
<span class="price-label">Special Price</span>
<span class="price" id="product-price-18787">
9&nbsp;999,00&nbsp;zł                </span>
</p>


</div>


</div>
<div class="info">                                                                                       
<div class="ialert">
ZAMÓWIENIE BEZ REJESTRACJI<br> W 2 MINUTY	
</div>
</div>
<br>                                                     			

<div class="add-to-cart-wrapper">

<div class="add-to-box">
                                        
<div class="add-to-cart">


<div class="add-to-cart-buttons">
<button type="button" title="Do koszyka" class="button btn-cart" onclick="productAddToCartForm.submit(this)"><span><span>Do koszyka</span></span></button>
</div>
</div>
            <span class="or">LUB</span>
                                                                </div>
                                        <div id="price_negotiation">
<div id="price_negotiation_button">Negocjuj cenę</div>

<div id="price_negotiation_form">
<p class="bolded title">Zadzwoń</p>
<a href="tel:61 642 77 42" class="phone_link">61 642 77 42</a>
<a href="tel:" class="phone_link"></a>

<p class="subtitle">lub <span class="bolded">wypełnij formularz</span></p>
<label for="price_negotiation_name">Imię i nazwisko:</label>
<input class="input_text" type="text" name="name" id="price_negotiation_name">
<label for="price_negotiation_mail_phone">Telefon lub e-mail</label>
<input class="input_text" type="text" name="mail_phone" id="price_negotiation_mail_phone">
<div class="agreement_container">
<input class="input_checkbox" type="checkbox" name="mail_phone" id="price_negotiation_agreement">
<label id="price_negotiation_agreement_label" for="price_negotiation_agreement">
Wyrażam zgodę na Negocjację Ceny
<div class="contactCheckbox4">
<div class="readmoreContainer">
<div class="readmorePopup4">

<p>
Zostałem poinformowany, że Administratorem moich dobrowolnie podanych danych osobowych jest Matrix Media Sp. z o.o. z siedzibą w Suchym Lesie, ul. Wierzbowa 5, 62 – 002 Suchy Las. Będą one przetwarzane w celu negocjacji ceny, co stanowi czynność poprzedzającą dokonanie Rezerwacji lub złożenie Zamówienia (art. 6 ust. 1 lit. b Rodo).
</p>
<p>
W sprawach związanych z przetwarzaniem Twoich danych osobowych możesz kontaktować się z Inspektorem Ochrony Danych dostępnym pod adresem e-mail: abi@matrixmedia.pl
</p>
<p>
Dane osobowe mogą być udostępniane upoważnionym przez nas podmiotom przetwarzającym lub innym administratorom działających we własnym imieniu, w tym osobom z nimi współpracującym, tj. firmom świadczącym usługi marketingowe, reklamowe, informatyczne, hostingowe oraz wspierające obsługę Sklepu.
</p>
<p>
Twoje dane będą przetwarzane do zakończenia czynności poprzedzających zawarcie umowy.
</p>
<p>
Obecnie nie będziemy przekazywać Twoich danych osobowych do państwa trzeciego lub organizacji międzynarodowej poza obszar Europejskiego Obszaru Gospodarczego, obejmującego Państwa Unii Europejskiej, Norwegię, Islandię oraz Lichtenstein.
</p>
<p>
Przysługuje Ci prawo dostępu do treści swoich danych, żądania ich przenoszenia bezpośrednio innemu administratorowi (o ile jest to technicznie możliwe), sprostowania, ograniczenia ich przetwarzania lub ich usunięcia, jeżeli są zbędne do realizacji celu, dla którego zostały zebrane, wniesiono prawnie uzasadniony sprzeciw oraz zostały zebrane z naruszeniem prawa. W celu z korzystania ze swoich uprawnień należy skierować swoje żądania na adres e-mail: dane.osobowe@matrixmedia.pl
Podanie przez Ciebie danych osob
</p>
<p>
Przysługuje Ci także prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych.
</p>
<p>
Zachęcamy również do zapoznania się z naszą Polityką Prywatności, w której szczegółowo opisujemy procesy przetwarzania danych w sklepie internetowym MatrixMedia.pl
</p>
</div>
<div class="readMore">Czytaj więcej.</div>
</div>

</div>


</label>
</div>
<div id="send_price_negotiation">Wyślij</div>
<div class="close"></div>
</div>

</div>

<script>

var priceNegotiationForm = jQuery('#price_negotiation_form');

jQuery(document).ready(function() {

jQuery('#send_price_negotiation').on('click', function() {
sendPriceNegotiationRequest();
});

jQuery('#price_negotiation_button').on('click', function() {
togglePriceNegotiationForm();
});

jQuery('#price_negotiation .close').on('click', function() {
closePriceNegotiationForm();
});

priceNegotiationForm = jQuery('#price_negotiation_form');

});

function sendPriceNegotiationRequest()
{
if (validatePriceNegotiationForm()) {

var name = jQuery("#price_negotiation_name").val();
var mail_phone = jQuery("#price_negotiation_mail_phone").val();
var agreement = 0;

if (jQuery("#price_negotiation_agreement").is(':checked')) {
agreement = 1;
}

var spinner = '<div class="spinner">' +
'  <div class="cube1"></div>' +
'  <div class="cube2"></div>' +
'</div>';

jQuery('#price_negotiation_button, #price_negotiation_form').css('display', 'none');
jQuery("#price_negotiation").append(spinner);


var request = jQuery.ajax({
url: 'https://matrixmedia.pl/price_negotiation/request/new/',
dataType: 'json',
data: "name="+name+"&mail_phone="+mail_phone+"&agreement="+agreement+"&product_id="+18787,
error: function() {
jQuery("#price_negotiation").html('<div class="response error">Something went wrong. Try again later</div>');
},
success: function(response) {
console.log(response);

if(response.status) {
jQuery("#price_negotiation").html('<div class="response success">'+response.message+'</div>');
} else {
jQuery("#price_negotiation").html('<div class="response error">'+response.message+'</div>');
}

},
type: 'POST'
});
}
}

function togglePriceNegotiationForm()
{
if (priceNegotiationForm.hasClass('active')) {
closePriceNegotiationForm();
} else {
openPriceNegotiationForm();
}
}

function openPriceNegotiationForm()
{
if(!priceNegotiationForm.is(":animated")) {
priceNegotiationForm.addClass('active');
priceNegotiationForm.animate({
opacity: 1
}, 600, function() {

});
}
}

function closePriceNegotiationForm()
{
if(!priceNegotiationForm.is(":animated")) {
priceNegotiationForm.animate({
opacity: 0
}, 600, function() {
priceNegotiationForm.removeClass('active');
});
}
}

function validatePriceNegotiationForm()
{
var validation = true;

jQuery('#price_negotiation_form .input_text').each(function(){
var value = jQuery(this).val();
if (value.trim() == '') {
validation = false;
jQuery(this).addClass('error');

}
});

if (!jQuery("#price_negotiation_agreement").is(':checked')) {
validation = false;
jQuery("#price_negotiation_agreement_label").addClass('error')
}

return validation;
}


jQuery('.readMore').click(function(){
jQuery('.readmorePopup4').toggle();
})
</script>                                                                    </div>
<div class="product-availabilty">
<div class="period-availabilty">

<div class="available">
Produkt dostępny    </div>


</div>
                                <div class="pickup-availability">
<button id="pickup-availability" class="btn-icon" data-pickup-url="https://matrixmedia.pl/pickupatstore/product/index/id/18787/">
<i class="icon-lokalizacja"></i>Sprawdź dostępność w punkcie    </button>
</div>                        <h6 style="padding-top: 10px"><b>KOSZT DOSTAWY</b> </h6>

<p style="padding-bottom: 8px; padding-top: 10px; font-size: 12px;">Odbiór osobisty:
<span style="float: right" class="price">0,00&nbsp;zł</span></p>


<table style="font-size: 12px;">
<tbody><tr style="width: 100%; ">
<td style="width: 100%; font-weight: normal; padding-left: 0; padding-bottom: 8px;">
<p style="text-decoration: none">GEIS (K-EX) - Przedpłata:</p>

</td>
<td style="vertical-align: center; text-align: right; padding-bottom: 8px; padding-left: 8px;">
<span class="price" style="float: right;">
0,00&nbsp;zł			</span>
</td>
</tr>

</tbody></table>


<table style="font-size: 12px;">
<tbody><tr style="width: 100%; ">
<td style="width: 100%; font-weight: normal; padding-left: 0; padding-bottom: 8px;">
<p style="text-decoration: none">GEIS (K-EX) - Wysyłka za pobraniem:</p>

</td>
<td style="vertical-align: center; text-align: right; padding-bottom: 8px; padding-left: 8px;">
<span class="price" style="float: right;">
115,00&nbsp;zł			</span>
</td>
</tr>

</tbody></table>

</div>
</div>

<div class="product-info-box">
<div id="configurable-box">
<script type="text/javascript">
jQuery('#change-product').on('change', function () {
var url = jQuery(this).val();
if (url) {
window.location = url;
}
return false;
});
</script>
</div>

<script type="text/javascript">

productId = jQuery("[name=product]").val();
jQuery(document).ready(function () {
jQuery.ajax({
url: "https://matrixmedia.pl/configurable/configurable/check/",
data: {
"productId": productId,
},
success: (function (data) {
console.log(data);

jQuery('#configurable-box').html(data);
})
})
});
</script>
<div class="product-payments">
<div class="installment-label">
Oblicz ratę                                
<a target="_blank" href="https://wniosek.eraty.pl/symulator/oblicz/numerSklepu/200731/typProduktu/0/wartoscTowarow/15999.0000"><img class="eraty_banner" src="./materials1 (25)_files/santander_raty.png" alt="Eraty"></a>

</div><style> #leasing-button-wrapper { margin-top: 0px; float:right; display:block; text-align: center;  width: 100%;} .leaselinkCalucalteButtonContainerPRO a { display: inline-block;width:100%;border-radius: 0px;  font-family: "Open Sans", sans-serif; font-weight: 700; text-transform: uppercase; text-decoration: none; background: #000; color: #fff !important; padding: 10px 25px 10px 8px; font-size: 13px; position: relative; transition: all 0.5s ease-in-out; } .leaselinkCalucalteButtonContainerPRO {text-align: center;width: 100%; position: relative; padding: 0px 20px 10px 0px; margin: 0px 0px 0px 0px; background: transparent; min-width: 130px; display: inline-block; } .leaselinkCalucalteButtonContainerPRO a span { font-size: 14px; font-weight: 600; margin:0px !important;} .leaselinkCalucalteButtonContainerPRO a:after { background: #eee url(https://leaselink.pl/img/arrow.png ) no-repeat center center; border-radius: 0 5px 5px 0; content: ""; display: block; height: 100%; position: absolute; right: -20px; top: 0;    width: 30px; transition: all 0.5s ease-in-out; } .leaselinkCalucalteButtonContainerPRO a span {color:#fff!important; font-size: 14px; } .infotextProLease{font-weight: bold;text-align: left;} .product-view .product-info-box .installment {padding: 50px 0;}</style> <div id="leasing-button-wrapper"><div class="infotextProLease">Oblicz ratę leasingu</div><div id="leaselinkCalucalteButton1PRO" class="leaselinkCalucalteButtonContainerPRO normal"><a rel="nofollow" style="cursor:pointer;" title="Oblicz ratę Leasingu" class="projketn"><span>WEŹ LEASING TERAZ</span></a></div></div>

<div class="extrahint installment">

</div>

</div>


<div class="product-info">

<div class="product-name">
<span class="h1">Telewizor SONY KD-77AG9</span>
</div>

<div>
<div style="clear: both;"></div>
</div>
<div class="product-code">
Kod producenta: """ \
           + full_product['manufacturer_code'] + """<br>
EAN : """ + full_product['sku'] + \
           """</div><div class="product-shortdescription">""" + full_product['descriptions'][1] + \
           """</div>

<a class="more-desc" style="padding-bottom: 20px;" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#description">Dowiedz się więcej</a>

</div>
                                                        </div>

<div class="clr"></div>

</div>

</div>

<div class="clr"></div>

<script type="text/javascript">
var bundles_optionsPrice = [];
var magentoEdition = "C";
var magentoVersionn = "1.9.4.3";
var magentoEditionSplited = magentoVersionn.split(".");
</script>
<div class="box-collateral box-md-bundles">
<div class="box-title">
<!-- <h2>Bundle Promotions</h2> -->
</div>
<div class="box-content">

<div class="toggle-holder">
<a id="acc-toggler" href="https://matrixmedia.pl/telewizor-sony-kd-77ag9.html#" hidden="">Inne zestawy</a>
</div>
</div>
</div>

<style>

</style>
<script>

jQuery("#acc-toggler").click(function( event ) {
event.preventDefault();
jQuery(this).toggleClass('opened');
jQuery(".bundle-discount-container").toggleClass('opened');
});




</script>
</form>

<script type="text/javascript">
//<![CDATA[
var productAddToCartForm = new VarienForm('product_addtocart_form');
productAddToCartForm.submit = function(button, url) {
if (this.validator.validate()) {
var form = this.form;
var oldUrl = form.action;

if (url) {
form.action = url;
}
var e = null;
try {
this.form.submit();
} catch (e) {
}
this.form.action = oldUrl;
if (e) {
throw e;
}

if (button && button != 'undefined') {
button.disabled = true;
}
}
}.bind(productAddToCartForm);

productAddToCartForm.submitLight = function(button, url){
if(this.validator) {
var nv = Validation.methods;
delete Validation.methods['required-entry'];
delete Validation.methods['validate-one-required'];
delete Validation.methods['validate-one-required-by-name'];
// Remove custom datetime validators
for (var methodName in Validation.methods) {
if (methodName.match(/^validate-datetime-.*/i)) {
delete Validation.methods[methodName];
}
}

if (this.validator.validate()) {
if (url) {
this.form.action = url;
}
this.form.submit();
}
Object.extend(Validation.methods, nv);
}
}.bind(productAddToCartForm);
//]]>
</script>
<div style="clear: both"></div>
</div>



<div>

<div class="product-menu" id="product-menu-description">

<a name="description"></a>

<a data-button="description" class="product-menu-button button-description active">
<span>Opis</span>
</a>
<a data-button="tech_description" class="product-menu-button button-tech_description ">
<span>Dane techniczne</span>
</a>

</div>

<div class="tab-container">    <div class="std">""" + full_product['descriptions'][0] + """</div>
</div>


<div class="product-menu" id="product-menu-tech_description">

<a name="tech_description"></a>

<a data-button="description" class="product-menu-button button-description ">
<span>Opis</span>
</a>
<a data-button="tech_description" class="product-menu-button button-tech_description active">
<span>Dane techniczne</span>
</a>                    
<div class="go_up"></div>
</div>

<div class="tab-container"><div class="std">
<div class="product">""" + full_product['descriptions'][2] + \
           """    </div>
</div>
</div>

<div class="tab-container">

<div class="clr"></div>

<script type="text/javascript">
$j(document).ready(function(){
$j('#five-products-bd775f5a2e3caaeafedcd7302bc831a0').slick({
autoplay: false,
slidesToShow: 5,
arrows: true,
dots: false,
responsive: [
{
breakpoint: 1024,
settings: {
slidesToShow: 3,
slidesToScroll: 3,
infinite: true,
}
},
{
breakpoint: 768,
settings: {
slidesToShow: 2,
slidesToScroll: 2
}
},
{
breakpoint: 620,
settings: {
slidesToShow: 1,
slidesToScroll: 1
}
}
]
})
});
</script>

</div>

</div>

<script type="text/javascript">
jQuery(function() {
jQuery(window).scroll(function() {
if(jQuery(this).scrollTop() > 1000) {
jQuery('#back_top').fadeIn();    
} else {
jQuery('#back_top').fadeOut();
}
});
jQuery('#back_top').click(function() {
productAddToCartForm.submit(this);
});    
});
</script>
</div>



<script type="text/javascript">
var lifetime = 3600;
var expireAt = Mage.Cookies.expires;
if (lifetime > 0) {
expireAt = new Date();
expireAt.setTime(expireAt.getTime() + lifetime * 1000);
}
Mage.Cookies.set('external_no_cache', 1, expireAt);
</script>


<!-- Go.pl -->
<script type="text/javascript">
var goadservicesq = goadservicesq || [];
try {
goadservicesq.push(
[
"_PRODUCT",
{ 
identifier : '18787', 
availability : '1' 
} 
]
);
(function() {
var goadservices = document.createElement('script');
goadservices.type = 'text/javascript';
goadservices.async = true;
goadservices.src = '//t.goadservices.com/engine/666b5297-21b9-499d-a058-0918bb9674d4';

var id_s = document.cookie.indexOf('__goadservices=');
if (id_s != -1) {
id_s += 15;
var id_e = document.cookie.indexOf(';', id_s);
if (id_e == -1) {
id_e = document.cookie.length;
}
goadservices.src += '?id='+document.cookie.substring(id_s, id_e);
}

var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(goadservices, s);
})();
} catch (e) {}
</script>

</div>

<section class="ceneo-opineo-section">
<div class="container">
<div class="ceneo-cnt"><img alt="ceneo" src="./materials1 (25)_files/ceneo.png">
<p><span>97% </span>klientów poleca ten sklep</p>
</div>   
</div>
</section>


<div class="container">
</div>

<div class="upper-footer">
</div>
<div class="footer" style="overflow-y: auto;">
<div class="container">
<div class="">
<div class="nl-container">
<div class="nl-info">
Lubisz otrzymywać info o ofertach specjalnych?<br><b>Zapisz się na nasz newsletter</b>
</div>
<div class="nl-input">
<form action="https://matrixmedia.pl/newsletter/subscriber/new/" method="post" id="newsletter-validate-detail">
<i class="icon icon-koperta"></i>
<input type="email" placeholder=" Podaj swój adres e-mail" autocapitalize="off" autocorrect="off" spellcheck="false" name="email" id="newsletter" title="Zapisz się do newslettera" class="input-text required-entry validate-email">
<button>
zapisz mnie
</button>
<div class="nl-checkbox-container">
<div class="acceptance_agreement_checkbox">
<input type="checkbox" id="acceptance_agreement" class="required-entry" name="acceptance_agreement">
<label class="label" for="acceptance_agreement">
<div class="newsletterCheckbox">
Wyrażam zgodę na otrzymywanie od Matrix Media Sp. z o.o. drogą elektroniczną na wskazany przeze mnie adres e-mail informacji handlowych.
<a href="https://matrixmedia.pl/informacje-o-celach-i-zakresie-przetwarzania-danych-osobowych" class="readMore">Więcej o przetwarzaniu danych osobowych.</a>
</div>
</label>
</div>
</div>
<div class="amasty_recaptcha"></div><input type="hidden" name="amasty_invisible_token" value=""><input type="hidden" name="amasty_invisible_token" value=""><input type="hidden" name="amasty_invisible_token" value=""><input type="hidden" name="amasty_invisible_token" value=""></form>
<script type="text/javascript">
//<![CDATA[
var newsletterSubscriberFormDetail = new VarienForm('newsletter-validate-detail');
//]]>
</script>
</div>
<div class="clr"></div>            </div>
<div class="shop-features">
<div class="feature">
<i class="icon icon-sposob-wysylki"></i>
<span class="">Odbierz Rezerwację <br>w Punkcie <strong>w 60 min</strong></span>
</div>
<div class="feature">
<i class="icon icon-dostawa24-black"></i>
<span class="">dostawa nawet<br><b>w 24 godziny</b></span>
</div>
<div class="feature">
<i class="icon icon-ekspresowe-raty"></i>
<span class=""><b>ekspresowe<br>raty</b></span>
</div>
<div class="feature">
<i class="icon icon-bezpieczenstwo-zakupow-black"></i>
<span><b>bezpieczeństwo<br>zakupu</b></span>
</div>
<div class="feature short">
<i class="icon icon-jakosc-i-cena"></i>
<span class=""><b>jakość i cena</b></span>
</div>
<div style="clear: both;"></div>
</div>
<div class="M_innerfooter">
<div class="M_innerfooter-left">
<div class="footer-contact">
<div class="telephone">
<i class="icon icon-telefon"></i>
<span>
<a href="tel:+48616427742">
61 642 77 42                                </a>
<a href="tel:+48">
    </a>
</span>
</div>
<div class="mail">
<i class="icon icon-koperta"></i>
<span>
<a href="mailto:sklep@matrixmedia.pl">
sklep@matrixmedia.pl                                </a>
</span>
</div>
<div class="M_address">
<i class="icon icon-lokalizacja"></i>
<span class="">Matrix Media Sp. z o.o.<br>62-002 Suchy Las<br>ul. Wierzbowa 5</span>
</div>
<div class="M_worktime">
<b>Godziny pracy:</b><br>pon-pt 9:00 - 18:00
</div>

<a class="more" href="https://matrixmedia.pl/contacts/">
więcej
</a>
</div>
<div class="M_shop-finder">
<div class="M_tittle">
Kup i odbierz w jednym<br>z punktów stacjonarnych
</div>
<div class="M_sf-map">
<a href="https://matrixmedia.pl/punkt-odbioru/"><img src="./materials1 (25)_files/znajdzsklep.png" alt="img"></a>
</div>
</div>
</div>
<div class="M_innerfooter-right">
<div class="">
<div class="footer-col">
<div class="links">
<div class="block-title"><strong><span>Firma</span></strong></div>
<ul>
<li><a href="https://matrixmedia.pl/o-firmie">O firmie</a></li>
<li><a href="https://matrixmedia.pl/contacts/">Kontakt</a></li>
<li><a href="https://matrixmedia.pl/sposob-zamawiania/">Sposób zamawiania i rezerwacji</a></li>
<li><a href="https://matrixmedia.pl/punkt-odbioru/">Punkt odbioru</a></li>
</ul>
</div>                        </div>
<div class="footer-col">
<div class="links">
<div class="block-title"><strong><span>Ważne informacje</span></strong></div>
<ul>
<li><a href="https://matrixmedia.pl/regulamin">Regulamin</a></li>
<li><a href="https://matrixmedia.pl/polityka-prywatnosci">Polityka prywatności</a></li>
<li><a href="https://matrixmedia.pl/najczesciej-zadawane-pytania">FAQ</a></li>
<li><a href="https://matrixmedia.pl/sposoby-dostawy">Sposoby dostawy</a></li>
<li><a href="https://matrixmedia.pl/jak-zaplacic">Jak zapłacić</a></li>
<li><a href="https://matrixmedia.pl/jak-zamowic">Jak zamówić</a></li>
<li><a href="https://matrixmedia.pl/rezerwacja">Rezerwacja</a></li>
<li><a href="https://matrixmedia.pl/raty">Jak kupić na raty</a></li>
<li><a href="https://matrixmedia.pl/reklamacje">Reklamacje</a></li>
<li><a href="https://matrixmedia.pl/gwarancja">Gwarancja</a></li>
<li><a href="https://matrixmedia.pl/zwroty">Zwroty</a></li>
</ul>
</div>                        </div>
<div class="footer-col">
<div class="links">
<div class="block-title"><strong><span>Konto</span></strong></div>
<ul>
<li class="first last"><a href="https://matrixmedia.pl/customer/account/" title="Moje konto">Moje konto</a></li>
</ul>
</div>
</div>
</div>
</div>
<div class="clr"></div>
</div>
</div>
</div>
<div class="M_underfooter">
<div class="container">
<div class="M_all">
<div class="M_underfooter-left">
<a target="_blank" href="https://twitter.com/matrixmedia_pl"><i class="icon icon-twitter"></i></a>
<a target="_blank" href="https://www.facebook.com/matrixmediapl/"><i class="icon icon-facebook"></i></a>
<a target="_blank" href="https://www.instagram.com/matrixmedia.pl/"><i class="icon fa fa-instagram"></i></a>
<a target="_blank" href="https://www.youtube.com/channel/UCpnCROtqct57tPh_TSNw3jg?view_as=subscriber"><i class="icon icon-youtube"></i></a>
</div>
<div class="M_underfooter-right">
© 2020 Matrix Media. All Rights Reserved.                </div>
</div>
</div>
</div>
</div>



<script type="text/javascript">
var formsToProtectOnPage = [];
var currentForm;
var currentValidationForm;
var checkedForms = [];
var hasFormsChanged = false;

var onSubmit = function (token) {
currentForm.querySelector('[name="amasty_invisible_token"]').setAttribute('value', token);
if (typeof(recaptchaObject) !== 'undefined'
&& 'post' !== currentForm.method
) {
recaptchaObject.submit();
} else {
currentForm.submit();
}
};

function checkForms() {
var formsToProtect = ["form[action*="customer\/account\/createpost"]","form[action*="customer\/account\/loginPost"]","form[action*="customer\/account\/forgotpasswordpost"]","form[action*="customer\/account\/resetpasswordpost"]","form[action*="newsletter\/subscriber\/new"]","form[action*="review\/product\/post"]","form[action*="contacts\/index\/post"]"];

if ("object" == typeof(formsToProtect)) {
formsToProtect = Object.values(formsToProtect);
}

formsToProtect.forEach(function (item) {
var continueWorking = true;

if ("function" == typeof(item)) {
return;
}

formsSearchedBySelector = $$(item);

checkedForms.forEach(function (element) {
if (element[0] == formsSearchedBySelector[0]) {
continueWorking = false;
return;
}
});

if (formsSearchedBySelector.length != 0 && continueWorking) {
checkedForms.push(formsSearchedBySelector);
formsSearchedBySelector.forEach(function (formToProtect) {
formsToProtectOnPage.push(formToProtect);
hasFormsChanged = true;
});
}
});

if (hasFormsChanged) {
for (var index in formsToProtectOnPage) {
if (formsToProtectOnPage.hasOwnProperty(index)) {
var formToProtectOnPage = formsToProtectOnPage[index];
if ('form' !== formToProtectOnPage.tagName.toLowerCase()) {
formToProtectOnPage = formToProtectOnPage.getElementsByTagName('form');
if (0 < formToProtectOnPage.length) {
formToProtectOnPage = formToProtectOnPage[0];
} else {
continue;
}
}

if (1 > formToProtectOnPage.getElementsByClassName('amasty_recaptcha').length) {
var recaptchaBlock = document.createElement('div');
recaptchaBlock.className = 'amasty_recaptcha';
formToProtectOnPage.appendChild(recaptchaBlock);
}

if (1 > formToProtectOnPage.getInputs(formToProtectOnPage, 'hidden', 'amasty_invisible_token').length) {
var tokenInput = document.createElement('input');
tokenInput.type = 'hidden';
tokenInput.name = 'amasty_invisible_token';
tokenInput.value = '';
formToProtectOnPage.appendChild(tokenInput);
}

formToProtectOnPage.onsubmit = function submitProtectedForm(event) {
currentForm = event.target;
currentValidationForm = new VarienForm(currentForm.id, false);
recaptchaBlock = currentForm.querySelector(".amasty_recaptcha");

if (recaptchaBlock.innerHTML == '') {
if (currentValidationForm && currentValidationForm.validator
&& currentValidationForm.validator.validate()
) {
recaptcha = grecaptcha.render(recaptchaBlock, {
'sitekey': '6LcM_tsUAAAAACzhpGRASySXVwVNWaUYai1qkeHO',
'callback': onSubmit,
'size': 'invisible',
'theme': 'light',
'badge': 'bottomleft'
});
}
}

if (!recaptcha) {
grecaptcha.reset(recaptcha);
grecaptcha.execute(recaptcha);
}

return false;
}
}
}
}
}

document.observe("dom:loaded", function () {
var formsCount = 0;
setInterval(function () {
var formLength = $$('form').length;
if (formsCount != formLength) {
formsCount = formLength;
checkForms();
}
}, 1000);
});
</script>
<script src="./materials1 (25)_files/api.js" async="" defer=""></script>
<script>
fbq('track', 'ViewContent', {
source: 'magento',
version: "1.9.4.3",
pluginVersion: "2.6.0",
content_type: "product",
content_ids: ["18787"]
, content_name: "Telewizor SONY KD-77AG9"
, value: 16859              , currency: "PLN"
});
</script>
</div>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","1730222507228304");fbq("track","PageView");</script>
<noscript>
<img height="1" width="1" src="https://www.facebook.com/tr?id=1730222507228304&amp;ev=PageView
&amp;noscript=1">
</noscript>
<aside class="" id="ceneo-widget" style="transition: right 0.5s ease 0.3s; width: 200px; position: fixed; right: -200px; top: 185px; z-index: 10000; display: block;"><img id="widget-handler" src="https://ssl.ceneo.pl/shops/Content/img/tab-title-v.png?v=2" style="background: rgb(247, 148, 30); position: absolute; padding: 2px 0px; left: -27px; top: 0px;"><iframe width="200" height="198" scrolling="no" id="ceneo-widget-content-sliding" style="border: 0px; transition: height 0.5s ease 0.3s;"></iframe></aside><aside class="" id="ceneo-widget" style="transition: right 0.5s ease 0.3s; width: 200px; position: fixed; right: -200px; top: 185px; z-index: 10000; display: block;"><img id="widget-handler" src="https://ssl.ceneo.pl/shops/Content/img/tab-title-v.png?v=2" style="background: rgb(247, 148, 30); position: absolute; padding: 2px 0px; left: -27px; top: 0px;"><iframe width="200" height="198" scrolling="no" id="ceneo-widget-content-sliding" style="border: 0px; transition: height 0.5s ease 0.3s;"></iframe></aside>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","1730222507228304");fbq("track","PageView");</script>
<noscript>
<img height="1" width="1" src="https://www.facebook.com/tr?id=1730222507228304&amp;ev=PageView
&amp;noscript=1">
</noscript>
<aside class="" id="ceneo-widget" style="transition: right 0.5s ease 0.3s; width: 200px; position: fixed; right: -200px; top: 185px; z-index: 10000; display: block;"><img id="widget-handler" src="https://ssl.ceneo.pl/shops/Content/img/tab-title-v.png?v=2" style="background: rgb(247, 148, 30); position: absolute; padding: 2px 0px; left: -27px; top: 0px;"><iframe width="200" height="198" scrolling="no" id="ceneo-widget-content-sliding" style="border: 0px; transition: height 0.5s ease 0.3s;"></iframe></aside>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","1730222507228304");fbq("track","PageView");</script>
<noscript>
<img height="1" width="1" src="https://www.facebook.com/tr?id=1730222507228304&amp;ev=PageView
&amp;noscript=1">
</noscript>
<aside class="" id="ceneo-widget" style="transition: right 0.5s ease 0.3s; width: 200px; position: fixed; right: -200px; top: 185px; z-index: 10000; display: block;"><img id="widget-handler" src="./materials1 (25)_files/tab-title-v.png" style="background: rgb(247, 148, 30); position: absolute; padding: 2px 0px; left: -27px; top: 0px;"><iframe width="200" height="198" scrolling="no" id="ceneo-widget-content-sliding" style="border: 0px; transition: height 0.5s ease 0.3s;" src="./materials1 (25)_files/saved_resource(1).html"></iframe></aside>

<script>
create_iframe("https://iframe.matrixmedia.pl/huawei/");
function create_iframe(url){

var wrapper = jQuery('#lp22');

if(navigator.userAgent.match(/(iPod|iPhone|iPad)/)){
wrapper.addClass('ios');
var scrolling = 'no';
}else{
var scrolling = 'yes';
}

jQuery('<iframe>', {
src: url,
id:  'url',
frameborder: 0,
scrolling: scrolling
}).appendTo(wrapper);

}

jQuery(document).ready(function() {
var heightName = 0;
setTimeout(function() {
jQuery('.slick-track').each(function() {
jQuery(this).find('.product-name').each(function(index) {
if(index==0) heightName=0;
if(jQuery(this).height() > heightName)  {
heightName  = jQuery(this).height();
}
});
if(heightName>0) jQuery(this).find('.product-name').css('height',heightName );
});
}, 5);
});
jQuery(window).on('scroll', function() {
var navHeight = 3; // custom nav height
var bannerHeight = jQuery('.magestore-bannerslider').height();
var windowHeight = jQuery(window).height();
var scroll = jQuery(window).scrollTop();
if(scroll > navHeight) {
if(windowHeight > bannerHeight) {
jQuery('.magestore-bannerslider.pos-side-left, .magestore-bannerslider.pos-side-right').addClass('sticky');
} else {
if(scroll > bannerHeight-windowHeight) {
jQuery('.magestore-bannerslider.pos-side-left, .magestore-bannerslider.pos-side-right').addClass('sticky-bottom');
} else {
jQuery('.magestore-bannerslider.pos-side-left, .magestore-bannerslider.pos-side-right').removeClass('sticky-bottom');
}
}
} else { 
jQuery('.magestore-bannerslider.pos-side-left, .magestore-bannerslider.pos-side-right').removeClass('sticky').removeClass('sticky-bottom');
}
});
var logoAlt = jQuery('#header .logo-container img').attr('alt');
if(logoAlt != '') jQuery('.pos-all-side-left, .pos-all-side-right').remove();
jQuery('.category-prezent-na-dzien-dziecka .js-after-add').insertBefore(jQuery('.subcategories'));
jQuery('.productbox-product .add-buttons .button, .hotshot .button, .product-view .product-shop .add-to-cart .button').on('click', function() {
dataLayer.push({ 'event': 'form.addToCart', 'actionName': 'Dodanie do koszyka' });
});
</script>
<script type="text/javascript" src="./materials1 (25)_files/666b5297-21b9-499d-a058-0918bb9674d4(1)" async="true"></script>
<script type="text/javascript">
var goadservicesq = goadservicesq || [];
try {
goadservicesq.push(
[
"_ENTRY"
]
);
(function() {
var goadservices = document.createElement('script');
goadservices.type = 'text/javascript';
goadservices.async = true;
goadservices.src = '//t.goadservices.com/engine/666b5297-21b9-499d-a058-0918bb9674d4';

var id_s = document.cookie.indexOf('__goadservices=');
if (id_s != -1) {
id_s += 15;
var id_e = document.cookie.indexOf(';', id_s);
if (id_e == -1) {
id_e = document.cookie.length;
}
goadservices.src += '?id='+document.cookie.substring(id_s, id_e);
}

var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(goadservices, s);
})();
} catch (e) {}
</script>

<script type="text/javascript">
document.addEventListener("DOMContentLoaded", function(event){
jQuery(document).ready(function(){
var shopID 			= "MATRIX";
var sumaProduktu	=	0;
var productName 	= "";
var imageLeaslink= "https://leaselink.pl/konfigurator_partnera/img/buttony/btn-small.png";

if(jQuery('.catalog-product-view .product-right-box .product-name span.h1').length===1){
productName =jQuery('.catalog-product-view .product-right-box  .product-name span.h1').text().trim().replace(/ /g,"%20");
if( jQuery('.product-right-box .price-box p.special-price > span.price').length==1){
sumaProduktu = jQuery('.product-right-box .price-box p.special-price > span.price').text(); 	
}else{
sumaProduktu = jQuery('.product-right-box .price-box span.regular-price > span.price').text(); 
}

sumaProduktu = sumaProduktu.replace(' ','').replace(',','.');
sumaProduktu = sumaProduktu.replace(/[^0-9\.]+/g,"").trim(); 

if( jQuery('#product_addtocart_form div.product-right-box > div.product-shop > div.product-availabilty > div.ask').length!==1)
if(sumaProduktu>=369){ 
jQuery(".installment-label").after( '<style> #leasing-button-wrapper { margin-top: 0px; float:right; display:block; text-align: center;  width: 100%;} .leaselinkCalucalteButtonContainerPRO a { display: inline-block;width:100%;border-radius: 0px;  font-family: "Open Sans", sans-serif; font-weight: 700; text-transform: uppercase; text-decoration: none; background: #000; color: #fff !important; padding: 10px 25px 10px 8px; font-size: 13px; position: relative; transition: all 0.5s ease-in-out; } .leaselinkCalucalteButtonContainerPRO {text-align: center;width: 100%; position: relative; padding: 0px 20px 10px 0px; margin: 0px 0px 0px 0px; background: transparent; min-width: 130px; display: inline-block; } .leaselinkCalucalteButtonContainerPRO a span { font-size: 14px; font-weight: 600; margin:0px !important;} .leaselinkCalucalteButtonContainerPRO a:after { background: #eee url(https://leaselink.pl/img/arrow.png ) no-repeat center center; border-radius: 0 5px 5px 0; content: ""; display: block; height: 100%; position: absolute; right: -20px; top: 0;    width: 30px; transition: all 0.5s ease-in-out; } .leaselinkCalucalteButtonContainerPRO a span {color:#fff!important; font-size: 14px; } .infotextProLease{font-weight: bold;text-align: left;} .product-view .product-info-box .installment {padding: 50px 0;}</style> <div id="leasing-button-wrapper"><div class="infotextProLease">Oblicz ratę leasingu</div><div id="leaselinkCalucalteButton1PRO" class="leaselinkCalucalteButtonContainerPRO normal"><a rel="nofollow" style="cursor:pointer;"  title="Oblicz ratę Leasingu" class="projketn"><span>WE&#377; LEASING TERAZ</span></a></div></div>');
}

jQuery('.projketn').click(function(event){
event.preventDefault();
window.open('https://leaselink.azurewebsites.net/RateCalculator/calculate?tax=23&isNet=false&externalId='+shopID+'&value='+sumaProduktu+'&productName='+productName ,'_blank', "width=750, height=850"); 
})}
})})
</script><script type="text/javascript" async="" src="./materials1 (25)_files/666b5297-21b9-499d-a058-0918bb9674d4(2)"></script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/tag/666b5297-21b9-499d-a058-0918bb9674d4?data=%5B%5B%22_ENTRY%22%5D%2C%5B%22_PRODUCT%22%2C%7B%22identifier%22%3A%2218787%22%2C%22availability%22%3A%221%22%7D%5D%5D&amp;url=file%3A%2F%2F%2FC%3A%2FUsers%2Fuser%2FDownloads%2Fprodukt%2Fprodukt%2Fmaterials1%2520(25).html&amp;id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619004046122-937085"></script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/check/666b5297-21b9-499d-a058-0918bb9674d4?id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619004046200-4169"></script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/tag/666b5297-21b9-499d-a058-0918bb9674d4?data=%5B%5B%22_ENTRY%22%5D%2C%5B%22_PRODUCT%22%2C%7B%22identifier%22%3A%2218787%22%2C%22availability%22%3A%221%22%7D%5D%5D&amp;url=file%3A%2F%2F%2FC%3A%2FUsers%2Fuser%2FDownloads%2Fprodukt%2Fprodukt%2Fmaterials1%2520(25).html&amp;id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619004718984-943571"></script>



<div id="callpageWrapper"><div id="callpage" dir="ltr" data-specifity="" class="cp-callpage cp-callpage--widget-callback cp-theme-light"><div data-ignore-important-opacity="" class="cp-callpage__bg" style="display: none;"></div> <div class="cp-callpage__widget-wrapper js-cp-callpage__widget-wrapper cp-noscroll"><div data-ignore-important-display="" data-active-state="loader" data-active-root-state="loader" class="cp-callback-widget cp-callpage__widget cp-js-widget" data-test="widget" style="display: none;"><!----> <button type="button" class="cp-close-btn cp-callback-widget__close-btn cp-close-btn--mobile-friendly" tabindex="-1" data-test="widget-close-btn"><svg viewBox="2115.656 4371.656 11.054 11.054" class="cp-close-btn__img"><g class="cp-close-btn__shape"><path data-brand-color="stroke-color" d="M2126.003 4372.363l-9.64 9.64" class="cp-close-btn__path"></path> <path data-brand-color="stroke-color" d="M2116.363 4372.363l9.64 9.64" class="cp-close-btn__path"></path></g></svg></button> <div class="cp-fade-height cp-fade-height--flexbox"><div tabindex="0" class="loader__lol cp-callback-widget__state"><div class="loader"><svg viewBox="25 25 50 50" class="loader__circular"><circle cx="50" cy="50" r="10" fill="none" stroke-width="2" stroke-miterlimit="10" class="loader__path"></circle></svg></div></div></div> <!----> <!----> <a target="_blank" href="https://www.callpage.pl/?utm_source=matrixmedia.pl&amp;utm_medium=widget" class="cp-copyright cp-callback-widget__copyright"><span><!----> <span class="cp-copyright__text">Powered by</span> <span><img height="10" src="data:image/png;base64,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" alt=" " class="cp-copyright__logo cp-copyright__logo--light"> <img height="10" src="data:image/png;base64,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" alt=" " class="cp-copyright__logo cp-copyright__logo--dark"></span></span></a></div></div> <div data-test="widget-button-section" class="cp-button-section cp-callpage__button" style="left: calc(4% + 40px) !important; bottom: calc(0% + 40px) !important;"><div class="cp-tooltip cp-button-tooltip cp-button-section__tooltip" data-test="button-tooltip" data-ignore-important-opacity="" x-placement="top" style="position: absolute !important; top: auto !important; left: 141px !important; will-change: transform !important; bottom: 100% !important; display: none !important;"><button type="button" class="cp-close-btn cp-tooltip__close-btn cp-close-btn--round cp-close-btn--offset cp-close-btn--mobile-friendly" data-test="tooltip-close-btn"><svg viewBox="2115.656 4371.656 11.054 11.054" class="cp-close-btn__img"><g class="cp-close-btn__shape"><path data-brand-color="stroke-color" d="M2126.003 4372.363l-9.64 9.64" class="cp-close-btn__path"></path> <path data-brand-color="stroke-color" d="M2116.363 4372.363l9.64 9.64" class="cp-close-btn__path"></path></g></svg></button> <div x-arrow="" class="cp-tooltip__tail" style="left: 0px !important;"></div> <div class="cp-tooltip__inner cp-button-tooltip__inner"><div data-test="one-click-call" class="cp-instant-call"><p class="cp-instant-call__greeting-text">Cześć!</p> <p class="cp-instant-call__callback-text">Czy chcesz, żebyśmy oddzwonili do Ciebie za darmo w 30 minut ?</p> <!----> <div><button data-brand-color="background" class="cp-btn cp-btn--brand cp-instant-call__call-btn cp-btn--small" data-test="make-call-btn">TAK</button></div></div></div></div> <!----> <div data-test="widget-button" class="cp-widget-button"><!----> <div data-brand-color="background" class="cp-widget-button__inner"><svg x="0px" y="0px" viewBox="0 0 100 108.4" class="cp-phone-icon cp-widget-button__icon"><path d="M97.8,84.4l-0.6-1.2c-1.7-4-22.3-10-24.1-10.1l-1.4,0.1c-2.8,0.6-5.9,3.3-12.4,9C52,78.8,41.9,69.7,37.2,64.4 c-5.1-5.8-11.5-15.5-13.8-22.8C30.8,35,33.9,32.2,34.1,29c0.1-1.7-3.4-22.9-7.2-25.1l-1.1-0.7c-2.4-1.5-6-3.8-10-3 c-1,0.2-1.9,0.6-2.8,1.1C10.4,3,3.8,7.5,0.8,13.5C-1,17.2-1.9,51,23.5,79.6c25,28.3,55.9,29.5,60.5,28.5l0.1,0l0.4-0.1 c6.3-2.2,11.6-8.2,13.6-10.7C101.8,92.7,99.2,87.3,97.8,84.4"></path></svg></div> <span class="cp-widget-button__close-btn-hover"></span> <!----></div></div></div></div><img id="goadservices-rtb-ibillboard-0" src="./materials1 (25)_files/GoPl" width="0" height="0" style="display: none !important; width: 0px !important; height: 0px !important;"><img id="goadservices-rtb-netsprint-0" src="./materials1 (25)_files/saved_resource" width="0" height="0" style="display: none !important; width: 0px !important; height: 0px !important;"><app-content ng-version="11.1.0"></app-content>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","1730222507228304");fbq("track","PageView");</script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/check/666b5297-21b9-499d-a058-0918bb9674d4?id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619004719077-63993"></script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/tag/666b5297-21b9-499d-a058-0918bb9674d4?data=%5B%5B%22_ENTRY%22%5D%2C%5B%22_ENTRY%22%5D%2C%5B%22_PRODUCT%22%2C%7B%22identifier%22%3A%2218787%22%2C%22availability%22%3A%221%22%7D%5D%5D&amp;url=file%3A%2F%2F%2FC%3A%2FUsers%2Fuser%2FPycharmProjects%2FXMLbot%2Fpreview.html&amp;id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619006194014-825336"></script>
<noscript>
<img height="1" width="1" src="https://www.facebook.com/tr?id=1730222507228304&amp;ev=PageView
&amp;noscript=1">
</noscript>


<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","1730222507228304");fbq("track","PageView");</script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/check/666b5297-21b9-499d-a058-0918bb9674d4?id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619006194179-990447"></script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/tag/666b5297-21b9-499d-a058-0918bb9674d4?data=%5B%5B%22_ENTRY%22%5D%2C%5B%22_ENTRY%22%5D%2C%5B%22_PRODUCT%22%2C%7B%22identifier%22%3A%2218787%22%2C%22availability%22%3A%221%22%7D%5D%5D&amp;url=file%3A%2F%2F%2FC%3A%2FUsers%2Fuser%2FPycharmProjects%2FXMLbot%2Fmaterials1%2520(25).html&amp;id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619006891311-41964"></script><script type="text/javascript" async="" src="http://t.goadservices.com/v2/check/666b5297-21b9-499d-a058-0918bb9674d4?id=3-mSroyeuzI_XI9UN5mtWMD1l499uWyNu7v1QmsTHUGlA&amp;rid=1619006891406-785683"></script>
<noscript>
<img height="1" width="1" src="https://www.facebook.com/tr?id=1730222507228304&amp;ev=PageView
&amp;noscript=1">
</noscript>
<div class="zoomContainer" style="-webkit-transform: translateZ(0);position:absolute;left:30.5px;top:410.59375px;height:518px;width:518px;"><div class="zoomLens" style="background-position: 0px 0px; float: right; overflow: hidden; z-index: 999; transform: translateZ(0px); opacity: 0.4; zoom: 1; width: 345.333px; height: 345.333px; background-color: white; cursor: default; border: 1px solid rgb(0, 0, 0); background-repeat: no-repeat; position: absolute; left: 173px; top: 173px; display: none;">&nbsp;</div><div class="zoomWindowContainer" style="width: 400px;"><div style="overflow: hidden; background-position: -208px -208px; text-align: center; background-color: rgb(255, 255, 255); width: 400px; height: 400px; float: left; background-size: 600px 600px; z-index: 100; border: 4px solid rgb(136, 136, 136); background-repeat: no-repeat; position: absolute; background-image: url(&quot;./materials1 (25)_files/ag91_1_1.jpg&quot;); top: 0px; left: 518px; display: none;" class="zoomWindow">&nbsp;</div></div></div></body></html>"""

    return html


@timeit
def PreviewHTML(full_product, yes_to_all):
    try:
        full_product['imgs'][0]
    except IndexError:
        full_product['imgs'] = ['']

    while 'src="//' in full_product['descriptions'][0]:
        full_product['descriptions'][0] = full_product['descriptions'][0].replace('src="//', 'src="https://')

    with open('preview.html', 'w', encoding="utf-8") as preview:
        # add MatrixMedia CSS files
        preview.write(add_mm_css(full_product))

    os.startfile('preview.html')  # open "preview.html" file
    sleep(1)  # let the file being opened before it is removed

    if yes_to_all is False:
        print(f'Accept with "Enter" button, decline with "Esc" or mark with "M" ({full_product["sku"]})')

        # wait for a user to confirm it
        while True:
            if keyboard.is_pressed('Enter'):
                print(f'INFO: Accepted: {full_product["sku"]}')
                return 0
            elif keyboard.is_pressed('Esc'):
                print(f'INFO: Declined: {full_product["sku"]}')
                return -1
            elif keyboard.is_pressed('M'):
                print(f'INFO: Marked: {full_product["sku"]}')
                return 1
    else:
        print(f'INFO: Accepted automatially: {full_product["sku"]}')

    sleep(1)  # let "print" fuction print a message
    os.remove('preview.html')  # remove "preview.html" file
