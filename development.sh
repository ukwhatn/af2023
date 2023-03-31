#!/bin/bash
cd "$(dirname "$0")"

# python requirements
pip install -r backend/requirements.txt
pip install -r db/requirements.txt
pip install -r bot/requirements.txt
pip install -r redis/py/requirements.txt
