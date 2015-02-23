import os
from mouvinsa.user import UserManager


import UserView

def displaySettings(request, person):
    return UserView.display_settings(person, UserView.generate_setting_form(request, person))

def validateSetting(request, person):
    form = UserView.generate_setting_form(request, person)
    if not form.errors:
        saveSettings(person, form)
        file = request.files['image']
        if file:
            UserManager.change_picture(person, file)
        else:
            return "Error with the picture"
        return UserView.display_profil(person)
    else:
        return UserView.display_settings(person, form)


def saveSettings(person, form):
    if form.password.data and not form.password.errors:
        UserManager.change_password(person, form.password.data)

    if form.image.data and not form.image.errors:
        UserManager.change_picture()

    UserManager.update_from_form(person, form)

    # UserManager.change_info(person,
    #                         form.birthdate.data,
    #                         form.sex.data,
    #                         form.weight.data,
    #                         form.height.data,
    #                         form.firstname,
    #                         form.lastname,
    # )

    return

def validateStepsData(request, person):

    return UserManager.update_steps_ajax(person=person, form=request.form)