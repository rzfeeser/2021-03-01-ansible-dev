#!/usr/bin/python3
"""Russell Zachary Feeser || rzfeeser@alta3.com"""

## for accepting arguments from user at CLI
import argparse

## required for working with JSON (pystd. library)
import json

def main():
    # this is what we will ultimately return
    inventory = {}

    # Called with `--list`
    if args.list:
        # inventory is result of calling example_inventory()
        inventory = example_inventory()
    # Called with `--host [hostname]`
    elif args.host:
        # Not implemented, since we return _meta info `--list`
        # Let's put API request logic here...
        inventory = empty_inventory()
    # If no groups or vars are present, return an empty inventory.
    else:
        inventory = empty_inventory()

    # print the result of inventory
    print(json.dumps(inventory))  # from the json library use the
                                  # DUMPString function, dumps()

# Example inventory for testing.
def example_inventory():
    return {
        'group': {
            'hosts': ['bender', 'fry'],
            'vars': {
                'example_var1': 'proxyeast',
                'example_var2': 'proxywest',
                'ansible_ssh_pass': 'alta3',
                'ansible_python_interpreter': '/usr/bin/python3'
            }
        },
        '_meta': {
            'hostvars': {
                'bender': {
                    'ansible_user': 'bender',
                    'ansible_host': '10.10.2.3'
                },
                'fry': {
                    'ansible_user': 'fry',
                    'ansible_host': '10.10.2.4'
                }
            }
        }
    }

# Empty inventory for testing.
def empty_inventory():
    return {'_meta': {'hostvars': {}}}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host', action = 'store')
    args = parser.parse_args()
    main()

