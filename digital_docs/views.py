from django.shortcuts import render
from .models import Topic, Folder, Document
from .serializers import TopicSerializer, FolderSerializer, DocumentSerializer
from rest_framework import viewsets
from django.db.models import Q


class DocumentViewSet(viewsets.ModelViewSet):
    
    serializer_class = DocumentSerializer

    def get_queryset(self):
        """ 
        To override the get_queryset method to capture query parameters
        and manipulate accordingly
        """
        
        if self.request.query_params:
            topic = self.request.query_params.get('topic')
            folder = self.request.query_params.get('folder')

            topic_id = Topic.objects.filter(topic_name=topic).first()
            folder_id = Folder.objects.filter(folder_name=folder).first()

            if topic_id and folder_id:
                queryset = Document.objects.filter(Q(topic_id=topic_id) & Q(folder_id=folder_id))
            elif not folder_id:
                queryset = Document.objects.filter(topic_id=topic_id)
            elif not topic_id:
                queryset = Document.objects.filter(folder_id=folder_id)  
        else:
            queryset = Document.objects.all().order_by('id')

        return queryset


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
