
# django-elasticsearch-dsl Celery Processor


## Installation

1. Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
```bash
 pip install django-elasticsearch-dsl-celery
```

2. Add the following line to your `settings.py`:
```python
ELASTICSEARCH_DSL_SIGNAL_PROCESSOR = 'django_elasticsearch_dsl_celery.CelerySignalProcessor'
```
