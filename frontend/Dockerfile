FROM mhart/alpine-node:11 AS builder

EXPOSE 3000
EXPOSE 5000

WORKDIR /app
COPY . .
RUN yarn run build

FROM mhart/alpine-node
RUN yarn global add serve
WORKDIR /app
COPY --from=builder /app/build .
CMD ["serve", "-p", "3000", "-s", "."]

