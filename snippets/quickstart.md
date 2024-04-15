Before starting, we advise updating the `apt` repositories and installing `curl` download utility to fetch the package. If you want to fetch the package manually, follow this guide instead: [Manual Installation](#).
```{.bash data-prompt="$"}
$ sudo apt update
$ sudo apt install curl
```

Once everything is updated and ready, you can follow the below tasks to install:
{.power-number}

1. The first step is downloading the `percona-release` repository package:
	```{.bash data-prompt="$"}
	$ curl -O https://repo.percona.com/apt/percona-release_latest.generic_all.deb
	```

2. Install the downloaded package with `apt` as root or with `sudo`, and then refresh the local cache to update the package information:
	```{.bash data-prompt="$"}
	$ sudo apt install gnupg2 lsb-release ./percona-release_latest.generic_all.deb
	$ sudo apt update
	```

3. Use `percona-release` to set up the repository for the Percona Server for MySQL 8.0 version:
	```{.bash data-prompt="$"}
	$ sudo percona-release setup ps80
	```
	You can check the repository setup for the Percona original release list in `/etc/apt/sources.list.d/percona-original-release.list`.

4. Install the server package with the `percona-release` command:
	```{.bash data-prompt="$"}
	$ sudo apt install percona-server-server
	```
	For more information on `percona-release` command see [Configuring Percona Repositories](https://docs.percona.com/percona-software-repositories/percona-release.html).

5. It should now be installed! Percona Server runs automatically after installation. To control the service, learn how to [Stop/Run Percona Server](#).