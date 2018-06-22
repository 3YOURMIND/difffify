FROM node:8.9.3
COPY ./difffify /code/difffify
WORKDIR /code/difffify
RUN npm install

FROM nginx:1.13.9-alpine
COPY --from=0 /code /var/www/difffify
RUN apk update \
 && apk add bash \
 && apk add py-pip \
 && apk add nodejs \
 && pip install j2cli

COPY bin/run.sh /bin/run.sh
COPY nginx.conf.j2 /var/www/difffify/nginx.conf.j2
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log


WORKDIR /var/www/difffify

CMD ["/bin/run.sh"]

