FROM node:16-alpine as build-step
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json package-lock.json ./
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
RUN python seed.py
ENV FLASK_ENV production

EXPOSE 3000
WORKDIR /app/api
CMD ["gunicorn", "-b", ":3000", "api:app"]