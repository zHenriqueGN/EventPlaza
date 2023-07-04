from django.urls import path
from .views import (
    EventListView,
    EventAccessView,
    EventRegisterView,
    EventEditView,
    EventEditorView,
    EventDeleteView,
    EventExportCSVView,
    EventCertificationsView,
)

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("access/<int:id>", EventAccessView.as_view(), name="event_access"),
    path("register/", EventRegisterView.as_view(), name="event_register"),
    path("edit/", EventEditView.as_view(), name="event_edit"),
    path("edit/<int:id>/", EventEditorView.as_view(), name="event_editor"),
    path("delete/<int:id>/", EventDeleteView.as_view(), name="event_delete"),
    path(
        "generate_csv/<int:id>/", EventExportCSVView.as_view(), name="event_export_csv"
    ),
    path("event_certifications/<int:id>", EventCertificationsView.as_view(), name="certifications")
]
