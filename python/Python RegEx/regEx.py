# form a search pattern

import re

txt = "The rain in Kenya"
x = re.search("^The.*Kenya$",txt)

print(x)