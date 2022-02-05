# import biblioteki pygame i random
import pygame, random

# inicjalizacja pygame i fontow
pygame.init()
pygame.font.init()

# losowanie slowa z listy
def losowanie_slowa():
    slowa = ["cos", "cos2", "cos3", "ali", "ma", "kota", "python", "oooo", "ake"]
    n = random.choice(slowa)
    return n

# wyswietlanie odpowiedniego png wzgledem zycia. Zwraca ilosc zycia i odpowiedni png.
def pozycja_wisielca(ZYCIA):
    if (ZYCIA == 3):
        screen.blit(wisielec_img_1, (wisielecX, wisielecY+50))
    elif (ZYCIA==2):
        screen.blit(wisielec_img_2, (wisielecX, wisielecY))
    elif (ZYCIA == 1):
        screen.blit(wisielec_img_3, (wisielecX, wisielecY))
    elif (ZYCIA == 0):
        screen.blit(wisielec_img_4, (wisielecX, wisielecY))
    return ZYCIA

# sprawdza czy podana litera znajduje sie w hasle, jezeli tak znak "_", zamienia na dana litere
# (trzeba poprawic, bo nie zmienia wszystkich znakow)
# zwraca None jezeli nie znajdzie litery, a jezeli znajdzie zwraca ciag ze zmienionym znakiem
def sprawdzanie_litery(litera, haslo):

    if litera in haslo:
        index_litery = haslo.find(litera)
        znaki_haszowane[index_litery] = litera
        znaki_jako_string = " ".join(znaki_haszowane)
        return znaki_jako_string
    else:
        return None

# nadawanie width i height screenowi, title gry, ikona gry
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Wisielec")
ikona = pygame.image.load('rope.png')
pygame.display.set_icon(ikona)

# zmienna do petli, która jest na True. zmienna z haslem, zmienna z tablicą do "___", zycia,
# zmienna przechowujaca wykorzystane litery, zmienna przechowujaca litere gracza, petla do tworzenia zahaszowanego hasla
DZIALANIE_PROGRAMU = True
haslo = losowanie_slowa()
znaki_haszowane = []
zycia = 4
znaki_wykorzystane = []
litera_wpisana_przez_gracza = ''
znaki_jako_string = ''
for i in range(len(haslo)):
    znaki_haszowane.append("_")

# nadawanie zmiennej fonta i rozmaru + przypisanie zmiennej napisu z tym fontem
myfont = pygame.font.SysFont('arial', 20, bold=True)
myfont_for_end = pygame.font.SysFont("arial", 40, bold=True)
napis_wyswietlany_graczowi = myfont.render('PODAJ LITERE:', False, (0, 0, 0))
koniec_gry_napis_LOSE = myfont_for_end.render("Przegrałeś! Hasło to:      ", False, (255, 255, 255))
koniec_gry_napis_WIN = myfont_for_end.render("Wygrałeś! Gratuluję!", False, (255, 255, 255))
haslo_do_wyswietlenia = myfont_for_end.render(haslo, False, (255, 255, 255))

# pobieranie etapow wisielca jako png + zmienne okreslajace jego pozycje
wisielec_img_1 = pygame.image.load('hangman1.png')
wisielec_img_2 = pygame.image.load('hangman2.png')
wisielec_img_3 = pygame.image.load('hangman3.png')
wisielec_img_4 = pygame.image.load('hangman4.png')
wisielecX = 650
wisielecY = 150



# gra dziala dopoki dzialanie_programu nie zmieni się, czyli kiedy nastąpi event.QUIT (gracz kliknie x)
while DZIALANIE_PROGRAMU:
    #background RGB
    screen.fill((100, 140, 100))

    # sprawdzanie event 1. czy gracz nie kliknal 'x' i wpisywanie liter przez gracza event.unicode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DZIALANIE_PROGRAMU = False
        if event.type == pygame.KEYDOWN:
            litera_wpisana_przez_gracza = event.unicode

        # wyswitlanie litery gracza, miejsca na tekst, napis wyswietlany graczowy (wyzej zmienna), sprawdzanie poprawnosci litery
        # zwraca albo ciag znakow, albo None
        miejsce_na_tekst = myfont.render(litera_wpisana_przez_gracza, True, (0, 0, 0))
        screen.blit(miejsce_na_tekst, (300, 250))
        screen.blit(napis_wyswietlany_graczowi, (130, 250))
        sprawdzanie_dobrej_litery = sprawdzanie_litery(litera_wpisana_przez_gracza, haslo)

        # sprawdzanie czy litera ma None, czyli nie ma jej w hasle 1. Jeżeli nie ma - wyswietlany jest odpowiedni wisielec
        # wzgledem pozostalych żyć, a nastepnie sprawdzane jest czy litera znajduje sie w znakach wykorzystanych, jezeli nie
        # do znakow wykorzystanych jest dopisywana i gracz traci jedno zycie.
        if sprawdzanie_dobrej_litery == None:
                pozycja_wisielca(zycia)
                if not litera_wpisana_przez_gracza in znaki_wykorzystane:
                    znaki_wykorzystane.append(litera_wpisana_przez_gracza)
                    zycia -= 1

        # wyswitlanie wisielca, wyswitalnie odhaszowanych liter (np. "___p___"), jezeli "_" nie ma w stringu to gracz wygrywa
        else:
            ilosc_liter_w_stringu = myfont.render(sprawdzanie_dobrej_litery, True, (0, 0, 0))
            pozycja_wisielca(zycia)
            if not "_" in sprawdzanie_dobrej_litery:
                screen.fill((100, 100, 100))
                screen.blit(koniec_gry_napis_WIN, (250, 260))
        screen.blit(ilosc_liter_w_stringu, (450, 250))

        # koniec gry gdy zycia spadna do 0, bg zmienia sie na szary i wyskakuje napis i haslo
        if zycia == 0:
            screen.fill((100, 100, 100))
            screen.blit(koniec_gry_napis_LOSE, (220, 180))
            screen.blit(haslo_do_wyswietlenia, (630, 180))
            screen.blit(wisielec_img_4, (wisielecX-250,wisielecY+100))
        # update danych wpisanych przez gracza i eventow
        pygame.display.update()
