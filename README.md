# AWS IP Check

This script checks if one or more IP address or CIDR block is in an AWS IP range. It uses the [AWS IP Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) JSON file to determine the IP ranges.

## Usage

```python
python aws_ip_check.py IP [IP ...]
```

Arguments:

- `IP`: IP address or CIDR block

## Prerequisites

- Python 3.6+
- Install required packages:

    ```
    pip install -r requirements.txt
    ```

## Example

```bash
python aws_ip_check.py 192.0.2.1 
[
    {
        "ip_prefix": "192.0.2.0/24",
        "region": "us-east-1",
        "service": "AMAZON"
    }
]
```
