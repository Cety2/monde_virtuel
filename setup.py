from setuptools import setup, find_packages


setup(
    name='monde_virtuel_library',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Liste des dépendances si nécessaire
    author='Mangobe Niandinga Cétiane',
    author_email='m_cetiane@hotmail.fr',
    description='Bibliothèque pour la simulation du monde virtuel. Les agents apprennent, intéraggissent et collaborent en temps réel selon un Codex des Lois Intelligentes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://cety2.github.io/monde_virtuel/',  # Lien vers le projet (GitHub)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)