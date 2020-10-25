import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shopify-api-client-bwrobel99",  # Replace with your own username
    version="0.0.1",
    author="Bartosz Wrobel",
    author_email="bartoszwrobel99@gmail.com",
    description="A basic Shopify API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bwrobel99/shopify-api-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
