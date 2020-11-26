from django.apps import AppConfig


class ProjectsSecConfig(AppConfig):
    name = 'projects_sec'

    def ready(self):
        import project_posts.signals