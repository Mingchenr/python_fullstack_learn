

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-ywg^3@$x07@2n)ovlvok1o4vd4#3o&3$@y4_=hbg2193145o5b'


DEBUG = True

ALLOWED_HOSTS = []





INSTALLED_APPS = [
    'user.apps.UserConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_learn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
             ],
        },
    },
]

WSGI_APPLICATION = 'django_learn.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 语言编码 - 设置为简体中文,可以用 'zh-cn'，但 'zh-hans' 是更标准的国际代码
LANGUAGE_CODE = 'zh-hans'

# 时区 - 设置为中国时区,中国标准时间(CST)，覆盖北京/上海等所有中国地区
TIME_ZONE = 'Asia/Shanghai'
# 确保使用时区感知的时间（生产环境推荐）
USE_TZ = True

# 启用国际化（如果需要）
USE_I18N = True

# 启用本地化（如果需要）
USE_L10N = True


STATIC_URL = 'static/'

