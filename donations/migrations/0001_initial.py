# Generated by Django 3.0.8 on 2020-08-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(choices=[('A', 'A'), ('A+', 'A+'), ('A-', 'A-'), ('AB', 'AB'), ('B', 'B'), ('B+', 'B+'), ('B-', 'B-'), ('O', 'O'), ('O+', 'O+'), ('O-', 'O-')], max_length=5, verbose_name='blood type')),
                ('amount', models.PositiveIntegerField(verbose_name='amount')),
                ('height', models.FloatField(verbose_name='height')),
                ('weight', models.FloatField(verbose_name='weight')),
                ('last_donate_date', models.DateField(blank=True, null=True, verbose_name='last donate date')),
                ('has_hiv', models.BooleanField(blank=True, null=True, verbose_name='do you have hiv')),
                ('take_drugs', models.BooleanField(blank=True, null=True, verbose_name='do you use drugs')),
                ('has_diabetes', models.BooleanField(blank=True, null=True, verbose_name='do you use diabetes')),
                ('has_tattoo', models.BooleanField(blank=True, null=True, verbose_name='had a tattoo')),
                ('been_injured', models.BooleanField(blank=True, null=True, verbose_name='been injured with a used neddle')),
                ('blood_transfusion', models.BooleanField(blank=True, null=True, verbose_name='had a blood transfusion')),
                ('been_in_prison', models.BooleanField(blank=True, null=True, verbose_name='been imprisoned in a prison')),
                ('feedback', models.TextField(blank=True, null=True, verbose_name='feedback')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'blood',
                'verbose_name_plural': 'bloods',
            },
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organ', models.CharField(choices=[('HEART', 'HEART'), ('KIDENY', 'KIDENY'), ('LIVER', 'LIVER'), ('LUNG', 'LUNG'), ('PANCREAS', 'PANCREAS'), ('INTESTINES', 'INTESTINES')], max_length=200, verbose_name='organ')),
                ('allergies', models.BooleanField(blank=True, null=True, verbose_name='allergies')),
                ('medications', models.BooleanField(blank=True, null=True, verbose_name='medications')),
                ('has_disease', models.BooleanField(blank=True, null=True, verbose_name='do you have a disease')),
                ('has_asthma', models.BooleanField(blank=True, null=True, verbose_name='do you have a asthma')),
                ('has_diabetes', models.BooleanField(blank=True, null=True, verbose_name='do you use diabetes')),
                ('has_hypertension', models.BooleanField(blank=True, null=True, verbose_name='do you have a hypertension')),
                ('has_tuberculosis', models.BooleanField(blank=True, null=True, verbose_name='do you have a tuberculosis')),
                ('organ_date_registration', models.DateField(blank=True, null=True, verbose_name='organ date registration')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'organ',
                'verbose_name_plural': 'organs',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(choices=[('COVID-19', 'COVID-19'), ('MAKEDONIA', 'MAKEDONIA'), ('SELE ENAT CHARITABLE', 'SELE ENAT CHARITABLE')], max_length=300, verbose_name='blood type')),
                ('amount', models.PositiveIntegerField(verbose_name='amount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
            },
        ),
    ]
