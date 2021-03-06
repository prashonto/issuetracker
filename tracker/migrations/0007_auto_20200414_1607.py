# Generated by Django 3.0.5 on 2020-04-14 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20200414_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fab', models.CharField(max_length=200, null=True)),
                ('Esc_Level', models.IntegerField(null=True)),
                ('Issue_description', models.CharField(max_length=500, null=True)),
                ('POA', models.CharField(max_length=500, null=True)),
                ('Resolution', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateField(null=True)),
                ('date_closed', models.DateField(null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Pending', 'Pending'), ('Closed', 'Closed')], max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Fab',
        ),
        migrations.DeleteModel(
            name='Issues',
        ),
        migrations.AddField(
            model_name='issue',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.Customer'),
        ),
        migrations.AddField(
            model_name='issue',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.Product'),
        ),
    ]
