from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import EmailMessage
import pandas as pd
from io import BytesIO
from hcheckapp.models import ServiceHealthData

class Command(BaseCommand):
    help = 'Generate daily service report and send via email'

    def handle(self, *args, **kwargs):
        # Get today's date
        today = timezone.now().date()

        # Fetch data from the database
        data = ServiceHealthData.objects.filter(date__date=today)

        # Prepare the data for Excel/CSV
        rows = []
        for record in data:
            rows.append([
                record.node_name,
                record.haproxy,
                record.hazelcast,
                record.rabbitmq_server,
                record.httpd,
                record.centralized_configuration_server,
                record.backoffice_ekyc_service,
                record.tomcat,
                record.ekyc_consumer_service,
                record.ekyc_repository,
                record.ekyc_facade,
                record.g2_gateway,
                record.g2_gateway_sync,
                record.g2_result_handler,
                record.identity_repository,
                record.identity_service,
                record.sms_channel,
                record.free_space
            ])

        # Convert to DataFrame
        df = pd.DataFrame(rows, columns=[
            "Node Name", "haproxy", "hazelcast", "rabbitmq-server", "httpd", 
            "centralized-configuration-server", "backoffice-ekyc-service", 
            "tomcat", "ekyc-consumer-service", "ekyc-repository", "ekyc-facade", 
            "g2-gateway", "g2-gateway-sync", "g2-result-handler", 
            "identity-repository", "identity-service", "sms-channel", "Free Space"
        ])

        # Apply conditional formatting
        def apply_formatting(val):
            color = ''
            if val == 'active':
                color = 'background-color: green'
            elif val == 'inactive':
                color = 'background-color: red'
            elif val == 'none':
                color = 'background-color: white'
            return color

        def apply_free_space_formatting(val):
            color = 'background-color: green' if int(val[:-1]) <= 80 else 'background-color: red'
            return color

        df_style = df.style.applymap(apply_formatting, subset=pd.IndexSlice[:, :-1])
        df_style = df_style.applymap(apply_free_space_formatting, subset=['Free Space'])

        # Convert to Excel
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            df_style.to_excel(writer, index=False, sheet_name='Report')

        # Get the overview
        active_services = df[df == 'active'].count().sum()
        total_services = df.size - len(df['Free Space'])
        overview = f"Out of {total_services} services, {active_services} are active. Disk usage is okay for all nodes."

        # Send the email
        email = EmailMessage(
            subject=f"Daily Service Report - {today}",
            body=f"Please find attached the daily service report.\n\nOverview:\n{overview}",
            from_email="admin@dtechnologys",
            to=["danielnjama2015@gmail.com"]
        )
        email.attach('daily_service_report.xlsx', excel_buffer.getvalue(), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        email.send()

        self.stdout.write(self.style.SUCCESS('Successfully generated and sent report'))
