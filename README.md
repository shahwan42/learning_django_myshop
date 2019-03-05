# My Shop

to make it work:
- fill in .env vars

0. make sure you have weasyprint dependencies installed and other stuff
1. run rabbitmq-server
2. run $celery -A myshop worker -l info
3. run $celery -A myshop flower # view at localhost:5555
4. run dev server
5. autossh for tunneling server to serveo.net
