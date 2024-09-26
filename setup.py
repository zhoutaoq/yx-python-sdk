import re

import requests
import setuptools
from bs4 import BeautifulSoup

package_name = "yx-python-sdk"


def curr_version():
    # 方法1：通过文件临时存储版本号
    # with open('VERSION') as f:
    #     version_str = f.read()

    # 方法2：从官网获取版本号
    url = f"https://pypi.org/project/{package_name}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    latest_version = soup.select_one(".release__version").text.strip()
    return str(latest_version)


def get_version():
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", curr_version())
    major = int(match.group(1))
    minor = int(match.group(2))
    patch = int(match.group(3))

    patch += 1
    if patch > 9:
        patch = 0
        minor += 1
        if minor > 9:
            minor = 0
            major += 1
    new_version_str = f"{major}.{minor}.{patch}"
    return new_version_str


def upload():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    with open('requirements.txt') as f:
        required = f.read().splitlines()

    setuptools.setup(
        name=package_name,
        version=get_version(),
        author="zhoutaoq",
        author_email="zhoutaoq1029@126.com",
        description="common tools",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://pypi.org/project/.../",
        packages=setuptools.find_packages(),
        data_files=["requirements.txt"],
        classifiers=[
            "Programming Language :: Python :: 3.12",
            "License :: OSI Approved :: Apache License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.12',
        install_requires=required,
    )


def write_now_version():
    print("Current VERSION:", get_version())
    with open("VERSION", "w") as version_f:
        version_f.write(get_version())


def main():
    try:
        upload()
        print("Upload success , Current VERSION:", curr_version())
    except Exception as e:
        raise Exception("Upload package error", e)


if __name__ == '__main__':
    main()
