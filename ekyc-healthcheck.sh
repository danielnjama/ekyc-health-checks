#!/bin/bash

# Define the endpoint
endpoint="http://127.0.0.1:8000/api/health/"

#Define auth token
auth_token='c1aa2586be8c036d37c5171fddc49f865f2d67f7'

# Define the mount point
mount_point="/dev/nvme0n1p2"


# Get the node_name
node_name=$(hostname)

# Declare an associative array to store service statuses
declare -A services

# List of services to check
services_list=(
    "haproxy"
    "hazelcast"
    "rabbitmq-server"
    "httpd"
    "centralized-configuration-server"
    "backoffice-ekyc-service"
    "tomcat"
    "ekyc-consumer-service"
    "ekyc-repository"
    "ekyc-facade"
    "g2-gateway"
    "g2-gateway-sync"
    "g2-result-handler"
    "identity-repository"
    "identity-service"
    "sms-channel"
)

# Check the status of each service and store it in the associative array
for service in "${services_list[@]}"; do
    if systemctl list-units --full -all | grep -Fq "$service.service"; then
        status=$(systemctl is-active "$service")
    else
        status="none"
    fi
    services["$service"]=$status
done

# Get disk usage for the specified mount point
# disk_usage=$(df -h | grep "$mount_point" | awk '{print $5}')
disk_usage=60

# Prepare JSON payload
json_payload=$(jq -n \
                  --arg node_name "$node_name" \
                  --arg haproxy "${services[haproxy]}" \
                  --arg hazelcast "${services[hazelcast]}" \
                  --arg rabbitmq_server "${services[rabbitmq-server]}" \
                  --arg httpd "${services[httpd]}" \
                  --arg centralized_configuration_server "${services[centralized-configuration-server]}" \
                  --arg backoffice_ekyc_service "${services[backoffice-ekyc-service]}" \
                  --arg tomcat "${services[tomcat]}" \
                  --arg ekyc_consumer_service "${services[ekyc-consumer-service]}" \
                  --arg ekyc_repository "${services[ekyc-repository]}" \
                  --arg ekyc_facade "${services[ekyc-facade]}" \
                  --arg g2_gateway "${services[g2-gateway]}" \
                  --arg g2_gateway_sync "${services[g2-gateway-sync]}" \
                  --arg g2_result_handler "${services[g2-result-handler]}" \
                  --arg identity_repository "${services[identity-repository]}" \
                  --arg identity_service "${services[identity-service]}" \
                  --arg sms_channel "${services[sms-channel]}" \
                  --arg free_space "$disk_usage" \
                  '{
                    "node_name": $node_name,
                    "haproxy": $haproxy,
                    "hazelcast": $hazelcast,
                    "rabbitmq_server": $rabbitmq_server,
                    "httpd": $httpd,
                    "centralized_configuration_server": $centralized_configuration_server,
                    "backoffice_ekyc_service": $backoffice_ekyc_service,
                    "tomcat": $tomcat,
                    "ekyc_consumer_service": $ekyc_consumer_service,
                    "ekyc_repository": $ekyc_repository,
                    "ekyc_facade": $ekyc_facade,
                    "g2_gateway": $g2_gateway,
                    "g2_gateway_sync": $g2_gateway_sync,
                    "g2_result_handler": $g2_result_handler,
                    "identity_repository": $identity_repository,
                    "identity_service": $identity_service,
                    "sms_channel": $sms_channel,
                    "free_space": $free_space
                  }')

# Send the JSON payload to the API endpoint
curl -X POST -H "Content-Type: application/json" -d "$json_payload" "$endpoint" -H "Authorization: Token $auth_token"
