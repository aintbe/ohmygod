# ohmygod - Console Powered by Buddha

```bash
> python3 -m venv env
> source ./env/bin/activate
> python3 -m pip install -r requirements.lock
> python3 -m example
```

### How to Deploy to PyPI

```bash
> python3 setup.py sdist bdist_wheel
> python3 -m twine upload dist/* --password $PYPI_API_TOKEN
```
