Install mysql version 5.7.* on both servers.

Link: https://computingforgeeks.com/how-to-install-mysql-on-ubuntu-focal/#comments

The `REPLICATION CLIENT` privilege in MySQL grants a user the ability to perform certain operations related to replication. Specifically, a user with this privilege can:

1. **Check the replication status**:
   - The user can execute `SHOW MASTER STATUS` to view the binary log file and position of the master server.
   - The user can execute `SHOW SLAVE STATUS` (or `SHOW REPLICA STATUS` in MySQL 8.0.22 and later) to view the replication status of the slave server.

2. **Check binary log coordinates**:
   - The user can use the `SHOW BINARY LOGS` command to see the list of binary logs on the master server.
   - The user can execute `SHOW BINLOG EVENTS` to view the events within a binary log.

The `REPLICATION CLIENT` privilege does not allow the user to start or stop replication, change replication configuration, or modify data. It is primarily used for monitoring and viewing the replication status and binary log information.

Here's how you might grant this privilege to a user:

```sql
GRANT REPLICATION CLIENT ON *.* TO 'username'@'host';
```

And to revoke this privilege:

```sql
REVOKE REPLICATION CLIENT ON *.* FROM 'username'@'host';
```

### Example Use Cases

- **Monitoring Replication**:
  - A monitoring system or DBA might use this privilege to keep an eye on the replication status without needing full administrative rights.
- **Debugging Replication Issues**:
  - DBAs can use the `SHOW SLAVE STATUS` or `SHOW REPLICA STATUS` command to troubleshoot replication issues.

### Security Considerations

Granting the `REPLICATION CLIENT` privilege does not pose a significant security risk since it only allows read access to certain status information. However, always ensure that privileges are granted only to trusted users and only as needed.


To grant a user the ability to replicate from the primary (master) MySQL server to a replica (slave), you need to provide them with the REPLICATION SLAVE privilege. This privilege allows the user to read the binary log files from the primary server, which is essential for replication to work.
	
	GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'replica_host' IDENTIFIED BY 'replica_password';

Optionally, grant the REPLICATION CLIENT privilege:
This allows the user to check the replication status.
	
	GRANT REPLICATION CLIENT ON *.* TO 'replica_user'@'replica_host';

Flush the privileges to ensure that the changes take effect:
	
	FLUSH PRIVILEGES;

Redundancy in IT systems means having the ability to duplicate your system components, whether on hardware, VMs, or the cloud. At the user level, a simple example is making a copy of the user's PC system and storing it on another PC as a spare in case the user's PC fails.

SQL REPLICATION: 
	MASTER - SLAVE REPLICATION:
		The most basic kind of SQL Replication.
		You have a main database server -> master server.
		This is responsible for performing all writes and updates.
		The data from this server is continously copied to a slave server.
		Slave server can be read from, but can not be written to.
		This setup allows you to distribute the reads across multiple machines.
		Hence improving your application's performance.
		Main reason for setting up master-slave replication is to handle failover.
		If master server becomes unavailable, you can still read from slave server.
		Also possible to convert the slave into a master incase your master is offline for a long time.

		This is one area where we begin to see how redundancy and backup can complement each other.
		You can replicate data from the master to the slave.
		Then you can temporarily disable replication to mantain a consistent state of information on the slave.
		Then backup the database using an appropriate backup mechanism.

	MASTER-MASTER REPLICATION:
		Both database servers have master abilities.
		Both servers can accept writes and updates.
		Each server will transfer the changes to the opposite server.
		Has the advantages of the master slave setup,
		and also benefits from increased write performance if the writes are properly distributed by a load balancing mechanism.
		incase one server goes down, the other will remain up and accept requests.
		This configuration is more complicated, but:
			the failover incase of a problem is less complicated than the master-slave configuration,
			because the slave db server does not need to transform into a master.
		Can also be combined with a backup mechanism, if you take one of the masters offline.
		For backups to function correctly, you must mantain a static db.						                      Ensure no data is being modified, or written to until after the backup is complete.

1. Configuring source server ufw firewall
------------------------------------------
The source's firewall is configured to block/ deny all incoming traffic except ssh, http and https.
So it will block any connection attempts from the replica MySQL instance.

We need to include a UFW rule that allows connections from the replica through the source's firewall.
We run this command on our source server:
		sudo ufw allow from <replica_ip_address> to any port 3306

		This command allows any connections from the replica server ip to MySQL default port number 3306

2. Updating the source MySQL instance configuration to enable replication
--------------------------------------------------------------------------------
Let's configure the source database

Inorder for the source Mysql db to start replicating data, we need to make a few changes to its configuration.
The default MySql server configuration file: /etc/mysql/mysql.conf.d/mysqld.cnf

Find the bind-address directive.
	bind-address    = 127.0.0.1
	127.0.0.1 -> ipv4 loopback address that represents localhost.
	It is set as the value for the bind-address directive instructs MySQL to only listen for connections on the localhost address.
	That is the MySQL instance is only able to accept connections that originate from the server where it is installed.
	
	Our project requires that we dont use this directive and instead comment it out.

We are turning our other MySQL instance into a replica of this one.
The replica must be able to read whatever new data is written to the source installation.
Configure your source MySQL instance to listen for connections on an ip address that is reachable by the replica, such as the source server's public ip address.
	So this directive will look like this:
		bind-address    = source_server_ip

server-id directive:
Defines an identifier that MySQL uses internally to distinguish servers in a replication setup.
Every server in a replication env: source + all its replicas must have their own unique server-id value.
