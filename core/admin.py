from django.contrib import admin
from core.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
#admin.site.register(Compra)

class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines=(ItensInline,)