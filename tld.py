#!/usr/bin/python3
# scrappy program that searches through IANA's database of the managers of
# Top-Level Domains.
#
# USAGE: ./tld_info manager_name
#
# EXAMPLE: ./tld_info amazon
#          prints the number of TLDs amazon managers, and lists them all.
#
# work in progress :)

from data import html_doc
from bs4 import BeautifulSoup
from sys import argv

query = " ".join(argv[1:]).upper()

# make the soup
soup = BeautifulSoup(html_doc, 'lxml')
text = soup.get_text()
word_list = text.split('\n')
words = [word for word in word_list if word != '']

# never display these
invalid_tokens = {'generic', '', '\n', 'sponsored', 'country-code'}

domain_count = 0
print('-' * 60)
for i in range(len(words)):
    if query in words[i].upper() and words[i][0] != '.':
        domain_count += 1
print(f'results for {query.upper()} ({domain_count} domains)')
print('-' * 60)

format_count = 1    # just for looks
for i in range(len(words)):
    if query in words[i].upper():
        if words[i-2] not in invalid_tokens:
            print(f'{words[i-2]}', end=" ")
        if format_count % 8 == 0: # just for looks
            print()
        format_count += 1
print()
print('-' * 60)
