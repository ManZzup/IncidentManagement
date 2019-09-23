# Generated by Django 2.2.1 on 2019-09-21 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20190911_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='code',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='dsdivision',
            name='code',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='policestation',
            name='code',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='policestation',
            name='division',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='policestation',
            name='sn_division',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='policestation',
            name='tm_division',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pollingstation',
            name='code',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='code',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='division',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='GNDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=36, null=True)),
                ('name', models.CharField(max_length=200)),
                ('sn_name', models.CharField(blank=True, max_length=200, null=True)),
                ('tm_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.District')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]