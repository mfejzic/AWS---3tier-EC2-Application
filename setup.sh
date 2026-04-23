#!/bin/bash
set -e

# Update system
dnf update -y

# Install packages
dnf install -y \
  python3 \
  python3-pip \
  nginx \
  git

# Enable services
systemctl enable nginx

# Create app directory
mkdir -p /opt/app
