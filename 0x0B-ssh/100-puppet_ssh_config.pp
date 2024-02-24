# SSH configuration of client file
exec { 'Customize SSH settings':
  command => 'bash -c "echo PasswordAuthentication no >> /etc/ssh/ssh_config && echo IdentityFile \'~/.ssh/school\' >> /etc/ssh/ssh_config && echo PubkeyAuthentication yes >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}

