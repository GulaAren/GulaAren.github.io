import argparse

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


GH_USER_URL = 'https://github.com/{GITHUB_USERNAME}?tab=repositories'\
              '&q=&type=source'
GH_REPO_URL = 'https://github.com/{GITHUB_USERNAME}/{REPO_NAME}'


def get_pinned_repository(username: str):
    """collect listed repository list"""
    soup = get_html_content(
        GH_USER_URL.format(GITHUB_USERNAME=username)
    )
    # find span elements, class="repo"
    repo_spans = soup.find_all("span", class_="repo")
    result = []
    for repo in repo_spans:
        result.append(repo['title'])
    return result


def get_repository_data(username: str, repo_name: str):
    """Collect repository data"""
    result = {'name': repo_name}

    soup = get_html_content(GH_REPO_URL.format(
        GITHUB_USERNAME=username, REPO_NAME=repo_name
    ))

    ul = soup.find(
        'ul', class_='UnderlineNav-body list-style-none'
    )
    for li in ul.find_all('li'):
        spans = li.find_all('span')
        if 'Issues' in spans[0].string:
            result['issues'] = spans[1].string
        if 'Pull requests' in spans[0].string:
            result['pull_req'] = spans[1].string
    return result



def save_xlsx_report(repo_data_list: list):
    """Save repository data list to xlsx file"""

    workbook = Workbook()
    # Get active sheet
    worksheet = workbook.active
    # XSLX Header

    # First row is for header
    row = 1
    headers = ['Repository', 'Issues', 'Pull Request']
    columns = ['A', 'B', 'C']
    for index, col in enumerate(columns):
        cell = f'{col}{row}'
        worksheet[cell] = headers[index]

    for repo_data in repo_data_list:
        row += 1
        worksheet[f'A{row}'] = repo_data['name']
        worksheet[f'B{row}'] = repo_data['issues']
        worksheet[f'C{row}'] = repo_data['pull_req']
        print(f'repo_data: {repo_data}')

    # Save excel file
    filename = f"report.xlsx"
    workbook.save(filename)

    return filename



def get_html_content(url: str):
    """Get HTML Content from url or raise exception on error"""
    response = requests.get(url)
    # Raise exception if got error
    response.raise_for_status()
    html_text = response.text

    # Make BeautifulSoup Nested data structure
    return BeautifulSoup(html_text, 'html.parser')



def get_username() -> str:
    """Get github username from command list argument"""
    parser = argparse.ArgumentParser("Github Report")
    parser.add_argument('username')
    args = parser.parse_args()
    return args.username


def main(username: str):
    """Our main code logic"""
    repo_list = get_pinned_repository(username)
    len_repo_list = len(repo_list)
    if len_repo_list == 0:
        print(f'Pinned repository is empty')
        return
    print(f'got {len_repo_list} pinned repository: {repo_list}')

    repo_data_list = []
    for repo_name in repo_list:
      repo_data = get_repository_data(username, repo_name)
      print(f'repo_data: {repo_data}')
      repo_data_list.append(repo_data)

    if len_repo_list == 0:
        print(f'Pinned repository is empty')
        return

    # Save to xlsx file
    filename = save_xlsx_report(repo_data_list)
    print(f'Report saved to: {filename}')



# main script entry
if __name__ == '__main__':
    username = get_username()
    main(username)

