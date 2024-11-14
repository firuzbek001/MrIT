from modeltranslation.translator import translator, TranslationOptions
from .models import Item, TranslatedItem


@translator(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
    pass

@translator(TranslatedItem)
class TranslatedItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
    pass
