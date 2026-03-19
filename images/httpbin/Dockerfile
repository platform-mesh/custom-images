FROM kong/httpbin:latest
USER root

# Modified from upstream
COPY third_party/ /httpbin/httpbin

# Add /files endpoints
ADD store.py /httpbin/httpbin
RUN echo 'from .store import *' >> /httpbin/httpbin/__init__.py
USER 1001
