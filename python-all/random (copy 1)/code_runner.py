# import re

# class ArticleManager:
#     def __init__(self, article_text, options=None):
#         # Input validation
#         if not isinstance(article_text, str) or not article_text.strip():
#             raise ValueError("article_text must be a non-empty string.")
#         if options is None:
#             options = {}

#         # Assign options with validation
#         self.article_text = article_text.strip()
#         self.pages = []
#         self.words = []
#         self.options = {
#             'words_per_line': options.get('words_per_line', 12),
#             'lines_per_page': options.get('lines_per_page', 20),
#             'payment_structure': options.get('payment_structure', {
#                 1: 30, 2: 30, 3: 60, 4: 60, 'default': 100,
#             })
#         }
#         self._validate_options()

#     def _validate_options(self):
#         if not isinstance(self.options['words_per_line'], int) or self.options['words_per_line'] <= 0:
#             raise ValueError("'words_per_line' must be a positive integer.")
#         if not isinstance(self.options['lines_per_page'], int) or self.options['lines_per_page'] <= 0:
#             raise ValueError("'lines_per_page' must be a positive integer.")

#     def split_into_pages(self):
#         words_per_line = self.options['words_per_line']
#         lines_per_page = self.options['lines_per_page']

#         # Split the text into words, handle any extra spaces
#         self.words = re.split(r'\s+', self.article_text)
#         total_pages = -(-len(self.words) // (words_per_line * lines_per_page))  # math.ceil alternative

#         for i in range(total_pages):
#             start = i * words_per_line * lines_per_page
#             end = start + words_per_line * lines_per_page
#             page_words = self.words[start:end]

#             if not page_words:  # Avoid empty pages
#                 break

#             page_lines = [
#                 ' '.join(page_words[j:j + words_per_line])
#                 for j in range(0, len(page_words), words_per_line)
#             ]

#             self.pages.append('\n'.join(page_lines))

#     def calculate_payment(self):
#         payment_structure = self.options['payment_structure']
#         total_pages = len(self.pages)

#         # Default to 'default' payment if not explicitly defined
#         return payment_structure.get(total_pages, payment_structure['default'])

#     def display_payment(self):
#         total_pages = len(self.pages)
#         payment = self.calculate_payment()
#         print(f"Total Pages: {total_pages}")
#         print(f"Payment Due: ${payment}")

#     def display_pages(self):
#         for index, page in enumerate(self.pages):
#             print(f"\nPage {index + 1}:\n{page}\n")

#     def process_article(self):
#         self.split_into_pages()
#         self.display_payment()
#         self.display_pages()


# # Example usage
# article_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
# et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
# commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
# pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
# laborum."""
# article_manager = ArticleManager(article_text)
# article_manager.process_article()

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))