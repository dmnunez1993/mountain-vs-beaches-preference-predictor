import sqlalchemy as sa
from sqlalchemy.sql import func

from database.meta import metadata

dataset = sa.Table(
    "dataset",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
        nullable=False,
    ),
    sa.Column(
        "income",
        sa.Integer,
        nullable=False,
    ),
    sa.Column(
        "travel_frequency",
        sa.Integer,
        nullable=False,
    ),
    sa.Column(
        "vacation_budget",
        sa.Integer,
        nullable=False,
    ),
    sa.Column(
        "proximity_to_mountains",
        sa.Integer,
        nullable=False,
    ),
    sa.Column(
        "proximity_to_beaches",
        sa.Integer,
        nullable=False,
    ),
    sa.Column(
        "gender",
        sa.String(15),
        nullable=False,
    ),
    sa.Column(
        "education_level",
        sa.String(15),
        nullable=False,
    ),
    sa.Column(
        "preferred_activities",
        sa.String(15),
        nullable=False,
    ),
    sa.Column(
        "location",
        sa.String(15),
        nullable=False,
    ),
    sa.Column(
        "favorite_season",
        sa.String(15),
        nullable=False,
    ),
    sa.Column(
        "age_range",
        sa.String(15),
        nullable=False,
    ),
    sa.Column(
        "pets",
        sa.Boolean,
        nullable=False,
    ),
    sa.Column(
        "environmental_concerns",
        sa.Boolean,
        nullable=False,
    ),
    sa.Column(
        "preference",
        sa.Boolean,
        nullable=False,
    ),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=func.now(),    # pylint: disable=not-callable
        nullable=False
    ),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        server_default=func.now(),    # pylint: disable=not-callable
        onupdate=func.now(),    # pylint: disable=not-callable
        nullable=False
    ),
)
