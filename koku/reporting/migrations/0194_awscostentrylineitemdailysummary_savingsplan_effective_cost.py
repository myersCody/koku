# Generated by Django 3.1.12 on 2021-09-09 14:23
import pkgutil

from django.db import connection
from django.db import migrations
from django.db import models


def add_aws_views(apps, schema_editor):
    """Create the AWS Materialized views from files."""
    version = "_20210910"
    views = {
        f"sql/views/{version}/reporting_aws_compute_summary": ["", "_by_account", "_by_region", "_by_service"],
        f"sql/views/{version}/reporting_aws_cost_summary": ["", "_by_account", "_by_region", "_by_service"],
        f"sql/views/{version}/reporting_aws_storage_summary": ["", "_by_account", "_by_region", "_by_service"],
        f"sql/views/{version}/reporting_aws_database_summary": [""],
        f"sql/views/{version}/reporting_aws_network_summary": [""],
    }
    for base_path, view_tuple in views.items():
        for view in view_tuple:
            view_sql = pkgutil.get_data("reporting.provider.aws", f"{base_path}{view}{version}.sql")
            view_sql = view_sql.decode("utf-8")
            with connection.cursor() as cursor:
                cursor.execute(view_sql)


class Migration(migrations.Migration):

    dependencies = [("reporting", "0193_gcptopology")]

    operations = [
        migrations.AddField(
            model_name="awscostentrylineitemdailysummary",
            name="savingsplan_effective_cost",
            field=models.DecimalField(decimal_places=9, max_digits=24, null=True),
        ),
        migrations.RunPython(add_aws_views),
    ]