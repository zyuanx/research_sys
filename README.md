# research_sys

## About The Project

> Dynamic form, survey questionnaire backend system. Front-end repo: [vue-research-admin](https://github.com/Pandalzy/vue-research-admin)

### Api docs

![](https://gitee.com/pandalzy/cloud_img/raw/master/imgs/20200820102208.png)

### Built With

- [Django](https://docs.djangoproject.com/en/3.1/)

## Related Project

- [vue-research-admin](https://github.com/Pandalzy/vue-research-admin)

## Getting Started

### Installation

1. clone the project

```sh
git clone https://github.com/Pandalzy/research_sys.git
```

2. enter the project directory

```sh
cd research_sys
```

3. install dependency

```sh
pip install -r requirements.txt
```

### Configuration

Edit `research_sys/setting.py` file and modify mongo as your own database.

```python
# Configure mongo
from mongoengine import connect

connect('test', host='127.0.0.1', port=27017)
```

### Run

```sh
python manage.py runserver
```



## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

zyuanlee - zyuanlee@cumt.edu.cn

Project Link: [https://github.com/Pandalzy/research_sys](https://github.com/Pandalzy/research_sys)

## Acknowledgements

- [django-rest-framework](https://www.django-rest-framework.org/)
- [django-rest-framework-mongoengine](http://umutbozkurt.github.io/django-rest-framework-mongoengine/)
- [django-rest-framework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)