from django.db.models import Manager


class ActiveManager(Manager):

    def get_queryset(self):
        return super(
            ActiveManager, self
        ).get_queryset().filter(status=1)
