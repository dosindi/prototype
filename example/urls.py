from django.conf.urls import patterns, include, url
from example.notes.models import Note
from example.notes.views import ListNotes, CreateNote, EditNote, DeleteNote

urlpatterns = patterns('',
	url(r'^$', 'example.notes.views.index', name='home_view'),
    url(r'^area/$', ListNotes.as_view(), name='list_notes'),
    url(r'^area/create/$', CreateNote.as_view(), name='create_note'),
    url(r'^area/edit/(?P<pk>\d+)/$', EditNote.as_view(), name='edit_note'),
    url(r'^area/delete/(?P<pk>\d+)/$', DeleteNote.as_view(), name='delete_note'),
)
