
ls -la

echo "python: before .venv"
which python

python -m venv .venv
source .venv/Scripts/activate

echo "python: after .venv"
which python

npm run setup:ci
ls -la .venv/Lib/site-packages/nose/

npm ci
