FROM postgres 
ENV POSTGRES_PASSWORD ck-admin 
ENV POSTGRES_DB musicboxd 
COPY init.sql /docker-entrypoint-initdb.d/