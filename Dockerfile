###########
# Warm Up #
###########
# Use Debian:Stretch as a parent runtime image
FROM debian:stretch

# Update Linux Dependencies
RUN apt-get update -y

# Linux Dependencies
RUN apt-get install -yq make cmake gcc g++ unzip wget build-essential gcc zlib1g-dev tk-dev libgtk2.0-dev pkg-config curl sudo

###########
# Node.js #
###########
# Installing node.js version 10.x
RUN curl --silent --location https://deb.nodesource.com/setup_10.x | sudo bash -
RUN apt-get install -y nodejs


##########
# Python #
##########
# Python Installation
RUN apt-get dist-upgrade
RUN apt-get install -yq python2.7 python-pip

# Python Dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# OpenCV Compilation to Install
RUN wget https://github.com/opencv/opencv/archive/3.4.3.zip \
&& unzip 3.4.3.zip \
&& mkdir /opencv-3.4.3/cmake_binary \
&& cd /opencv-3.4.3/cmake_binary \
&& cmake -DWITH_QT=OFF \
        -DWITH_OPENGL=ON \
        -DFORCE_VTK=OFF \
        -DWITH_TBB=ON \
        -DWITH_GDAL=ON \
        -DWITH_XINE=ON \
        -DBUILD_EXAMPLES=OFF \
        -DENABLE_PRECOMPILED_HEADERS=OFF .. \
&& make install \
&& rm /3.4.3.zip \
&& rm -r /opencv-3.4.3

# Install Opencv Python Package
RUN apt-get install python-opencv -y

################
# Finish Touch #
################
# Set the working directory to /ez-lft
WORKDIR /ez-lft

# Copy the current directory contents into the container at /ez-lft
COPY . /ez-lft

# Make port 80 and 3000 available to the world outside this container
EXPOSE 80
EXPOSE 3000

# Run app.py when the container launches
# CMD ["python"]
