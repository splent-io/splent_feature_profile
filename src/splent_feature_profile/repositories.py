from splent_feature_profile.models import UserProfile
from splent_framework.repositories.BaseRepository import BaseRepository


class UserProfileRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfile)
