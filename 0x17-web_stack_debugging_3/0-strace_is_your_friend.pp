# A puppet code that fix a word press site of 5xx error 

exec { 'fix-word press':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
