import webbrowser
import re

# 'http://docs.python.org/'

links_separated_by_new_lines = """

"""

links_separated_by_new_lines = re.sub(r'\n+', '\n', links_separated_by_new_lines).strip()

urls = links_separated_by_new_lines.split('\n')

# browser_path = 'open -a /Applications/Google\ Chrome.app %s'
browser_path = 'open -a /Applications/Firefox.app %s'
for u in urls:
    print(u)
    webbrowser.get(browser_path).open_new_tab(u)