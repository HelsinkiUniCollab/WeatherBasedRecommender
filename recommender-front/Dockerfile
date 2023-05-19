FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm ci --only=production

COPY . .

RUN npm run build 

RUN npm install -g serve

CMD ["serve", "-s", "-l", "tcp://0.0.0.0:5000", "build"]
