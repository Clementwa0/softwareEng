# form a search pattern

import re

txt = "The rain in Kenya"
x = re.search("^The.*Kenya$",txt)

print(x)

# find all
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# 