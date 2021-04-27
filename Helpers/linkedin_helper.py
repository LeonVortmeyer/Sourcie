from googlesearch import search
import re
# to search
def scrape_linkedins(query, limit=10):

    linkedin_results = []
    pattern = re.compile(r"(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/in\/(?P<permalink>[\w\-\_À-ÿ%]+)\/?")
    for j in search(query, tld="co.in", num=20, stop=20, pause=2):
        if pattern.search(j):
            linkedin_results.append(j)

    return linkedin_results

print(scrape_linkedins("Jetpack workflow ceo"))


