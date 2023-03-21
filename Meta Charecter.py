import re
pattern = r"^colo..r$"

if re.match(pattern,"coloubr"):
    print(" Yes It Is  Matched")

# strict meta charecter
import re
pattern = r"(ab)*"

if re.match(pattern,"coloubr"):
    print(" Yes It Is  Matched")

# + meta charecter > eta mane hoccce jeta plus dibo ota thaktey hobe ebong sheta bade onno kicu  thaktte pare ebong oy shonkha ta ekadhikbar oo thakte pare
import re
pattern = r"a+"

if re.match(pattern,"abcoloubr"):
    print(" Yes It Is  Matched")
# ? meta charecter > eti bebohar er fole jeta chacci seta user er kace thakleou kaj korbe ebong
#na thakleou kaj korbe kintu ekadhikbar chawa jabe na ...............................................
import re
pattern = r"ice(-)?cream"

if re.match(pattern,"icecreamm"):
    print(" Yes It Is  Matched")

# {and} meta charecter er bebohar
import re
pattern = r"a{1,3}$"

if re.match(pattern,"aa"):
    print(" Yes It Is  Matched")


