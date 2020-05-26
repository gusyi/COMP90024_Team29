#!/bin/bash

nohup python3 tweet_stream_vic.py 172.26.133.229 stream-vic stream-victoria >nohup1.out 2>&1 &
nohup python3 tweet_stream_mel.py 172.26.133.240 stream-mel stream-melbourne >nohup2.out 2>&1 &