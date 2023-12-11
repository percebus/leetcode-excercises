FROM nikolaik/python-nodejs:python3.10-nodejs16 as base

FROM base as dev
WORKDIR /project
COPY . .
RUN ls -la
RUN npm run setup:ci && npm ci
RUN npm test

FROM base as release
WORKDIR /project
COPY . .
RUN ls -la
RUN npm run pip:install:prd
