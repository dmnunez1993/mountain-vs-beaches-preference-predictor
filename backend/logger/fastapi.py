FASTAPI_LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters":
        {
            "default":
                {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(asctime)s %(levelprefix)s %(message)s",
                    "use_colors": None,
                },
            "access":
                {
                    "()":
                        "uvicorn.logging.AccessFormatter",
                    "fmt":
                        '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',    # noqa: E501
                },
        },
    "handlers":
        {
            "default":
                {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout"
                },
            "access":
                {
                    "formatter": "access",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout"
                }
        },
    "loggers":
        {
            "uvicorn":
                {
                    "handlers": ["default"],
                    "level": "INFO",
                    "propagate": False
                },
            "uvicorn.error": {
                "level": "INFO"
            },
            "uvicorn.access":
                {
                    "handlers": ["access"],
                    "level": "INFO",
                    "propagate": False
                },
            "databases":
                {
                    "handlers": ["default"],
                    "level": "ERROR",
                    "propagate": False
                },
            "tinysched":
                {
                    "handlers": ["default"],
                    "level": "DEBUG",
                    "propagate": False
                },
        },
    "root": {
        "level": "DEBUG",
        "handlers": ["default"],
        "propagate": "no"
    }
}
