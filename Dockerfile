FROM alpine:latest
RUN apk add --no-cache bash
RUN apk add vim
COPY ./contacts_DB.sh /contacts_DB.sh
COPY ./database.txt /database.txt
RUN chmod +x /contacts_DB.sh
CMD ["bash", "/contacts_DB.sh"]
