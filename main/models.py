from django.db import models

from root.app_utils.meta_models.meta import MetaModel


class LogEntry(MetaModel):
    user = models.ForeignKey(
        'auth.User',
        related_name='logs',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'log_entry'
        verbose_name = 'Log entry'
        verbose_name_plural = 'Log entries'

    def __str__(self) -> str: return self.user.username
