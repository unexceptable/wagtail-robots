
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from robots.models import Rule


class RuleAdmin(ModelAdmin):
    model = Rule
    menu_label = 'robots.txt'
    menu_icon = "redirect"
    add_to_settings_menu = True
    list_display = (
        'robot', 'affected_sites', 'allowed_urls',
        'disallowed_urls', 'crawl_delay')

    def affected_sites(self, obj):
        sites = obj.sites.all()
        if sites:
            return ",".join([s.site_name or s.hostname for s in sites])
        else:
            return "All sites."
    affected_sites.short_description = 'sites'

    def allowed_urls(self, obj):
        urls = obj.allowed.all()
        if urls:
            return " ".join([u.pattern for u in urls])
        else:
            return None
    allowed_urls.short_description = 'allowed'

    def disallowed_urls(self, obj):
        urls = obj.disallowed.all()
        if urls:
            return " ".join([u.pattern for u in urls])
        else:
            return None
    allowed_urls.short_description = 'disallowed'


modeladmin_register(RuleAdmin)
