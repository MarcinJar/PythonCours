import os

os.system('clear')

favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'rust',
    'paweł': 'python',
}

language = favorite_languages['sara'].title()
print(f"Ulubiony język programowania Sary to {language}.")

for name, language in favorite_languages.items():
    print(f"Ulubiony język programowania użytkowanika {name.title()} to {language.title()}")

print("\nNasi uczestnicy:")
for name in favorite_languages.keys():
    print(name.title())

if 'elżbieta' not in favorite_languages.keys():
    print("\nElżbieta, proszę, weź udział w naszej ankiecie")

print("\nPodziękowania")
for name in sorted(favorite_languages):
    print(f"{name.title()}, dziękujemy za udział w ankiecie")

print("\nW ankiecie wymieniono następujuące języki programowania:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())