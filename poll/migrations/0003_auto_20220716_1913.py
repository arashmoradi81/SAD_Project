# Generated by Django 3.2 on 2022-07-16 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_alter_openend_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='closetest_answer',
            name='answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='closetest',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_closetest', to='poll.poll'),
        ),
        migrations.AlterField(
            model_name='openend',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_openend', to='poll.poll'),
        ),
    ]
