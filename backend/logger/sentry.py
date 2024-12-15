import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration

from config.sentry import BACKEND_SENTRY_DSN


def init_sentry():
    if BACKEND_SENTRY_DSN is not None:
        sentry_sdk.init(
            dsn=BACKEND_SENTRY_DSN,
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            integrations=[
                StarletteIntegration(
                    transaction_style="endpoint",
                    failed_request_status_codes=[403, range(500, 599)],
                ),
                FastApiIntegration(
                    transaction_style="endpoint",
                    failed_request_status_codes=[403, range(500, 599)],
                ),
            ]
        )
