FROM node:8.11.0 as builder
WORKDIR /code/difffify
COPY ./app/package.json /code/difffify/
RUN npm install

COPY ./app /code/difffify
RUN npm run build

FROM nginx:1.13.9-alpine
COPY --from=0 /code/difffify/dist /var/www/difffify/dist
COPY --from=0 /code/difffify/index.html /var/www/difffify/
RUN apk update \
 && apk add bash \
 && apk add py-pip \
 && apk add nodejs \
 && pip install j2cli

COPY run.sh /bin/run.sh
COPY nginx.conf.j2 /var/www/difffify/nginx.conf.j2
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /var/www/difffify

CMD ["/bin/run.sh"]

