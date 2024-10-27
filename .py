def calculator_acumulare_dobanda(suma_lunara, perioada, randament):
    randament_lunar = randament / 100 / 12
    suma_totala = suma_lunara * (((1 + randament_lunar) ** perioada) - 1) / randament_lunar
    return suma_totala
#inputuri
suma_lunara = float(input("Care este suna lunara depusa?:\n"))
perioada = int(input("Perioada pentru care acumulezi?:\n"))
randament = float(input("Care este randamentul pe care il estimezi?:\n"))

#conversia

suma_totala = calculator_acumulare_dobanda(suma_lunara, perioada, randament)
print(f"Suna acumulata dupa {perioada} luni, cu un randament de {randament} si o depunere lunara de {suma_lunara}, este {suma_totala:.2f}! ")
