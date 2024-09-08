# A puppet code that fix a word press site of 5xx error to 200k

exec { 'fix-wordpess-server-error':
   command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path  => '/usr/bin/:/bin/',
}
