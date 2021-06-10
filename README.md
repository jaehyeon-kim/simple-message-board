# simple-message-board

It is to design a simple message board API where users can register to get a userID, then they
can request messages, create boards and post messages to a board.

As a minimum, the API should allow a user to:

- Register for a userID by providing their name and email address
- List users
- List messageboards
- Create a new messageboard
- Post a message to a board
- Get messages from a board

Additionally, it would be great to allow users to:

- Get boards a user has posted to
- Get messages posted between certain timestamps

## Development Environment Setup

### Pipenv

```bash
PIPENV_VENV_IN_PROJECT=true python -m pipenv install
```

### Vscode

- Use [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) as the default formatter
- Use black for formating Python

```bash
# .vscode/settings.json
{
  "files.watcherExclude": {
    "**/.venv": true
  },
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.tabSize": 2,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": false,
  "python.linting.enabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackPath": "black",
  "python.formatting.blackArgs": ["--line-length", "100"],
  "[python]": {
    "editor.tabSize": 4,
    "editor.defaultFormatter": "ms-python.python"
  },
  "python.testing.pytestEnabled": true
}
```

### SAM CLI

```bash
export FILE_NAME=aws-sam-cli-linux-x86_64.zip

# install
wget https://github.com/aws/aws-sam-cli/releases/latest/download/$FILE_NAME \
  && sha256sum $FILE_NAME \
  && unzip $FILE_NAME -d sam-installation \
  && sudo ./sam-installation/install \
  && rm $FILE_NAME \
  && rm -rf sam-installation \
  && sam --version

# upgrade
wget https://github.com/aws/aws-sam-cli/releases/latest/download/$FILE_NAME \
  && sha256sum $FILE_NAME \
  && unzip $FILE_NAME -d sam-installation \
  && sudo ./sam-installation/install --update \
  && rm $FILE_NAME \
  && rm -rf sam-installation \
  && sam --version

# delete
sudo rm $(which sam) && sudo rm -rf /usr/local/aws-sam-cli
```
