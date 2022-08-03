FROM python:3.8

RUN \
    pip install --upgrade --force-reinstall Boto3 && \
    pip install --upgrade --force-reinstall jwt && \
    pip install --upgrade --force-reinstall pyjwt && \
    pip install pytest

