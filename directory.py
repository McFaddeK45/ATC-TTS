# Python Module Directory/Database
from pathlib import Path
import os
import fnmatch
# import zipfile; for later
import fileinput
# from tempfile import TemporaryFile

# import sys; for later

# Creation of a directory using paths
direct_path = Path('ATC_directory/')
# if the path already exists show the user
try:
    direct_path.mkdir()
except FileExistsError as exc:
    print(exc)

    # get some input from gui to pick a file type


def text_file():
    # Filename matching; text files; searches for .txt files
    for file_name in os.listdir('ATC_directory/'):
        if fnmatch.fnmatch(file_name, '*.txt'):
            print(file_name)
    # can possibly expand to search for .txt files with keywords from the user

    # walk directory tree and print names of directories and file
    for txt_path, txt_names, files in os.walk('.'):
        print(f'found directory: {txt_path}')
        for txt_file_name in files:
            print(txt_file_name)


def wav_file():
    # Filename matching; wav files; searches for .wav files
    for audio_file_name in os.listdir('ATC_directory/'):
        if fnmatch.fnmatch(audio_file_name, '*.wav'):
            print(audio_file_name)
    # can possibly expand to search for .wav files with keywords from the user

    # walk directory tree and print names of directories and file
    for wav_path, wav_names, files in os.walk('.'):
        print(f'found directory: {wav_path}')
        for wav_file_name in files:
            print(wav_file_name)


def zip_file():
    # Filename matching; zip files; searches for .zip files
    for zip_file_name in os.listdir('ATC_directory/'):
        if fnmatch.fnmatch(zip_file_name, '*.zip'):
            print(zip_file_name)
    # can possibly expand to search for .zip files with keywords from the user

    # walk directory tree and print names of directories and file
    for zip_path, zip_names, files in os.walk('.'):
        print(f'found directory: {zip_path}')
        for zipp_file_name in files:
            print(zipp_file_name)

    # reading zip file


def mp3_file():
    # Filename matching; mp3 files; searches for .mp3 files
    for mp3_file_name in os.listdir('ATC_directory/'):
        if fnmatch.fnmatch(mp3_file_name, '*mp3'):
            print(mp3_file_name)
    # can possibly expand to search for .mp3 files with keywords from the user

    # walk directory tree and print names of directories and file
    for mp3_path, mp3_names, files in os.walk('.'):
        print(f'found directory: {mp3_path}')
        for mp_file_name in files:
            print(mp_file_name)


def multi_files():
    # Gets information from multiple files
    files = fileinput.input()
    for line in files:
        if fileinput.isfirstline():
            print(f'\n---Reading {fileinput.filename()}---')
        print('->' + line, end='')
    print()


def user_input_direct():
    # Get basic user input
    print('Please enter one of the following file types \n .txt, .mp3, .wav, .zip')
    file_input_type = input("")
    print(file_input_type)
