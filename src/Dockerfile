# Stage 1: builder.
FROM python:3.12-slim-bullseye as builder

# Copy local context to `/app` inside container (see .dockerignore).
WORKDIR /app
COPY . .

# Create virtualenv which will be copied into final container.
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

RUN apt-get update && apt-get install -y unzip curl

# Install app requirements and reflex inside virtualenv.
RUN pip install -r requirements.txt

# Deploy templates and prepare app.
RUN reflex init

# Export static copy of frontend to /app/.web/_static.
# .env export is required to get correct values for static files.
RUN export $(cat .env | grep -v ^# | xargs) && reflex export --frontend-only --no-zip

# Copy static files out of /app to save space in backend image.
RUN mv .web/_static /tmp/_static
RUN rm -rf .web && mkdir .web
RUN mv /tmp/_static .web/_static

# Stage 2: copy artifacts into nginx image.
FROM nginx:alpine as frontend
# Set working directory to nginx public folder.
WORKDIR /usr/share/nginx/html
# Copy static files from builder stage.
COPY --from=builder /app/.web/_static /usr/share/nginx/html
