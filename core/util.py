from facepy import GraphAPI
from llabs.config.conf import _get_config


def get_face_person(fb_id):
    __base = "https://graph.facebook.com/v2.4"
    __graph = GraphAPI(_get_config('token'))
    fields = 'id,name,gender,email'
    search = fb_id + '?fields=' + fields
    person = __graph.get(search)

    for f in fields.split(','):
        if f not in person:
            person[f] = 'Not in facebook'
    return person
