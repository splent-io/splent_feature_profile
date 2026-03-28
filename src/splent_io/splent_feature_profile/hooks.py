from splent_framework.hooks.template_hooks import register_template_hook
from flask import render_template


def sidebar_edit_profile():
    return render_template("hooks/sidebar_edit_profile.html")


def navbar_user_name():
    return render_template("hooks/navbar_user_name.html")


register_template_hook("layout.sidebar.authenticated.items", sidebar_edit_profile)
register_template_hook("layout.navbar.authenticated", navbar_user_name)
