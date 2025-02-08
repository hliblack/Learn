#提前把证书文件放入到"/etc/certs/"目录下

docker run --restart always \
  --name derper -p 443:12345 -p 3478:3478/udp \
  -v /data/certs/:/app/certs \
  -e DERP_CERT_MODE=manual \
  -e DERP_ADDR=:443 \
  -e DERP_DOMAIN=dert.hyouka.top \
  -d ghcr.io/yangchuansheng/derper:latest
