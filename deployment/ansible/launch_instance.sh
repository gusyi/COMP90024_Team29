#!/bin/bash

. ./openrc.sh; ansible-playbook --private-key=~/.ssh/team29.pem --ask-become-pass launch_instance.yml -vv