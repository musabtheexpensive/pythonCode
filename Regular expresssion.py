# Match() function
import re
pattern = r"colour"
if re.match(pattern,"Red is a colour, I love red colour"):
    print("Match")

else:
    print("Not Matched")

############## 1
import re
pattern = r"Colour"
if re.match(pattern,"Colour is a colour, I love red colour"):
    print("Match")

else:
    print("Not Matched")

############## Search function() 2

import re
pattern = r"colour"
if re.search(pattern,"Red is a colour, I love red colour"):
    print("Match")

else:
    print("Not Matched")

############## findall function () 3
import re
pattern = r"colour"
print(re.findall(pattern,"Red is a colour, I love red colour"))


############# 4
import re
pattern = r"col"
print(re.findall(pattern,"Red is a colour, I love red colour"))


############# 4
import re
pattern = r"col"
if re.match(pattern,"colour is a colour, I love red colour"):
    print("Match")

else:
    print("Not Matched")

