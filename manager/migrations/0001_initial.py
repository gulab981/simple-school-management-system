# Generated by Django 3.2.25 on 2024-08-23 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('Worker', 'Worker'), ('Chef', 'Chef'), ('Security', 'Security'), ('Cleaner', 'Cleaner')], max_length=20)),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_number', models.CharField(max_length=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=10)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('students', models.ManyToManyField(blank=True, to='manager.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.teacher')),
            ],
        ),
    ]
