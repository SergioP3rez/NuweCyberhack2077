#!/bin/bash

aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set region us-east-1
aws configure set output json

awslocal s3 mb s3://arasaka
awslocal s3 cp note.txt s3://arasaka/
