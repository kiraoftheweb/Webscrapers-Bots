#Imports
import logging
import coloredlogs
import requests
from bs4 import BeautifulSoup
#Defined
logger = logging.getLogger(__name__)
FMT = ("%(asctime)s - %(message)s")
coloredlogs.install(fmt=FMT, logger=logger)
F = open("us-proxy.txt", "w+")
HEADERS = requests.utils.default_headers()
HEADERS.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
URL = "https://www.us-proxy.org/"
PAGE = requests.get(URL, headers=HEADERS)
CONTENT = PAGE.text

def read_header(tr):
    """Read all the <th> columns in a <tr> row.

    Args:
      tr: the Soup row element
    Returns:
      The list of th text values, if any.
    """
    header = []
    for th in tr.find_all('th'):
        header.append(th.text.strip())
    return header

def read_row(tr):
    """Read all the <td> columns in a <tr> row.

    Args:
      tr: the Soup row element
    Returns:
      The list of td cell text values, if any.
    """
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    return row

def read_table(table):
    """Read an IP Address table.

    Args:
      table: the Soup <table> element
    Returns:
      None if the table isn't an IP Address table, otherwise a list of
        the IP Address:port values.
    """
    header = None
    rows = []
    for tr in table.find_all('tr'):
        if header is None:
            header = read_header(tr)
            if not header or header[0] != 'IP Address':
                return None
        else:
            row = read_row(tr)
            if row:
                rows.append('{}:{}'.format(row[0], row[1]))
    return rows

def load_page():
    with open('content.html', 'w') as output:
        output.write(CONTENT)


def parse_page():
    with open('content.html') as infile:
        CONTENT = infile.read()

    SOUP = BeautifulSoup(CONTENT, 'lxml')

    result = []
    for table in SOUP.find_all('table'):
        header = None
        rows = read_table(table)
        if rows:
            result.append(rows)

    for rs in result:
        for r in rs:
            logger.info(r)
            F.write(str(r + '\n'))

load_page()
parse_page()


