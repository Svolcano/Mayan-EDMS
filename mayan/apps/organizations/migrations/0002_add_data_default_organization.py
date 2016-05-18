# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def default_data(apps, schema_editor):
    # We can't import the Organization model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Organization = apps.get_model("organizations", "Organization")
    default_organization = Organization(id=1, label='Default')
    default_organization.save()


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_data),
    ]
