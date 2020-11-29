from django.urls import path, include
from rest_framework import routers 
from rest_framework_nested import routers as nested_routers 

from .views import * 

app_name = 'library'
# ストレートなルーター
router = routers.SimpleRouter()
router.register("books", BookViewSet)
router.register("authors", AuthorViewSet)
router.register("cats", CategoryViewSet)
router.register("libraries", LibraryViewSet)
router.register("info", InformationViewSet)
router.register("districts", DistrictViewSet)

book_router = nested_routers.NestedSimpleRouter(
    router, # router の 
    "books", # books の下に登録する
    lookup="book", # book の pk を探す
)

book_router.register(
    "libraries", # /books/{book_pk}/libraries/ という path なら
    BookLibraryViewSet, # このviewset を呼び出して
    basename="book-library" # ユニークなURL名をつける
)

author_router = nested_routers.NestedSimpleRouter(
    router, 
    "authors",
    lookup="author_name" # 
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_router.urls)), #book_routerも追加 
]