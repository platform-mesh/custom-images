FROM kong/httpbin:0.2.3

USER root

# Add /files endpoints
ADD store.py /httpbin/httpbin
RUN echo 'from .store import *' >> /httpbin/httpbin/__init__.py

USER httpbin
