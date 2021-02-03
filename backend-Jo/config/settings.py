"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from .email_settings import EMAIL   # 이메일 정보가 담겨있는 py
from . import debug_settings
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!3vhrk@*^^o(^a*!@)^2mk3^opgi+(sh87y8dojontqxk0@m@t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = debug_settings.DEBUG

ALLOWED_HOSTS = [
    "localhost",
    ".ap-northeast-2.compute.amazonaws.com",
    ".inukurly.shop",
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',  # 가격에서 30,000 이런식으로 나오게 하기 위한 모듈
    'accounts',             # 회원정보 관련 앱
    'shop',                 # 제품 리스트 등 상점 앱
    'cart',                 # 장바구니 앱
    'rangefilter',          # accounts -> admin.py 에 사용됨. admin 페이지에서 모델을 범위별로 검색하기 위한 모듈
    'six',
    'main',                 # 메인 앱
    'shop_admin',           # shop 관리자 앱
    'debug_toolbar',        # 디버깅툴
    'photo',                # 이미지 업로드
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = debug_settings.INTERNAL_IPS

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATIC 파일 설정
STATIC_URL = debug_settings.STATIC_URL
STATICFILES_DIRS = [BASE_DIR / 'config' / 'static/']
STATIC_ROOT = BASE_DIR / 'staticfiles/'     # collectstatic 실행할 시 모여지는 파일
# Media files 설정 (웹 상에서 업로드 받은 이미지나 파일들이 들어갈 장소)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'     # 업로드된 파일이 들어갈 장소

SITE_ID = 1

# email 전송을 위한 setting email_settings.py에 이메일 개인정보가 들어있음.
EMAIL_USE_TLS = EMAIL['EMAIL_USE_TLS']
EMAIL_PORT = EMAIL['EMAIL_PORT']
EMAIL_HOST = EMAIL['EMAIL_HOST']
EMAIL_HOST_USER = EMAIL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = EMAIL['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# iframe 'deny' except
X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']