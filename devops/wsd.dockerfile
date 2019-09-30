#FROM python:3.7-alpine
FROM python:3.7-slim

# RUN apk add --update \
#     curl \
#     bash \
#     && rm -rf /var/cache/apk/*

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/wsd
WORKDIR /opt/wsd

COPY src/ /opt/wsd

RUN curl -L -O "https://github.com/joewalnes/websocketd/releases/download/v0.3.0/websocketd-0.3.0-linux_amd64.zip"
RUN unzip websocketd-0.3.0-linux_amd64.zip
RUN chmod +x websocketd
RUN cp websocketd /usr/local/bin/websocketd
RUN chmod +x run.sh

RUN echo 'root:x:0:0:root:/root:/bin/bash\n' >> /etc/passwd


ENV PATH="/opt/wsd:${PATH}"

RUN ls -la 

#ENTRYPOINT [ "websocketd", "--port=80", "sh", "run.sh" ]

#CMD tail -f /dev/null

ENTRYPOINT [ "sh","run.sh" ]