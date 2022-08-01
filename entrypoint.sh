#!/usr/bin/env bash
python initial.py create_db
gunicorn --bind 0.0.0.0:8000 flasky:app