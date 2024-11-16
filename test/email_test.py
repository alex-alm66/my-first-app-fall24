# this is the "test/email_test.py" file...

from app.email_service import send_email_with_sendgrid

def test_send_email_with_sendgrid():
    assert send_email_with_sendgrid() == 202