#!/bin/bash

. ./openrc.sh; ansible-playbook -i hosts --key-file=~/.ssh/team29.pem --ask-become-pass launch_instance.yml -v