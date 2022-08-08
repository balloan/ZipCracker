#!/usr/bin/env python3
"""Basic zip file password cracking for Python Practice.
Does not currently support multiprocessing; use john or similar tools for real world use."""

import zipfile
import argparse

def zip_attack(zip_file, password):
    # Attempts to extract a zipped file with the password provided
    try:
        zip_file.extractall(pwd=password.encode('utf-8'))
        print(f'[+] The password is: {password}\n')
    except RuntimeError:
        pass

def main(zip_name, dict_name):
    z_file = zipfile.ZipFile(zip_name)
    with open(dict_name) as dictionary_file:
        for line in dictionary_file:
            password = line.strip('\n')
            zip_attack(z_file,password)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='Zipcracker.py ZIPFILE -d DICTFILE')
    parser.add_argument('-d', '--dictionary', required=True, help = 'Select the dictionary to use')
    parser.add_argument('zipfile', help='Select the zip file to use')
    args = parser.parse_args()

    try:
        main(args.zipfile, args.dictionary)
    except Exception as e:
        print(e)
        
