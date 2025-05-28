import os
import click
from app import app
from seed.seed_script import seed_database
from seed.seed_data import seed_data

@app.cli.group()
def translate():
    """Translation and Localization commands"""
    pass

@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')

@translate.command()
def compile():
    """Compile all Languages"""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')
    
@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel init -i messages.pot -d app/translations -l' + lang):
        raise RuntimeError('Init command failed')
    os.remove('messages.pot')

@app.cli.group()
def seed():
    """Commands for filling the database with test data."""
    pass

@seed.command()
def run():
    """Run the script for filling the database with test data."""
    try:
        seed_database(seed_data, drop=False)
    except Exception as e:
        raise RuntimeError('Error create new data')

@seed.command()
def clear_run():
    """Run the script for filling the database with test data."""
    try:
        seed_database(seed_data, drop=True)
    except Exception as e:
        raise RuntimeError('Error create new data')
