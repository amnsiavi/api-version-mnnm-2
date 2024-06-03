from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
from rest_framework import (
    generics,
    mixins
)
from rest_framework.exceptions import ValidationError
from watch_list.models import WatchList, StreamPlatform, Review
from watch_list.api.serializers import (
    WatchListSerializer,
    StreamPlatformSerialzer,
    ReviewSerialzer
    
)


class WatchListAV(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
    def get(self, request, *args, **kwargs):
        
        try:
            return Response({
                'data':self.list(request,*args,**kwargs).data,
                'status':'Successful'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Fetch Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request,*args,**kwargs):
        
        try:
            
            if len(request.data) == 0:
                return Response({
                    'status':'Failed',
                    'messgae':'No Empty Object'
                },status=HTTP_400_BAD_REQUEST)
            serialzer = self.get_serializer(data=request.data)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Fetch Successful'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Fetch Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Fetch Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Fetch Failed',
                'errors':str(e)
            })

class WatchListDetailsAV(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
    
    def get(self, request, *args, **kwargs):
        
        try:
            return Response({
                'data':self.retrieve(request,*args,**kwargs).data,
                'status':'Fetch Successful'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed Fetch',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request,*args,**kwargs):
        
        try:
            instance = self.get_object()
            
            self.perform_destroy(instance)
            
            return Response({
                'status':'Deletion Successful',
                
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                
                'status':'Failed',
                'errors':str(e)
                
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request,*args,**kwargs):
        
        try:
            
            if len(request.data) == 0:
                return Response({
                    'status':'No Data Provided'
                },status=HTTP_400_BAD_REQUEST)
            
            instance = self.get_object()
            serialzer = self.get_serializer(instance,data=request.data)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Updation Sucessful'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Updation Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Updation Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Failed to Update',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request, *args, **kwargs):
        
        try:
            
            if len(request.data) == 0:
                return Response({
                    'status':'Updation Failed',
                    'errors':'No Empty Objects'
                },status=HTTP_400_BAD_REQUEST)
            instance = self.get_object()
            serialzer  = self.get_serializer(instance,data=request.data,partial=True)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Updation Sucessful'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Updation Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Updation Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'errors':str(e),
                'status':'Updation Failed'
            },status=HTTP_500_INTERNAL_SERVER_ERROR)


# StreamPlatform Views

class StreamPlatformListAV(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerialzer
    
    
    def get(self,request,*args,**kwargs):
        
        try:
            return Response({
                'data':self.list(request,*args,**kwargs).data,
                'status':'Success'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed To Fetch',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request,*args,**kwargs):
        
        try:
            if len(request.data) ==   0:
                return Response({
                    'status':'Failed',
                    'errors':'Recieved Empty Object'
                },status=HTTP_400_BAD_REQUEST)
            serialzer = self.get_serializer(data=request.data)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Success'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'staus':'Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Failed To Create',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)

class StreamPlatformDetailAV(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerialzer
    
    def get(self,request,*args,**kwargs):
        
        try:
            return Response({
                'data':self.retrieve(request,*args,**kwargs).data,
                'status':'Success'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request,*args,**kwargs):
        
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            
            return Response({
                'status':'Deletion Successful'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            })
    
    def put(self, request,*args,**kwargs):
        
        try:
            if len(request.data) == 0:
                return Response({
                    'status':'Updation Failed',
                    'msg':'Recieved Empty Object'
                },status=HTTP_400_BAD_REQUEST)
            instance = self.get_object()
            serialzer = self.get_serializer(instance,data=request.data)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Updation Sucessful'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Updation Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Updation Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Updation Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self,request,*args,**kwargs):
        
        try:
            if len(request.data) == 0:
                return Response({
                    'status':'Failed',
                    'msg':'Recieved Empty Object'
                },status=HTTP_400_BAD_REQUEST)
            instance = self.get_object()
            serialzer = self.get_serializer(instance,data=request.data,partial=True)
            
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Success'
                },status=HTTP_200_OK)
            else:
                return Response({
                    'status':'Failed',
                    'errors':serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
            
            
# Review Model Views

class ReviewListAV(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzer
    
    
    def get(self, request,*args,**kwargs):
        
        try:
            return Response({
                'data':self.list(request,*args,**kwargs).data,
                'status':'Success'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, *args, **kwargs):
        
        try:
            if len(request.data) == 0:
                return Response({
                    'status':'Failed',
                    'errors':'Revieved Empty Objects'
                },status=HTTP_400_BAD_REQUEST)
            serialzer = self.get_serializer(data=request.data)
            if serialzer.is_valid():
                serialzer.save()
                return Response({
                    'data':serialzer.data,
                    'status':'Success'
                })
            else:
                return Response({
                    'status':'Failed',
                    'errors': serialzer.errors
                },status=HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({
                'status':'Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)

class ReviewDetailsAV(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzer
    def get(self,request,*args,**kwargs):
        
        try:
            return Response({
                'data':self.retrieve(request,*args,**kwargs).data,
                'status':'Success'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, *args, **kwargs):
        
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'status':'Deletion Sucessful'
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed',
                'errors':str(e)
            },status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def put(self,request,*args,**kwargs):
        
        try:
            if len(request.data) == 0:
                return Response({
                    'status':'Updation Failed',
                    'errors':'Recieved Empty Object'
                })
        except ValidationError as ve:
            return Response({
                'status':'Updation Failed',
                'errors':ve.detail
            },status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status':'Updation Failed',
                'errors':str(e)
            })
    
    def patch(self, request, *args, **kwargs):
        
        pass
        
