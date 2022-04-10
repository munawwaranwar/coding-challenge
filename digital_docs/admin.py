from django.contrib import admin
from .models import Topic, Document, Folder


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic_name']


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'folder_name', 'topic_id']



@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'document_name', 'folder_id', 'topic_id']
