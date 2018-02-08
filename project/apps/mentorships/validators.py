from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_uni_id(value):

    # @@ ANU validation
    if not value[0] == 'u' and not len(value) == 7:
        raise ValidationError(
            _('%(value)s is not a valid ANU uni id number'),
            params={'value': value},
        )
