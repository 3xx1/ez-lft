# Use an official Python runtime as a parent image
FROM python:2.7-slim
RUN apt-get update -y
RUN apt-get install -yq make cmake gcc g++ unzip wget build-essential gcc zlib1g-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# OpenCV
RUN wget https://github.com/opencv/opencv/archive/2.4.13.3.zip \
&& unzip 2.4.13.3.zip \
&& mkdir /opencv-2.4.13.3/cmake_binary \
&& cd /opencv-2.4.13.3/cmake_binary \
&& cmake -DWITH_QT=OFF \
        -DWITH_OPENGL=ON \
        -DFORCE_VTK=OFF \
        -DWITH_TBB=ON \
        -DWITH_GDAL=ON \
        -DWITH_XINE=ON \
        -DBUILD_EXAMPLES=OFF \
        -DENABLE_PRECOMPILED_HEADERS=OFF .. \
&& make install \
&& rm /2.4.13.3.zip \
&& rm -r /opencv-2.4.13.3

# Set the working directory to /ez-lft
WORKDIR /ez-lft

# Copy the current directory contents into the container at /ez-lft
COPY . /ez-lft

# Install Opencv
RUN apt-get install python-opencv -y

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python"]
