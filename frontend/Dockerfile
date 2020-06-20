FROM node:lts

RUN apt-get update

# for react frontend
EXPOSE 3000
EXPOSE 5000

WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn
COPY . ./
RUN yarn build