# Whitelist Checker Tool
# StolicaRP.pl ~Konieczkooo

# Pobieranie danych od użytkownika
data = []
print("Wpisz nick gracza, później dane do zapisania w pliku - (wpisz 'q', aby zakończyć):")
print("Plik zostanie zapisany pod nazwą pierwszej wpisanej zmiennej, czyli nicku gracza.")
while True:
    line = input()
    if line == "q":
        break
    data.append(line)
    print("Twoja wiadomość została dodana do pliku.")

# Pobranie nazwy pliku z pierwszej wpisanej zmiennej
filename = data[0] + ".txt"

# Otwarcie pliku tekstowego do zapisu
with open(filename, "w") as file:
    # Zapisanie danych w pliku tekstowym
    for line in data:
        file.write(line + "\n")

# Zakończenie programu
print(f"Zapisano dane w pliku {filename}")
