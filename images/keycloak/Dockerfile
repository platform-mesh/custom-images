FROM quay.io/keycloak/keycloak:26.8.2@sha256:c68e286cacd87b942ac1939a0a1481461109d6acd3a57dc496969a319a76bbf0 AS builder

ENV KC_DB=postgres
ENV KC_HTTP_RELATIVE_PATH=/keycloak
ENV KC_PROXY_HEADERS=xforwarded
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:26.8.2@sha256:c68e286cacd87b942ac1939a0a1481461109d6acd3a57dc496969a319a76bbf0

COPY --from=builder /opt/keycloak/ /opt/keycloak/

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
