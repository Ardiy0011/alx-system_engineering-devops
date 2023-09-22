exec { 'killmenow':
  command     => 'pkill -f "killmenow"',
  path        => '/usr/bin:/bin', # Specify the path to pkill
  refreshonly => true,            # Only run when explicitly refreshed
}
