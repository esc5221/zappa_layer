from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zappa_layer",
    version='0.1.1',
    author="Byungwook Choi",
    author_email='esc5221@gmail.com',
    description="A tool for managing AWS Lambda layers for Zappa",
    url='https://github.com/esc5221/zappa_layer',
    license='GNU General Public License v3.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'Click'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'layer_manage = zappa_layer.layer_manage:cli'
        ],
    },
    python_requires=">=3.6,!=3.10.*,!=3.11.*",
)
