# HubSpot-ruby Search results iterating sample app

## Requirements

1. ruby 2.6.3
2. [Configured](https://github.com/HubSpot/sample-apps-manage-search-results-iterating/blob/main/README.md#how-to-run-locally) .env file

### Running

1. Install dependencies

```bash
bundle install
```

2. Commands

Show all commands (get help)

```bash
ruby cli.rb -h
```

Run sample app

```bash
ruby cli.rb -q [search_query] -s [batch_size]
```

Example:

```bash
ruby cli.rb -q test -s 5
```
