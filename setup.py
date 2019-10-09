import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="correiosws",
    version="1.0.0",
    author="Nykollas",
    author_email="nicolauarti09@gmail.com",
    description="Conjuneto de técnicas para acesso ao serviços da API do Correios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nykollas/correiosws",
    packages=["correiosws"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
