file { '/tmp/school':
  ensure  => 'file',        # Ensure that it's a file (not a directory)
  mode    => '0744',        # File permissions
  owner   => 'www-data',    # Owner
  group   => 'www-data',    # Group
  content => 'I love Puppet',  # Content of the file
}
