from django.urls import path


from watch_list.api.views import WatchListAV, WatchListDetailsAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewListAV, ReviewDetailsAV



urlpatterns = [
    
    # URL Patterns For WatchList
    path('list/',WatchListAV.as_view(),name='watch_list'),
    path('<int:pk>/',WatchListDetailsAV.as_view(),name='watch_list_details'),
    
    # URL Patterns For StreamPlatform
    path('stream-platform/list', StreamPlatformListAV.as_view(),name='stream_platform_list'),
    path('stream-platform/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream_platform_details'),
    
    
    # URL Patterns For Review
    path('review/list',ReviewListAV.as_view(),name='review_list'),
    path('review/<int:pk>', ReviewDetailsAV.as_view(),name='review_detail')
    
]
