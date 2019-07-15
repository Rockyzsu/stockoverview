echo "start-gunicorn-server"
nohup gunicorn -c setup.py stockoverview.wsgi:application  > log/gunicorn.log 2>&1 &
echo "gunicorn start!"