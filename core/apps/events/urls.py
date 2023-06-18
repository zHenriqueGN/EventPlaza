from django.urls import path
from .views import EventRegisterView, EventEditView, EventEditorView, EventDeleteView

urlpatterns = [
    path("register/", EventRegisterView.as_view(), name="event_register"),
    path("edit/", EventEditView.as_view(), name="event_edit"),
    path("edit/<int:id>/", EventEditorView.as_view(), name="event_editor"),
    path("delete/<int:id>/", EventDeleteView.as_view(), name="event_delete"),
]
