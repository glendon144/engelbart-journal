#!/bin/bash

echo "========================"
echo "DemoKit Phase 5.1 Mac M1 Turn-Key Installer"
echo "========================"

python3 -m venv demokit-env
source demokit-env/bin/activate

pip install --upgrade pip
pip install pandas openai

echo ""
echo "✅ Setup complete!"
echo "To start DemoKit:"
echo "source demokit-env/bin/activate"
echo "python main.py"
