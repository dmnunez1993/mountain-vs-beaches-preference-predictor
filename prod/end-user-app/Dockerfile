FROM node:18.16-alpine as build

RUN mkdir /end-user-app

COPY ./end-user-app/package.json /end-user-app/package.json
COPY ./end-user-app/yarn.lock /end-user-app/yarn.lock

WORKDIR /end-user-app

RUN yarn install

COPY ./end-user-app/. /end-user-app/

RUN yarn build

# production environment
FROM nginx:1.21.1-alpine
COPY --from=build /end-user-app/build /usr/share/nginx/html
COPY ./prod/end-user-app/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./end-user-app/setup_env_config.sh /setup_env_config.sh

COPY ./prod/end-user-app/entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["nginx", "-g", "daemon off;"]
