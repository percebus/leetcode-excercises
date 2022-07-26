FROM nikolaik/python-nodejs:python3.10-nodejs16

WORKDIR /project
COPY . .
RUN ls -la
RUN npm run setup:ci && npm ci
RUN npm test
