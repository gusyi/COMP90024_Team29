#!/bin/bash

. ./openrc.sh; ansible-playbook --private-key=~/.ssh/team29.pem --ask-become-pass launch_instance.yml -v

# ====================================
# COMP90024 Cluster and Cloud Computing - Assignment 2
# Group 29
# Hongwei Yin 901012
# Cheng Sun 900806
# Xinyi Xu 900966
# Yiran Yao 1144268
# Xiaotao Tan 1032950
# ====================================