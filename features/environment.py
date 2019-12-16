import os
import tempfile
from behave import fixture, use_fixture
# app is the sample application we want to test
from app import app

@fixture
def app_client(context, *args, **kwargs):
    app.testing = True
    context.client = app.test_client()
    

def before_feature(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(app_client, context)