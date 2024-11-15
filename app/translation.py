from modeltranslation.translator import register, translator, TranslationOptions
from .models import Item, TranslatedItem


@register(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(TranslatedItem)
class TranslatedItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
