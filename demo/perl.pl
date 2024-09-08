# 1. Example
use strict;
use warnings;
use IO::Handle;

my ( $remaining, $total );

$remaining = $total = shift(@ARGV);

STDOUT->autoflush(1);

while ( $remaining ) {
  printf ( "Remaining %s/%s \r", $remaining--, $total );
  sleep 1;
}

print "\n";