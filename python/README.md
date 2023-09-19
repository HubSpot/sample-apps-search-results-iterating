# HubSpot-python Search results iterating sample app

## Requirements

1. Make sure you have [Python 3.8+](https://www.python.org/downloads/) installed.
2. [Configured](https://github.com/HubSpot/sample-apps-manage-crm-objects/blob/main/README.md#how-to-run-locally) .env file

### Running

1. Install dependencies

```bash
pip3 install -r requirements.txt
```

2. Commands

Show all commands (get help)

```bash
python cli.py -h
```

Run sample app

```bash
python cli.py -q [search_query] -s [batch_size]
```

Example:

```bash
python cli.py -q test -s 5
```
