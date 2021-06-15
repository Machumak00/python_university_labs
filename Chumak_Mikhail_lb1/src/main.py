import wikipedia as wk
from help_wiki_function import is_page_valid


def is_lang_valid(language):
    if language in wk.languages():
        return True
    else:
        return False


def max_words_in_page(title_of_page):
    words = []
    title = ""
    count = 0
    for i in range(len(title_of_page)):
        words = wk.page(title_of_page[i]).summary.split()
        if len(words) >= count:
            count = len(words)
            title = wk.page(title_of_page[i]).title
    arguments = [count, title]
    return arguments


def find_links(title_of_page):
    chain = [title_of_page[0]]
    for i in range(len(title_of_page) - 1):
        if title_of_page[i + 1] in wk.page(title_of_page[i]).links:
            chain.append(title_of_page[i + 1])
        else:
            for x in wk.page(title_of_page[i]).links:
                if is_page_valid(x):
                    if title_of_page[i + 1] in wk.page(x).links:
                        chain.append(x)
                        chain.append(title_of_page[i + 1])
                        break
    return chain


titles = input().split(", ")
lang = titles.pop()
if is_lang_valid(lang):
    wk.set_lang(lang)
    args = max_words_in_page(titles)
    print(args[0], args[1])
    print(find_links(titles))
else:
    print("no results")
