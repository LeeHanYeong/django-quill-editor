from django.contrib.admin.apps import AdminConfig as DefaultAdminConfig

__all__ = ("AdminConfig",)


class AdminConfig(DefaultAdminConfig):
    default_site = "config.admin.AdminSite"
