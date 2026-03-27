"""
Unit tests for UserProfileService.

These tests mock the repository so they run without a database.
"""

from unittest.mock import MagicMock
from splent_io.splent_feature_profile.services import UserProfileService


def test_get_by_user_id_returns_profile():
    service = UserProfileService()
    mock_profile = MagicMock(user_id=1, name="John", surname="Doe")
    service.repository = MagicMock()
    service.repository.get_by_column.return_value = [mock_profile]

    result = service.get_by_user_id(1)

    assert result == mock_profile
    service.repository.get_by_column.assert_called_once_with("user_id", 1)


def test_get_by_user_id_returns_none_when_not_found():
    service = UserProfileService()
    service.repository = MagicMock()
    service.repository.get_by_column.return_value = []

    result = service.get_by_user_id(999)

    assert result is None


def test_update_profile_with_valid_form():
    service = UserProfileService()
    service.update = MagicMock(return_value=MagicMock())

    mock_form = MagicMock()
    mock_form.validate.return_value = True
    mock_form.data = {"name": "Jane", "surname": "Smith"}

    result, errors = service.update_profile(1, mock_form)

    assert result is not None
    assert errors is None
    service.update.assert_called_once_with(1, name="Jane", surname="Smith")


def test_update_profile_with_invalid_form():
    service = UserProfileService()

    mock_form = MagicMock()
    mock_form.validate.return_value = False
    mock_form.errors = {"name": ["Required"]}

    result, errors = service.update_profile(1, mock_form)

    assert result is None
    assert errors == {"name": ["Required"]}
