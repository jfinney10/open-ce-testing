import re
import sys

for line in sys.stdin:
    match = re.match (r'^([\w-]+)(?:\s+\S+)*\s+(\d+)([.,](\d+|\d{1}))?([.,](\d+|\d{1}))?[\s\S]*?$', line)
    if match:
        package_name = match.group(1)
        version_components = [match.group(i) for i in [2,4,6] if match.group(i)]
        version_number = '.'.join(version_components)
        #print (f'  - {package_name}={version_number}')
        print (f'conda install {package_name}={version_number}')
    else:
        print (f'---> Failed to match: {line.split ()[0]}')
