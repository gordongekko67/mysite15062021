from django.contrib import admin
from .models import Post,Articoli,Clienti,Titoli, Comment
from funzioniiot.models import Employee


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Articoli)
class ArticoliAdmin(admin.ModelAdmin):
    list_display = ('codart', 'codslug', 'codauthor', 'codpublish', 'codstatus')


@admin.register(Clienti)
class ClientiAdmin(admin.ModelAdmin):
    list_display = ('codcli', 'codslugcli', 'codauthorcli', 'codpublishcli', 'codstatuscli')


@admin.register(Titoli)
class TitoliAdmin(admin.ModelAdmin):
    list_display = ('codtit', 'codslugtit', 'codisintit', 'codbodytit', 'codmintit', 'codmaxtit')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid', 'ename', 'eemail', 'econtact')