import wget
import os

from constant.path import GITHUB_URL, BASE_PATH

file_list = [
    "Basic_OOP.pdf",
    "Mamba.pdf"
]


def start():
    for filename in file_list:
        if not os.path.exists(BASE_PATH + "/resource/" + filename):
            print(f"{filename} is NOT exists.")
            print(f"Starting download {filename}")
            wget.download(GITHUB_URL + "/resource/" + filename)
        else:
            print(f"{filename} is exists. Go next file")

    print("Checking resource completed!")
