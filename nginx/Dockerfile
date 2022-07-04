FROM nginx:1.23.0

EXPOSE 80
EXPOSE 443

ENV TZ=America/Sao_Paulo

COPY src/nginx.conf /etc/nginx/nginx.conf
COPY src/hosts.conf /etc/nginx/conf.d
COPY src/security_headers /etc/nginx/security_headers

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /app
WORKDIR /app

COPY src /app
