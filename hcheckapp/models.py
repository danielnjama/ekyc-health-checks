from django.db import models

class ServiceHealthData(models.Model):
    node_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    haproxy = models.CharField(max_length=10)
    hazelcast = models.CharField(max_length=10)
    rabbitmq_server = models.CharField(max_length=10)
    httpd = models.CharField(max_length=10)
    centralized_configuration_server = models.CharField(max_length=10)
    backoffice_ekyc_service = models.CharField(max_length=10)
    tomcat = models.CharField(max_length=10)
    ekyc_consumer_service = models.CharField(max_length=10)
    ekyc_repository = models.CharField(max_length=10)
    ekyc_facade = models.CharField(max_length=10)
    g2_gateway = models.CharField(max_length=10)
    g2_gateway_sync = models.CharField(max_length=10)
    g2_result_handler = models.CharField(max_length=10)
    identity_repository = models.CharField(max_length=10)
    identity_service = models.CharField(max_length=10)
    sms_channel = models.CharField(max_length=10)
    free_space = models.CharField(max_length=10)

    def __str__(self):
        return self.node_name
