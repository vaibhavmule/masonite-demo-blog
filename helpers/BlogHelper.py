import re
import unidecode

def slugify(text):
    # helper function that creates slugs for the articles
    text = unidecode.unidecode(text).lower()
    return re.sub(r'\W+', '-', text)