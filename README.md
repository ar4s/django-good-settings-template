# {{ project_name }}

Available commands:

* {{ project_name }} -- run with ``settings.prod``
* dev_{{ project_name }} -- run with ``settings.dev``
* test_{{ project_name }} -- run with ``settings.test``


Install requirements for each env by following command
    
    pip install -e '.[ENV]'

Where ``ENV`` is your target environment.
