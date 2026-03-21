"""Alembic migration environment for splent_feature_profile."""

from splent_io.splent_feature_profile import models  # registers UserProfile with db.metadata  # noqa
from splent_framework.migrations.feature_env import run_feature_migrations

FEATURE_NAME = "splent_feature_profile"
FEATURE_TABLES = {"user_profile"}

run_feature_migrations(FEATURE_NAME, FEATURE_TABLES)
