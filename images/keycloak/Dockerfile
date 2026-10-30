FROM quay.io/keycloak/keycloak:26.8.1@sha256:a78d6b79572168cb25886b80a8b5b8d4ed4390743e3eecb810538683e209dd6b AS builder

ENV KC_DB=postgres
ENV KC_HTTP_RELATIVE_PATH=/keycloak
ENV KC_PROXY_HEADERS=xforwarded
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:26.8.1@sha256:a78d6b79572168cb25886b80a8b5b8d4ed4390743e3eecb810538683e209dd6b

COPY --from=builder /opt/keycloak/ /opt/keycloak/

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
