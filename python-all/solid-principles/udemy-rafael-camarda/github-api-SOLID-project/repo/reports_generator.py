# V3.1

class ReportGenerator():
    @classmethod
    def build(cls, generator, repos):
        return generator.build(repos)


# V3

# from .reports.html_generator import HTMLGenerator
# from .reports.markdown_generator import MarkdownGenerator


# class ReportGenerator():
#     @classmethod
#     def build(cls, type, repos):
#         if type == 'HTML':
#             return HTMLGenerator.build(repos)
#         elif type == 'Markdown': 
#             return MarkdownGenerator.build(repos)
#         else:
#             return "Invalid report type!"