#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=config.settings.production
pipenv lock --requirements > requirements.txt
git add -A
git add -f .secrets/ requirements.txt
eb deploy --profile fc-8th-eb --staged
git reset HEAD .secrets/ requirements.txt
rm requirements.txt