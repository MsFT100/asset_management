# Generated by Django 4.2.2 on 2023-07-03 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('employee', '0002_alter_employee_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_tag', models.CharField(max_length=255)),
                ('model_id', models.IntegerField()),
                ('serial_no', models.CharField(max_length=191, null=True)),
                ('purchase_date', models.DateField()),
                ('asset_eol_date', models.DateField(null=True)),
                ('purchase_cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('order_number', models.CharField(max_length=191)),
                ('comments', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/devices/')),
                ('physical', models.BooleanField(default=True)),
                ('status', models.IntegerField()),
                ('archived', models.BooleanField(default=False)),
                ('rtd_location_id', models.IntegerField()),
                ('warranty_months', models.IntegerField()),
                ('depreciate', models.BooleanField()),
                ('supplier_id', models.IntegerField()),
                ('last_checkout', models.DateTimeField()),
                ('expected_checkin', models.DateField()),
                ('assigned_type', models.CharField(max_length=191)),
                ('last_audit_date', models.DateTimeField()),
                ('next_audit_date', models.DateField()),
                ('byod', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company')),
            ],
            options={
                'db_table': 'device',
            },
        ),
    ]
