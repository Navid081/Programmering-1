# 9.2

registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmalningar = ["Anna", "Erik", "Karl"]

print("Före modifiering: ", registrerade)
print("****************************")

for namn in avanmalningar:          # namn kommer att innhålla alla namn(element) i avanmalningar tillfälligt.
    if namn in registrerade:        # Om värdet på namn finns i listan "registrerade"
        registrerade.remove(namn)   # kommer värdet på namn att tas bort ur listan "registrerade"

print("Efter modifiering: ", registrerade)


