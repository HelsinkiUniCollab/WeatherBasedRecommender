FROM node:alpine

WORKDIR '/app'

COPY package*.json ./

RUN npm install --only=production

COPY ./build ./build

CMD ["npm","start"]
