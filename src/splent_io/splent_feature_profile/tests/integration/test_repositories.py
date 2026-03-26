"""
Integration tests for UserProfile repository.

These tests run against a real test database to verify queries,
relationships and constraints work as expected.
"""
from splent_framework.db import db
from splent_io.splent_feature_auth.models import User
from splent_io.splent_feature_profile.models import UserProfile
from splent_io.splent_feature_profile.services import UserProfileService


def test_create_and_retrieve_profile(test_client):
    with test_client.application.app_context():
        user = User(email="integration@test.com", active=True)
        user.set_password("pass123")
        db.session.add(user)
        db.session.commit()

        profile = UserProfile(user_id=user.id, name="Test", surname="User")
        db.session.add(profile)
        db.session.commit()

        service = UserProfileService()
        found = service.get_by_user_id(user.id)

        assert found is not None
        assert found.name == "Test"
        assert found.surname == "User"
        assert found.user_id == user.id


def test_profile_user_relationship(test_client):
    with test_client.application.app_context():
        user = User(email="rel@test.com", active=True)
        user.set_password("pass123")
        db.session.add(user)
        db.session.commit()

        profile = UserProfile(user_id=user.id, name="Rel", surname="Test")
        db.session.add(profile)
        db.session.commit()

        assert profile.user.email == "rel@test.com"
        assert user.profile.name == "Rel"


def test_get_by_user_id_nonexistent(test_client):
    with test_client.application.app_context():
        service = UserProfileService()
        result = service.get_by_user_id(99999)
        assert result is None
