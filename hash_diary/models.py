import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

# A hash group is known as a pack.
# The word hash is too ambiguous between a group and an individual trail
class Pack(models.Model):
	# full name - e.g. Otter Valley (hhh can be implicit)
	name = models.CharField('Name', max_length=200, default='Your name H3')
	# Short name - e.g. OVH3 or Otter
	short_name = models.CharField('Short name', max_length=20)
	# Territory - typical area of operation in local informal terms - e.g. Exmouth to Sidmouth or in and around exeter
	territory = models.CharField('Territory', max_length=200, blank=True)
	
	REGIONS = (
		('SW', 'South West'),
	)
	
	# Region - area of the UK for future-proofing. SW for now.
	region = models.CharField('Region', max_length=10, choices=REGIONS, blank=True)
	# Frequency - informal description of run times, e.g. weekly on thurs at 19:30
	frequency = models.CharField('Frequency', max_length=200, blank=True)
	# Active - may want to archive packs
	active = models.BooleanField('Active?', null=True, default=True, blank=True)
	# Default time - default time to create events at. May vary, just pick most common.
	default_time = models.TimeField('Default start time', null=True, blank=True)
	# GM - leader
	gm = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='GM', related_name='%(class)s_pack_gm', null=True, blank=True)
	# Sec - secretary
	sec = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Sec', related_name='%(class)s_pack_sec', null=True, blank=True)
	# Email - main contact email
	email = models.EmailField('Email', null=True, blank=True)
	# Website - pack's personal website. Could also point to a social media page or group.
	website = models.URLField('Website', null=True, blank=True)
	# Text - text box to talk about your pack, give info, etc
	text = models.TextField('Text', null=True, blank=True)
	
	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ['name']
	
# A trail is an individual run.
class Trail(models.Model):
	# Pack - pack the trail belongs to
	pack = models.ForeignKey(Pack, on_delete=models.CASCADE, verbose_name='Pack')
	# Location - Start location
	location = models.CharField('Location', max_length=200, null=True, blank=True)
	# Datetime - Start time
	datetime = models.DateTimeField('Start time')
	# Hare - person/people laying the trail (text, not user)
	hare = models.CharField('Hare', max_length=200, null=True, blank=True)
	# Number - trail number for packs that like to count
	number = models.PositiveIntegerField('Number', null=True, blank=True)
	# On down - location to go to after the trail, typically a pub or person's house. Could include notes such as BYOD
	on_down = models.CharField('On down', max_length=200, null=True, blank=True)
	# Description - longer description for additional detail, e.g. directions to car park, information about food
	description = models.TextField('Description', null=True, blank=True)
	
	def __str__(self):
		od = ""
		if self.on_down is not None:
			od = ', OD %s' % self.on_down
		return '%s, %s, %s%s' % (timezone.localtime(self.datetime).strftime('%H:%M %d %b %Y'), self.pack, self.location, od)
	
	def local_day(self):
		return timezone.localtime(self.datetime).strftime('%a')
	def local_date(self):
		return timezone.localtime(self.datetime).strftime('%d %b %Y')
	def local_time(self):
		return timezone.localtime(self.datetime).strftime('%H:%M')
	class Meta:
		ordering = ['datetime']