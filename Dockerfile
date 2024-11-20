# Use a lightweight Python 3.9 image as the base
FROM python:3.9-slim

# Update system and install Chrome dependencies
RUN apt update && apt install -y \
    sudo \
    curl \
    wget \
    gnupg \
    --no-install-recommends && \
    \
    # Add Google's signing key and Chrome repository
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    \
    # Update and install Google Chrome
    apt update && apt install -y google-chrome-stable && \
    \
    # Clean up
    apt clean && rm -rf /var/lib/apt/lists/*

# Create a Jenkins user
RUN useradd -ms /bin/bash jenkins && \
    echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to the Jenkins user
USER jenkins

# Set the working directory
WORKDIR /home/jenkins
