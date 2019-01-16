echo "start-gunicorn-server"
nohup gunicorn -c setup.py stockoverview.wsgi:application  > log/spider_output.log 2>&1 &
echo "gunicorn start!"