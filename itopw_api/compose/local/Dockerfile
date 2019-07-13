FROM php:7.2-fpm

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    zip \
    jpegoptim optipng pngquant gifsicle \
    vim \
    unzip \
    git \
    curl

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install extensions
RUN docker-php-ext-install pdo_mysql mbstring zip exif pcntl
RUN docker-php-ext-configure gd --with-gd  --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/
RUN docker-php-ext-install gd

RUN apt-get update
RUN curl -s https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
COPY . /app
WORKDIR /app
RUN chmod 775 -R storage 
RUN chown -R $USER:www-data storage 
RUN chmod 775 -R bootstrap/cache 
RUN chown -R $USER:www-data bootstrap/cache
EXPOSE 9000
CMD bash -c "composer install; php artisan route:clear; php artisan config:clear; php artisan cache:clear; php artisan key:generate; php-fpm"
