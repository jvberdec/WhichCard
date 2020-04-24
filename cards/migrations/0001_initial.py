from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardName', models.CharField(max_length=200)),
                ('bankName', models.CharField(max_length=200)),
                ('annualFee', models.IntegerField()),
                ('rewardsType', models.CharField(max_length=200)),
                ('rewardValue', models.DecimalField(decimal_places=5, max_digits=10)),
                ('rewardsDisplay', models.TextField()),
                ('groceryMultiplier', models.DecimalField(decimal_places=5, max_digits=10)),
                ('restMultiplier', models.DecimalField(decimal_places=5, max_digits=10)),
                ('travelMultiplier', models.DecimalField(decimal_places=5, max_digits=10)),
                ('gasMultiplier', models.DecimalField(decimal_places=5, max_digits=10)),
                ('elseMultiplier', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('APR', models.DecimalField(decimal_places=5, default=1, max_digits=10)),
                ('bonusDisplay', models.TextField(blank=True, null=True)),
                ('bonusValue', models.IntegerField(default=1)),
                ('link', models.TextField()),
                ('creditScore', models.CharField(max_length=200)),

                ('bonusMinimumSpend', models.IntegerField()),
                ('bonusSpendMonths', models.IntegerField()),

            ],
        ),
    ]