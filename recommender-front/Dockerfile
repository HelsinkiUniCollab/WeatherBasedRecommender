
FROM node:18 

WORKDIR /usr/src/app

COPY . .

RUN npm install

RUN npm run build

ENV NODE_ENV production

EXPOSE 3000

CMD [ "npx", "serve", "build" ]
