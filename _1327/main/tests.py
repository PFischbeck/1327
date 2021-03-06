from django.core.urlresolvers import reverse
from django.test import RequestFactory, TestCase
from django_webtest import WebTest
from guardian.shortcuts import assign_perm
from guardian.utils import get_anonymous_user
from model_mommy import mommy

from _1327.information_pages.models import InformationDocument
from _1327.minutes.models import MinutesDocument
from .context_processors import mark_selected
from .models import MenuItem


class TestMenuProcessor(TestCase):

	def test_mark_selected(self):
		rf = RequestFactory()
		request = rf.get('/this_is_a_page_that_most_certainly_does_not_exist.html')

		menu_item = mommy.make(MenuItem)
		try:
			mark_selected(request, menu_item)
		except AttributeError:
			self.fail("mark_selected() raises an AttributeError")


class MainPageTests(WebTest):

	def test_main_page_no_page_set(self):
		response = self.app.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_main_page_information_page_set(self):
		document = mommy.make(InformationDocument)
		assign_perm(InformationDocument.VIEW_PERMISSION_NAME, get_anonymous_user(), document)
		with self.settings(MAIN_PAGE_ID=document.id):
			response = self.app.get(reverse('index')).follow()
			self.assertEqual(response.status_code, 200)
			self.assertTemplateUsed(response, 'documents_base.html')

	def test_main_page_minutes_document_set(self):
		document = mommy.make(MinutesDocument)
		assign_perm(MinutesDocument.VIEW_PERMISSION_NAME, get_anonymous_user(), document)
		with self.settings(MAIN_PAGE_ID=document.id):
			response = self.app.get(reverse('index')).follow()
			self.assertEqual(response.status_code, 200)
			self.assertTemplateUsed(response, 'documents_base.html')
