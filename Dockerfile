FROM heroku/miniconda

# Grab requirements.txt
ADD ./app/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD ./app /opt/app/
WORKDIR /opt/app

# Install scientific dependencies
RUN conda install scikit-learn

# Start app
CMD gunicorn --bind 0.0.0.0:$PORT wsgi