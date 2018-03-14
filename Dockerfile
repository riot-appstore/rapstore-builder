FROM python:3.5

# Setup rapstore-builder
COPY .    /code/builder
WORKDIR   /code/builder
RUN python3 setup.py install

# Hardwritten configuration
ENV LOGDIR  /vol/log/
ENV PORT    8000

# Chmod LOGDIR for www-data
# Inspired by
# https://github.com/docker-library/postgres/blob/0aaaf209/10/Dockerfile#L125
RUN mkdir -p "$LOGDIR" \
    && chown -R www-data:www-data "$LOGDIR" \
    && chmod 755 "$LOGDIR"

# Exposed volumes/ports
VOLUME  $LOGDIR
EXPOSE  $PORT

# Use 'exec' to have PID 1
USER www-data
CMD exec rapstore-builder localhost ${PORT} --logdir ${LOGDIR}
