FROM node:lts

RUN apt-get update

# for react frontend
EXPOSE 3000
EXPOSE 5000

# set working directory
ADD . /app
WORKDIR /app

COPY package.json /app
RUN npm install
COPY . /app

# This is the runtime command for the container
CMD yarn start
