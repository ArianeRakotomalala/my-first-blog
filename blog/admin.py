from django.contrib import admin
from .models import Post

admin.site.register(Post)
# nous importons le modèle « Post » que nous avons écrit dans le chapitre précédent. Afin que notre 
# modèle soit visible dans l'interface d'administration, nous avons besoin d'enregistrer notre modèle à
#l'aide de admin.site.register(Post).