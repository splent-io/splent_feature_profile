"""
Signal handlers for the profile feature.

Connects to auth's user_registered signal to auto-create a UserProfile
when a new user signs up.
"""

from splent_io.splent_feature_auth.services import user_registered
from splent_io.splent_feature_profile.models import UserProfile
from splent_framework.db import db


@user_registered.connect
def on_user_registered(sender, user, **kwargs):
    """Create a UserProfile when a new user registers."""
    name = kwargs.get("name", "")
    surname = kwargs.get("surname", "")

    if name and surname:
        profile = UserProfile(user_id=user.id, name=name, surname=surname)
        db.session.add(profile)
        db.session.commit()
