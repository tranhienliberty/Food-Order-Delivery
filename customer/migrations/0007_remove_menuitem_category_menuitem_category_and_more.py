# Generated by Django 4.0.3 on 2022-06-21 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_remove_menuitem_category_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.category'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='ward',
            field=models.CharField(max_length=50, null=True),
        ),
    ]