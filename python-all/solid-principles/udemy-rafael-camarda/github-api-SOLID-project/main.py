# V3.2

from github.client import GithubClient
from repo.parser import RepoParser
from repo.reports_generator import ReportGenerator

# Depedency injection (better than Polymorphism and Inhiretance in many cases)
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator


if __name__ == '__main__':
    username = 'LondonComputadores'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser.parse(response['body'])
        html_report = ReportGenerator.build(HTMLGenerator, repos)
        markdown_report = ReportGenerator.build(MarkdownGenerator, repos)
        print(html_report)
        print(markdown_report)
    else:
        print(response['body'])

####################################################################
        
# V3.1

# from github.client import GithubClient
# from repo.parser import RepoParser
# from repo.reports_generator import ReportGenerator


# if __name__ == '__main__':
#     username = 'LondonComputadores'
#     response = GithubClient.get_repos_by_user(username)

#     if response['status_code'] == 200:
#         repos = RepoParser.parse(response['body'])
#         html_report = ReportGenerator.build("HTML", repos)
#         markdown_report = ReportGenerator.build("Markdown", repos)
#         print(html_report)
#         print(markdown_report)
#     else:
#         print(response['body'])

######################################################################
        
# V3

# from github.client import GithubClient
# from repo.parser import RepoParser
# from repo.reports_generator import ReportGenerator


# if __name__ == '__main__':
#     username = 'LondonComputadores'
#     response = GithubClient.get_repos_by_user(username)

#     if response['status_code'] == 200:
#         repos = RepoParser.parse(response['body'])
#         html_report = ReportGenerator.build("HTML", repos)
#         markdown_report = ReportGenerator.build("Markdown", repos)
#     else:
#         print(response['body'])