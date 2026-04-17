FROM kong/httpbin:latest

# Add prefix middleware for subpath deployments (HTTPBIN_PREFIX env var)
# and custom /files endpoints
COPY prefix.py /httpbin/

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:80", "prefix:app", "-k", "gevent"]
