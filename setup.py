import setuptools 

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
__version__ = '0.0.1'

REPO_NAME = 'chatbot'
AUTHOR_NAME = 'bikas-dahal'
SRC_REPO = 'chatbot'
AUTHOR_EMAIL = 'bikkydahal@gmail.com'

setuptools.setup(
    name='Medical Chatbot',
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='Medical Chatbot using Llama that provides information on various diseases and their symptoms.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    project_urls = {
        'Bug Tracker': f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues',
    },
    packages=setuptools.find_packages(where='src'),
)

# The setup.py file is used to package the project. The setup.py file is used to package the project.
