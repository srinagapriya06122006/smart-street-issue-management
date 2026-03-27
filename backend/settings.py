# import os
# from pathlib import Path
# import pymysql  # type: ignore
# pymysql.install_as_MySQLdb()




# # -----------------------------------------------------------------------------
# # Django settings for auth-only project (register + login).
# # -----------------------------------------------------------------------------

# BASE_DIR = Path(__file__).resolve().parent

# # Allow you to override from env, but keep a dev-friendly default.
# SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-m#$v-^v-p)69=o3#*k$!5_b$a!_p-^6u!n$^5_b$a!_p-^6")
# DEBUG = os.getenv("DJANGO_DEBUG", "1") == "1"

# ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")


# # -----------------------------------------------------------------------------
# # Applications
# # -----------------------------------------------------------------------------

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "corsheaders",
#     "rest_framework",
#     "auth_app",
#     "complaint_app",
# ]


# # -----------------------------------------------------------------------------
# # Middleware
# # -----------------------------------------------------------------------------

# MIDDLEWARE = [
#     "corsheaders.middleware.CorsMiddleware",
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]


# ROOT_URLCONF = "urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     }
# ]

# WSGI_APPLICATION = "wsgi.application"


# # -----------------------------------------------------------------------------
# # Database (MySQL via pymysql)
# # -----------------------------------------------------------------------------

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.getenv("DB_NAME", "civix_auth"),
#         "USER": os.getenv("DB_USER", "root"),
#         "PASSWORD": os.getenv("DB_PASSWORD", "Mass@162"),  # Note: Keep fallback
#         "HOST": os.getenv("DB_HOST", "127.0.0.1"),
#         "PORT": os.getenv("DB_PORT", "3306"),
#         "OPTIONS": {
#             "charset": "utf8mb4",
#         },
#     }
# }


# # -----------------------------------------------------------------------------
# # Password validation
# # -----------------------------------------------------------------------------

# AUTH_PASSWORD_VALIDATORS = []


# # -----------------------------------------------------------------------------
# # Internationalization
# # -----------------------------------------------------------------------------

# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True


# # -----------------------------------------------------------------------------
# # Static files
# # -----------------------------------------------------------------------------

# STATIC_URL = "static/"


# # -----------------------------------------------------------------------------
# # REST Framework + CORS
# # -----------------------------------------------------------------------------

# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ORIGIN_ALLOW_ALL = True  # Legacy fallback

# REST_FRAMEWORK = {
#     "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
#     "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
# }


# # -----------------------------------------------------------------------------
# # Default primary key type
# # -----------------------------------------------------------------------------

# # ---------------------------------------------------------------------
# COMPLAINT APP SETTINGS
# ---------------------------------------------------------------------

COMPLAINT_SLA_MINUTES = 1

import pymysql  # type: ignore
pymysql.version_info = (2, 2, 1, "final", 0)  # Fake version for Django
pymysql.install_as_MySQLdb()

import os
from pathlib import Path

# ---------------------------------------------------------------------
# BASIC SETTINGS
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = "dev-secret-key"

DEBUG = True

ALLOWED_HOSTS = []


# ---------------------------------------------------------------------
# APPLICATIONS
# ---------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "auth_app",
    "complaint_app",   # keep if you use it
]


# ---------------------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ---------------------------------------------------------------------
# URL / TEMPLATE
# ---------------------------------------------------------------------

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR.parent, "frontend")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "wsgi.application"



# ---------------------------------------------------------------------
# DATABASE (✅ MYSQL ENABLED)
# ---------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "civix_auth"),
        "USER": os.getenv("DB_USER", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", "Sri@2006"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    }
}


# ---------------------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = []


# ---------------------------------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------------------

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR.parent, "frontend")]


# ---------------------------------------------------------------------
# CORS + REST
# ---------------------------------------------------------------------

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
}


# ---------------------------------------------------------------------
# DEFAULT PRIMARY KEY
# ---------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------
# COMPLAINT SYSTEM SETTINGS
# ---------------------------------------------------------------------
COMPLAINT_SLA_MINUTES = 1