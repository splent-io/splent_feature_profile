from splent_io.splent_feature_profile.repositories import UserProfileRepository
from splent_framework.services.BaseService import BaseService


class UserProfileService(BaseService):
    def __init__(self):
        super().__init__(UserProfileRepository())

    def get_by_user_id(self, user_id):
        """Get the profile for a given user id."""
        results = self.repository.get_by_column("user_id", user_id)
        return results[0] if results else None

    def update_profile(self, user_profile_id, form):
        if form.validate():
            updated_instance = self.update(user_profile_id, **form.data)
            return updated_instance, None

        return None, form.errors
