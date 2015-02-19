__author__ = 'vcaen'
import UserView

def displaySettings(request, person):
    return UserView.display_settings(request, person)

def validateSetting(request):
    return 0