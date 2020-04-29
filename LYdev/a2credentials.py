import yaml

config = dict(
    search_tweets_api = dict(
        account_type = 'premium',
        endpoint = 'https://api.twitter.com/1.1/tweets/search/fullarchive/a2dev.json',
        consumer_key = 'zXoReKA7fvCP5CLiC0C2HDI3Y',
        consumer_secret = 'dpMPUWNgbc9nwq5ntanSx7DFYDWQo7hH51CHxbauX2iKyczH7r'
    )
)

with open('credentials.yaml', 'w') as config_file:
    yaml.dump(config, config_file, default_flow_style=False)