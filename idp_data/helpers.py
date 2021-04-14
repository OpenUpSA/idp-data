import os
from idp_data.idp_data.models import Event, Municipality
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def EmailEventSubmission(event_submission):
    event = Event.objects.get(pk=event_submission['event'].value)

    if (email_address := event.muni.event_submission_email_address):
        message = Mail(
            from_email='paul@openup.org.za',
            to_emails=email_address,
            subject=f'A new event submission for; {event.title}',
            html_content=f"""Hello,<br>
            <br>
            A new submission was submitted for;<br>
            {event.title}<br>
            <br>
            by;<br>
            {event_submission['submitter_name'].value} ({event_submission['submitter_contact'].value})<br>
            <br>
            Their comment is;<br>
            {event_submission['submission'].value}<br>
            -------------<br>
            <br>
            Their issue is;<br>
            {event_submission['submission_issue'].value}<br>
            <br>
            Their town is;<br>
            {event_submission['submitter_town'].value}<br>
            <br>
            regards,<br>
            OpenUp
            """)
        try:
            sg=SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response=sg.send(message)
        except Exception as e:
            print(e.message)

    return True
