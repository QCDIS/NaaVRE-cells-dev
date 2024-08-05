
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_api_key = os.getenv('secret_api_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_server_url', action='store', type=str, required=True, dest='param_server_url')

args = arg_parser.parse_args()
print(args)

id = args.id


param_server_url = args.param_server_url.replace('"','')


print(param_server_url)
print(secret_api_key)

