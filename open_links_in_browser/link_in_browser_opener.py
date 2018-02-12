import webbrowser
import re

# 'http://docs.python.org/'

links_separated_by_new_lines = """

"""

links_separated_by_new_lines = re.sub(r'\n+', '\n', links_separated_by_new_lines).strip()

urls = links_separated_by_new_lines.split('\n')

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
for u in urls:
    webbrowser.get(chrome_path).open(u)
