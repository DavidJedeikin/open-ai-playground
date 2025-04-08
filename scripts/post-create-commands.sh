#!/bin/bash

# Line break
echo " " >> ~/.bashrc

# Source the API key
source /workspace/open-api-key.sh

echo "Exporting OpenAI API Key"
printf '\nexport OPENAI_API_KEY=${OPEN_AI_KEY}\n' >> ~/.bashrc

echo "Enabling coloured integrated terminal"
printf '\nexport TERM=xterm-256color\n' >> ~/.bashrc

echo "Adding productivity aliases"
cat /workspace/scripts/productivity.sh >> ~/.bashrc

echo "Installing and configuring python environment"
python -m venv .venv
.venv/bin/pip install -r requirements.txt 




