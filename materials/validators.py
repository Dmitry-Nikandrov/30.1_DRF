import re

from rest_framework.exceptions import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile("^(https://)?(www.)?youtube.com/[a-z0-9]+")
        tmp_value = dict(value).get(self.field)
        if not bool(reg.match(tmp_value)):
            raise ValidationError(
                "Ссылка недействительна. Разрешены только ссылки на youtube.com."
            )
