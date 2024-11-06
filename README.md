# ohmygod - CLI Tool Powered by Buddha

### Set up with Poetry

If poetry is not installed, follow [this installation steps](https://python-poetry.org/docs/).

```bash
> poetry install --no-dev
> poetry shell
> python3 -m example
```

### Set up with PIP

```bash
> # You may skip following:
> poetry export -f requirements.txt > requirements.txt

> python3 -m venv .venv
> source ./.venv/bin/activate
> python3 -m pip install -r requirements.txt
> python3 -m example
```
