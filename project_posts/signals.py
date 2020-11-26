from django.db.models.signals import post_save
from projects_sec.models import Projects
from django.dispatch import receiver
from .models import P_Post


@receiver(post_save, sender=Projects)
def create_p_post(sender, instance, created, **kwargs):
    if created:
        P_Post.objects.create(project=instance)


@receiver(post_save, sender=Projects)
def save_p_post(sender, instance, **kwargs):
    instance.p_post.save()




