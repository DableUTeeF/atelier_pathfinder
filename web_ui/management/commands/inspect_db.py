from web_ui.models import Material
from django.utils import timezone

class Command:

    def run_from_argv(self, *args, **kwargs):
        pass


uid = 'U444899655f2a3e784b498097fa8d961d'
# a = Material(
#     name='Uni'
# )
# a.save()
a = Material.nodes.all()
now = timezone.now()
print(a)
