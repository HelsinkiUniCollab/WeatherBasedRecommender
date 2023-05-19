
FROM node:18 

WORKDIR /usr/src/app

COPY --chown=node:node . .

RUN npm install --package-lock-only

RUN npm ci

RUN npm run build

ENV NODE_ENV production

EXPOSE 3000

CMD [ "npx", "serve", "build" ]
