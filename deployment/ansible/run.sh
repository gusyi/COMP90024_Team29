#!/bin/bash

. ./openrc.sh; ansible-playbook --key-file=~/.ssh/team29.pem --ask-become-pass launch_instance.yml -v