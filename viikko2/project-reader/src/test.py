x = {'tool': 
    {'poetry': 
        {'name': 'web-login-robot', 'version': '0.1.0', 
        'description': '', 
        'authors': ['Kalle Ilves <kalle.ilves@helsinki.fi>'], 
        'dependencies': {'python': '^3.6', 'Flask': '^1.1.2'}, 
        'dev-dependencies': {'robotframework': '^3.2.2', 'robotframework-seleniumlibrary': '^4.5.0', 'requests': '^2.24.0'}}
    }, 
    'build-system': {'requires': ['poetry-core>=1.0.0'], 'build-backend': 'poetry.core.masonry.api'}
}
print(x['tool']['poetry']['name'])