from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    # The title of the article.
    title = models.CharField(max_length=255)

    # The slugyfied version of the articles title.
    slug = models.CharField(max_length=255)

    # The content of the article. It may contain HTML Tags.
    content = models.TextField()

    # The language tag corresponding to the language this article is written in.
    language = models.CharField(max_length=7, blank=True, null=True)

    # The icon that might be used as a cover or in an article overview.
    icon_1_url = models.TextField(blank=True, null=True)

    # The icon that might be used in the articles detail view.
    icon_2_url = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title.encode('ascii', errors='replace')
