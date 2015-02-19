from mouvinsa.user import UserManager

__author__ = 'vcaen'
import UserView

def displaySettings(request, person):
    return UserView.display_settings(person, UserView.generate_setting_form(request, person))

def validateSetting(request, person):
    form = UserView.generate_setting_form(request, person)
    if not form.errors:
        saveSettings(person, form)
        return UserView.display_profil(person)
    else:
        return UserView.display_settings(person, form)


def saveSettings(person, form):
    UserManager.change_info(person,
                            form.birthdate.data,
                            form.sex.data,
                            form.weight.data,
                            form.height.data
    )

    if form.password.data and not form.password.errors:
        UserManager.change_password(person, form.password.data)

    if form.image and not form.image.errors:
        UserManager.change_picture()
    return
