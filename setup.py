from setuptools import setup, find_packages

setup(
    name='Alunos API',
    version='1.0',
    long_description='API utilizada para gerenciamento de alunos. Desenvolvido por Caio Cavalcanti como teste para desenvolvedor Python',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Flask>=1.0.2',
        'pymongo',
        'connexion'
    ]
)