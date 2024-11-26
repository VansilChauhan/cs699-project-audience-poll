cd poll_app
python3 -m venv virt
source ./virt/bin/activate
pip install -r poll_app/requirements.txt

before pushing:
cd poll_app
pip freeze > requirements.txt