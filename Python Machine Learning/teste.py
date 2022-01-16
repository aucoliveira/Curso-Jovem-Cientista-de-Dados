import re

tele = '0800-001-0031\n3497-1814\n98594-0305\n(39)97666-9377\n61900-010'

print(re.findall(r'\d{5}\W\d{4}', tele))