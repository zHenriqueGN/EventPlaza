from django.urls import path
from .views import (
    EventAccessView,
    EventRegisterView,
    EventEditView,
    EventEditorView,
    EventDeleteView,
)

urlpatterns = [
    path("access/<int:id>", EventAccessView.as_view(), name="event_access"),
    path("register/", EventRegisterView.as_view(), name="event_register"),
    path("edit/", EventEditView.as_view(), name="event_edit"),
    path("edit/<int:id>/", EventEditorView.as_view(), name="event_editor"),
    path("delete/<int:id>/", EventDeleteView.as_view(), name="event_delete"),
]
