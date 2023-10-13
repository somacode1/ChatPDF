from django.urls import path
from documents.views import (
    DocumentUploadView,
    DocumentsAPIView,
    QueryPDFAPIView
)



urlpatterns = [
    path('upload/', DocumentUploadView.as_view(), name="upload"),
    path('', DocumentsAPIView.as_view(), name="documents"),
    path('query_pdf/', QueryPDFAPIView.as_view(), name="query_pdf")
]