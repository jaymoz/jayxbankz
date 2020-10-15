#!"c:\users\jaymos\desktop\the wisdom of gathering fragments\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'mce==0.1.3','console_scripts','mce'
__requires__ = 'mce==0.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mce==0.1.3', 'console_scripts', 'mce')()
    )
