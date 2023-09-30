import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-opnsynid-stock-reporting",
    description="Meta package for open-synergy-opnsynid-stock-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-stock_card_report_value',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
