## How to run it

To run the client that connects with the API, you must be within the cluster machine and run the command

```bash
$ ./client.sh -t <text>
```

Just like the example below:

```bash
$ ./client.sh -t “#covid19 new york”
```

You don’t need to provide the IP address, since the client discovers it automatically by searching by the service name on kubernetes.
