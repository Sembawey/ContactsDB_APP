FROM alpine:latest
RUN apk add --no-cache bash
RUN apk add vim
RUN touch /database.txt
COPY ./contacts_DB.sh /contacts_DB.sh
RUN chmod +x /contacts_DB.sh
CMD ["bash", "/contacts_DB.sh"]
