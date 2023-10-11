from django.urls import path
from documents.views import (
    DocumentUploadView,
    DocumentsAPIView
)



urlpatterns = [
    path('upload/', DocumentUploadView.as_view(), name="upload"),
    path('', DocumentsAPIView.as_view(), name="documents")
]