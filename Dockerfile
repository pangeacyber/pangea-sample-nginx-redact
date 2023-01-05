FROM openresty/openresty:1.21.4.1-0-jammy
EXPOSE 8080

RUN opm get ledgetech/lua-resty-http
RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/ /etc/nginx/conf.d
