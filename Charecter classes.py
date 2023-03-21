import re
pattern = r"[aeiou]"

if re.match(pattern,"anuuindbnudu"):
    print(" Yes It Is  Matched")

#same programme just different
import re
pattern = r"[A-Z]"

if re.match(pattern,"Aggghhhh"):
    print(" Yes It Is  Matched")

#same programme just different
import re

pattern = r"[A-Z] [a-z] [0-9]"

if re.match(pattern, "Ag0ghhh"):
    print(" Yes It Is  Matched")
