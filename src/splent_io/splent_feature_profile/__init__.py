from splent_framework.blueprints.base_blueprint import BaseBlueprint

profile_bp = BaseBlueprint("profile", __name__, template_folder="templates")


def init_feature(app):
    pass


def inject_context_vars(app):
    return {}


# Register signal handlers (auto-create profile on user registration)
from splent_io.splent_feature_profile import signals  # noqa: F401,E402

# Register template hooks (sidebar items, navbar user name)
from splent_io.splent_feature_profile import hooks  # noqa: F401,E402
