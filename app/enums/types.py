from enum import Enum

from flask_babel import _


class Type(Enum):
    WATER = {'name': _('water'), 'description': _('Water drunk by your cat')}
    FOOD = {'name': _('food'), 'description': _('Food eaten by your cat')}
    PUKE = {'name': _('puke'), 'description': _('Puke released by your cat')}
    LITTER_USED = {'name': _('litter_used'), 'description': _('Litter used by your cat')}
    LITTER_CLEANED = {'name': _('litter_cleaned'), 'description': _('Litter cleaned by someone')}
    BOWL_CLEANED = {'name': _('bowl_cleaned'), 'description': _('Litter cleaned by someone')}
