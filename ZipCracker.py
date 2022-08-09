#!/usr/bin/env python3

"""Basic zip file password cracking for Python Practice.
Does not currently support multiprocessing; use john or similar tools for real world use."""

import zipfile
import argparse
from multiprocessing import Pool
import time

def zip_attack(zip_file, pass_list):
    zip = zipfile.ZipFile(zip_file)
    count = 0
    for password in pass_list:
        count = count + 1
        try:
            zip.extractall(pwd=password.encode('utf8'))
            print(f'[+] The password is: {password}\n')
            print(f'It took {count} guesses to find the password')
            break
        except Exception:
            pass

def main(zip_name, dict_name):
    
    with open(dict_name, encoding='utf8') as dictionary_file: #Convert dictionary file into list
        pass_list = dictionary_file.read().splitlines() 

    st = time.perf_counter()
    zip_attack(zip_name,pass_list)
    et = time.perf_counter()
    print(f'Time taken: {et - st}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='Zipcracker.py ZIPFILE DICTFILE')
    parser.add_argument('-d', '--dictionary', required=True, help = 'Select the dictionary to use')
    parser.add_argument('zipfile', help='Select the zip file to use')
    args = parser.parse_args()

    try:
        main(args.zipfile, args.dictionary)
    except Exception as e:
        print(e)
        
