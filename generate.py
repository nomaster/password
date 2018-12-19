#!/usr/bin/env python3

from password_generator import PasswordGenerator

pwo = PasswordGenerator()
pwo.minlen = 32
pwo.maxlen = 32
pwo.excludeschars = "!$%^.#()[]&<>,"
print(pwo.generate())
