"""
Check if one or more IP address or CIDR block is in an AWS IP range.

Usage:
    python aws_ip_check.py IP [IP ...]
    
Arguments:
    IP      IP address or CIDR block

Prerequisites:
    Python 3.6+
    Install required packages:
        pip install -r requirements.txt

"""

import ipaddress
import requests
import json
import click

response = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")

try:
    data = response.json()
except json.decoder.JSONDecodeError:
    print("Error: Could not decode JSON response from AWS.")
    exit(1)


@click.command()
@click.argument("ip", nargs=-1, required=True, type=str)
def check_ip(ip):
    """Check if an IP address or CIDR block is in an AWS IP range."""
    output = []
    for prefix in data["prefixes"]:
        try:
            if ipaddress.ip_address(ip) in ipaddress.ip_network(prefix["ip_prefix"]):
                output.append(prefix)
        except ValueError:
            try:
                if ipaddress.ip_network(ip).subnet_of(
                    ipaddress.ip_network(prefix["ip_prefix"])
                ):
                    output.append(prefix)
            except ValueError:
                print(f"Invalid IP address or CIDR block: {ip}")

    if output:
        click.echo(json.dumps(output, indent=4))
    return output

if __name__ == "__main__":
    check_ip()
