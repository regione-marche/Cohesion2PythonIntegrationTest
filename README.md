# CohesionIntegration - Python package

Test CohesionIntegration package app

## How to use

### Step 1
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements

```bash
pip install -r requirements.txt
```

### Step 2
Update Configuration file `config.json` with your settings

```json
{
    "sso.check.url": "https://cohesion2.regione.marche.it/SPManager/WAYF.aspx",
    "sso.webCheckSessionSSO": "https://cohesion2.regione.marche.it/SPManager/webCheckSessionSSO.aspx",
    "sso.additionalData": "http://127.0.0.1:8000/logout",
    "site.URLLogin": "http://127.0.0.1:8000/callback",
    "site.URLLogout": "http://127.0.0.1:8000/logout",
    "site.IndexURL": "http://127.0.0.1:8000/",
    "site.ID_SITO": "TEST",
    "debug": true
}
```

### Step 3
Just run it as a standard fastAPI project

```
python -m uvicorn main:app --reload
```

and go to `/login` page to initiate the authentication flow

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)