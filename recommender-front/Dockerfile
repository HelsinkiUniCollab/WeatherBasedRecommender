FROM node:18 

WORKDIR /usr/src/app

COPY . .

RUN npm ci --only=production --legacy-peer-deps

RUN npm run build

RUN npm install -g serve

CMD ["serve", "-s", "-l", "tcp://0.0.0.0:3000", "build"]
