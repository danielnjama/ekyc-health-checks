from django.contrib import admin
from .models import ServiceHealthData


class ServiceHealthDataAdmin(admin.ModelAdmin):
    list_display = [
        'node_name', 'date', 'haproxy', 'hazelcast', 'rabbitmq_server', 'httpd',
        'centralized_configuration_server', 'backoffice_ekyc_service', 'tomcat',
        'ekyc_consumer_service', 'ekyc_repository', 'ekyc_facade', 'g2_gateway',
        'g2_gateway_sync', 'g2_result_handler', 'identity_repository', 'identity_service',
        'sms_channel', 'free_space'
    ]
    list_filter = ['date', 'node_name']
    search_fields = ['node_name']
    
    
admin.site.register(ServiceHealthData,ServiceHealthDataAdmin)
