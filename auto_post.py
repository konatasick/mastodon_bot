#!/usr/bin/env python

import json
import os
import logging

from mastodon import Mastodon


TOKEN_FILE = "token.json"


def validate_token(token_config):
    """Retrieve options from CONFIG. If some options are not present,
    Python will emit KeyError."""
    for user in token_config:
        user["id"]
        user["url"]
        user["token"]


def get_token(config_file, validator=validate_token):
    """Return the config dictionary."""
    config_path = os.path.split(os.path.realpath(__file__))[0] + os.sep + config_file
    try:
        with open(config_path, "r") as fl:
            config = json.load(fl)
        validator(config)
        return config

    except FileNotFoundError:
        print("找不到 %s", config_file)
        exit(1)
    except json.decoder.JSONDecodeError:
        print("%s 有语法错误，用网上的json validator检查一下吧", config_file)
        exit(1)
    except KeyError as err:
        print('%s 里缺少这个选项："%s"', config_file, err.args[0])
        exit(1)


def get_mast_dict(token_file):
    """Return a MAST_DICT.
    MAST_DICT is a hash map from weibo author id (string) to Mastodon
    instances.
    TOKEN_FILE is the filename for the token file."""
    # Because multiple weibo authors could share a single token, we
    # create an auxiliary dictionary mapping tokens to Mastodon
    # instances. Then we map authors to instances by their assigned
    # token. This way we avoid creating duplicate instances for the
    # same token for different authors.
    token_instance_map = {}
    token_config = get_token(token_file, validate_token)
    mast_dict = {}
    for user in token_config:
        id = user["id"]
        url = user["url"]
        token = user["token"]
        if token_instance_map.get(token) != None:
            # Instance already created, use it.
            mast_dict[id] = token_instance_map.get(token)
        else:
            # Instance doesn’t exist, create it.
            mast = Mastodon(access_token=token, api_base_url=url, request_timeout=30)
            mast_dict[id] = mast
            token_instance_map[token] = mast
    return mast_dict


def post_toot(text, id):
    """Post text use id"""
    print(f"Begin {id}")

    mast_dict = get_mast_dict(TOKEN_FILE)
    toot = mast_dict[id].status_post(text)

    print(f"End {id}")
    return toot
