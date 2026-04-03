from flask import render_template, redirect, url_for, request
from flask_login import current_user
from splent_io.splent_feature_auth.decorators import login_required

from splent_io.splent_feature_profile import profile_bp
from splent_io.splent_feature_profile.forms import UserProfileForm
from splent_io.splent_feature_profile.services import UserProfileService
from splent_framework.utils.form_helpers import form_success, form_error


@profile_bp.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    service = UserProfileService()
    profile = service.get_by_user_id(current_user.id)
    if not profile:
        return redirect(url_for("public.index"))

    form = UserProfileForm()
    if request.method == "POST":
        result, errors = service.update_profile(profile.id, form)
        if result:
            return form_success("profile.edit_profile", "Profile updated successfully")
        return form_error("profile/edit.html", form, errors)

    return render_template("profile/edit.html", form=form, profile=profile)
