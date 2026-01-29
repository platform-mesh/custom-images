FROM kennethreitz/httpbin:latest

# Modified from upstream
COPY third_party/ /usr/local/lib/python3.6/dist-packages/httpbin

# Add /files endpoints
ADD store.py /usr/local/lib/python3.6/dist-packages/httpbin
RUN echo 'from .store import *' >> /usr/local/lib/python3.6/dist-packages/httpbin/__init__.py
