from distutils.version import LooseVersion

from django.conf import settings

from wagtail import VERSION as WAGTAIL_VERSION
if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import InlinePanel
else:
    from wagtail.admin.edit_handlers import InlinePanel


def WrappedInlinepanel(relation_name, heading='', label='',
                       card_header_from_field=None, new_card_header_text='',
                       **kwargs):
    klass = InlinePanel
    if 'condensedinlinepanel' in settings.INSTALLED_APPS:
        import condensedinlinepanel
        from condensedinlinepanel.edit_handlers import CondensedInlinePanel
        if LooseVersion(
                condensedinlinepanel.__version__) >= LooseVersion('0.3'):
            klass = CondensedInlinePanel
            defaults = {
                'heading': heading,
                'label': label,
                'card_header_from_field': card_header_from_field,
                'new_card_header_text': new_card_header_text,
            }
    else:
        if WAGTAIL_VERSION >= (2, 0):
            defaults = {
                'heading': heading,
                'label': label,
            }
        else:
            defaults = {
                'label': label,
            }

    defaults.update(kwargs)
    return klass(relation_name, **defaults)
