import webbrowser
import re

# 'http://docs.python.org/'

links_separated_by_new_lines = """
https://www.facebook.com/groups/114254395916158/
https://www.facebook.com/polishroot/
https://www.facebook.com/proudandpolish/?ref=br_rs
https://www.facebook.com/ilovemypolishheritage/
https://www.facebook.com/groups/english.speakers.gdansk.sopot.gdynia/
https://www.facebook.com/groups/english.speakers.gdansk.sopot.gdynia/
https://www.facebook.com/groups/152543081549780/?notif_id=1510766115418343&notif_t=group_r2j_approved&ref=notif
https://www.facebook.com/groups/1376471742618476
https://www.facebook.com/groups/586525431512983
https://www.facebook.com/Po-polsku-po-Polsce-1781417775419040
https://www.facebook.com/lektorzyjezykapolskiego
https://www.facebook.com/WroclawLanguageCafe/
https://www.facebook.com/Polish-no-problem-477337982368996
https://www.facebook.com/Poland.no.problem
https://www.facebook.com/ForeignersInPoland/
https://www.facebook.com/groups/lec.krakow/about/
https://www.facebook.com/groups/sillylinguistics/about/
https://www.facebook.com/groups/lecwroclaw/about/
"""

links_separated_by_new_lines = re.sub(r'\n+', '\n', links_separated_by_new_lines).strip()

urls = links_separated_by_new_lines.split('\n')

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
for u in urls:
    webbrowser.get(chrome_path).open(u)
