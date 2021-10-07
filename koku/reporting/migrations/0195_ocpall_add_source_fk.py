# Generated by Django 3.1.13 on 2021-09-24 15:01
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0049_auto_20210818_2208"),
        ("reporting", "0194_awscostentrylineitemdailysummary_savingsplan_effective_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ocpallcostlineitemdailysummaryp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid", null=True, on_delete=django.db.models.deletion.CASCADE, to="api.provider"
            ),
        ),
        migrations.AlterField(
            model_name="ocpallcostlineitemprojectdailysummaryp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid", null=True, on_delete=django.db.models.deletion.CASCADE, to="api.provider"
            ),
        ),
    ]