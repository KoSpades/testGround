# Dockerfile, Image, Container
FROM python:3.9

# Add [source: which python file would you like to add] [destination: . just means the base folder]
ADD dockertest.py .

# RUN: an image build-step, the state of the container after RUN will be commited to container image.
# We can use this step to install libraries
RUN pip install requests beautifulsoup4

# CMD: used to set a default command that gets executed once you run the Docker Container.
CMD ["python", "./dockertest.py"]
