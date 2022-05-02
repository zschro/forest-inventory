FROM node:16-alpine as build-step
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY forest-inventory-react/package.json forest-inventory-react/package-lock.json ./
COPY forest-inventory-react/src ./src
COPY forest-inventory-react/public ./public
RUN npm install
RUN npm run build

FROM python:3.9
WORKDIR /app
COPY --from=build-step /app/build ./build

RUN mkdir ./api
COPY forest-inventory-flask/requirements.txt forest-inventory-flask/*.py forest-inventory-flask/.flaskenv ./api/
RUN pip install -r ./api/requirements.txt
ENV FLASK_ENV production

EXPOSE 8003
WORKDIR /app/api
CMD ["gunicorn", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8003", "base:api"] 