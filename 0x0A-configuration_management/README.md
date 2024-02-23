# Configuration management
This is a system devops project that handles tasks using an auto-remediation too called Skynet.

## Requirements
The following requirements must be implemented in the project.
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp

## Note on Versioning
**Install puppet**  
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

**Install puppet-lint**  
$ gem install puppet-lint
