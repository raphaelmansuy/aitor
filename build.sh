#!/usr/bin/env bash

poetry build
pipx install . --force
