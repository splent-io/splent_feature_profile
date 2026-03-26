from splent_io.splent_feature_auth.models import User
from splent_io.splent_feature_profile.models import UserProfile
from splent_framework.seeders.BaseSeeder import BaseSeeder


class ProfileSeeder(BaseSeeder):

    priority = 2  # After AuthSeeder (priority 1)

    def run(self):
        users = User.query.all()
        names = [("John", "Doe"), ("Jane", "Doe")]

        profiles = []
        for user, (name, surname) in zip(users, names):
            if not user.profile:
                profiles.append(UserProfile(user_id=user.id, name=name, surname=surname))

        if profiles:
            self.seed(profiles)
