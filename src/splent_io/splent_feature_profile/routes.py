from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from splent_io.splent_feature_profile import profile_bp
from splent_io.splent_feature_profile.forms import UserProfileForm
from splent_io.splent_feature_profile.services import UserProfileService


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
        return service.handle_service_response(
            result,
            errors,
            "profile.edit_profile",
            "Profile updated successfully",
            "profile/edit.html",
            form,
        )

    return render_template("profile/edit.html", form=form, profile=profile)
