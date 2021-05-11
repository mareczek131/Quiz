import random
a = 0
dobre_odpowiedzi = 0

nazw_kat = ["Gry wideo", "Muzyka","filmy i seriale", "matematyka"]


pytania_gry = [
    "W którym roku odbyła się premiera Wiedzmina 3? A.2015 B.2014 C.2077 D.2016",
    "Kiedy zaplanowana jest premiera PlayStation 5? A.19.11.2020 B.20.11.2020 C.18.11.2020 D.15.11.2020",
    "Studio które wydało League of Legends: A.Tencent B.Blizzard C.Riot Games D. Ubisoft",
    "Data wydania Diablo III: A.2011 B.2013 C.2012 D.2014"

]

odp_gry = [
    "A",
    "A",
    "C",
    "C"
]

pytania_muzyka = [
"W którym roku powstał zespół rockowy Queen? A.1971 B.1969 C.1970 D.1980",
"W którym roku urodził się Elton John? A.1945 B.1947 C.1948 D.1938",
"Amerykański zespół heavymetalowy założony w Los Angeles w Kalifornii w 1981r.: A.Metallica B.Iron Maiden C.Nirvana D.The Rolling Stones",
"Brytyjski pop-rockowy zespół muzyczny z Liverpoolu: A.Queen, B.The Beatles C.AC/DC D.Nirvana"
]

odp_muz = [
    "C",
    "B",
    "A",
    "B"
]

pytania_filmy_i_seriale = [
"Ile sezonów ma serial Mr Robot? A.1 B.3 C.4 D.2",
"Jaki jest tytuł V części Star Wars? A.Imperium kontratakuje B.Nowa nadzieja C.Powrót Jedi D.Atak klonów",
"Imię aktora grającego głównego bohatera w filmie Catch Me if You Can: A.Arthur Fleck B.Leonardo DiCaprio C.Al Pacino D. Alan Rickman",
"Ile części ma Harry Potter? A.5 B.4 C.7 D.8"
]

odp_film_ser = [
    "C",
    "A",
    "B",
    "C"
]

pytania_matematyka = [
"Ile to 2 + 2? A.5 B.3 C.1 D.4",
"Wzór na pole trójkąta: A.a*a B.(1/2)ah C.(d1*d2)/2 D.a*b",
"Polski matematyk i kryptolog, który w 1932 roku złamał szyfr Enigmy: A.Kazimierz Abramowicz B.Kazimierz Alster C.Henryl Zygalski D.Bruno Abakanowicz",
"Wartość sin 30°: A.1/2 B.1/4 C.1 D.2"
]

pyt_mat = [
    "D",
    "B",
    "C",
    "A"
]

odpowiedzi = [odp_gry, odp_muz, odp_film_ser, pyt_mat]

kategorie = [pytania_gry, pytania_muzyka, pytania_filmy_i_seriale, pytania_matematyka]

while True:
    los_kat = random.randrange(0,4)
    los_pyt = random.randrange(0,4)
    a = los_pyt
    print("Kategoria:",nazw_kat[los_kat],":", kategorie[los_kat][los_pyt])
    odp = input("Podaj odpowiedź: ")

    if odp.upper() == odpowiedzi[los_kat][los_pyt]:
        print("Dobrze")
        dobre_odpowiedzi += 1

    else:
        print("Zła odpowiedź")
        print("Poprawna odpowiedź to: ", odpowiedzi[los_kat][los_pyt], "Ilość poprawnych odpowiedzi: ", dobre_odpowiedzi)
        break
