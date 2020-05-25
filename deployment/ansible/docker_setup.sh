#!/bin/bash

. ./openrc.sh; ansible-playbook -i ./inventory/hosts --private-key=~/.ssh/team29.pem --ask-become-pass docker_setup.yml -v