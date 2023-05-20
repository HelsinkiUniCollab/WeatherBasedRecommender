
FROM node:18-alpine 

WORKDIR /usr/src/app

COPY . .

RUN npm ci

RUN npm run build

ENV NODE_ENV production

EXPOSE 3000

CMD [ "npx", "serve", "build" ]
