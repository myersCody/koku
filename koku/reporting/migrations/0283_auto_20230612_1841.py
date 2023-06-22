# Generated by Django 3.2.19 on 2023-06-12 18:41
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("reporting", "0282_auto_20230608_1819"),
    ]

    operations = [
        migrations.AlterField(
            model_name="awscomputesummarybyaccountp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awscomputesummaryp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awscostsummarybyaccountp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awscostsummarybyregionp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awscostsummarybyservicep",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awscostsummaryp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awsdatabasesummaryp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awsnetworksummaryp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awsstoragesummarybyaccountp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
        migrations.AlterField(
            model_name="awsstoragesummaryp",
            name="source_uuid",
            field=models.ForeignKey(
                db_column="source_uuid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reporting.tenantapiprovider",
            ),
        ),
    ]