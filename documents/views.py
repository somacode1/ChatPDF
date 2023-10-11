from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import (
    MultiPartParser,
    JSONParser
)

import cloudinary.uploader

from documents.models import Document
from documents.serializers import DocumentSerializer


class DocumentUploadView(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    
    def post(self, request):
        doc = request.data.get('file')
        
        # we expect a response after calling cloudinary.uploader() func
        # handle exceptions here when
        try:
            res_uploaded_data  = cloudinary.uploader.upload(doc)
            # After getting response create a document with the meta data we got from the response 
            print(res_uploaded_data)
            obj = Document.objects.create(
                name= res_uploaded_data['original_filename'],
                url = res_uploaded_data['url'],
                created_at = res_uploaded_data['created_at']    
            )
            return Response(data={
                "msg": "success",
                "data":res_uploaded_data,
                "id": obj.id
                }, status=status.HTTP_200_OK)
        
        except Exception as e:
            # return error
            return Response(data={"msg": str(e), "data": None}, status=status.HTTP_400_BAD_REQUEST)
            
class DocumentsAPIView(ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()