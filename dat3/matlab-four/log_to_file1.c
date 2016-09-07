#include "iwl_connector.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <linux/netlink.h>
//#include <linux/in.h>

#define MAX_PAYLOAD 2048
#define SLOW_MSG_CNT 1

int sock_fd = -1;							// the socket
FILE* out = NULL;

void check_usage(int argc, char** argv);

FILE* open_file(char* filename, char* spec);

void caught_signal(int sig);

void exit_program(int code);
void exit_program_err(int code, char* func);

int main(int argc, char** argv)
{
	/* Local variables */
	struct sockaddr_nl proc_addr, kern_addr;	// addrs for recv, send, bind
	struct cn_msg *cmsg;
	char buf[4096];
	char receivedata[1024];
	int ret;
	unsigned short l, l2;
	int count = 0;

	/* Make sure usage is correct */
	check_usage(argc, argv);

	/* Open and check log file */
	out = open_file(argv[1], "w");

	/* Setup the socket */
	sock_fd = socket(PF_NETLINK, SOCK_DGRAM, NETLINK_CONNECTOR);
	if (sock_fd == -1)
		exit_program_err(-1, "socket");

	/* Initialize the address structs */
	memset(&proc_addr, 0, sizeof(struct sockaddr_nl));
	proc_addr.nl_family = AF_NETLINK;
	proc_addr.nl_pid = getpid();			// this process' PID
	proc_addr.nl_groups = CN_IDX_IWLAGN;
	memset(&kern_addr, 0, sizeof(struct sockaddr_nl));
	kern_addr.nl_family = AF_NETLINK;
	kern_addr.nl_pid = 0;					// kernel
	kern_addr.nl_groups = CN_IDX_IWLAGN;

	/* Now bind the socket */
	if (bind(sock_fd, (struct sockaddr *)&proc_addr, sizeof(struct sockaddr_nl)) == -1)
		exit_program_err(-1, "bind");

	/* And subscribe to netlink group */
	{
		int on = proc_addr.nl_groups;
		ret = setsockopt(sock_fd, 270, NETLINK_ADD_MEMBERSHIP, &on, sizeof(on));
		if (ret)
			exit_program_err(-1, "setsockopt");
	}

	/* Set up the "caught_signal" function as this program's sig handler */
	signal(SIGINT, caught_signal);

	int serverSock,clientSock;
	struct sockaddr_in server_addr,client_addr;
	int sin_size;
	unsigned short portnum=0x8888; 
	serverSock = socket(AF_INET, SOCK_STREAM, 0);
	bzero(&server_addr,sizeof(struct sockaddr_in));
	server_addr.sin_family=AF_INET;
	//server_addr.sin_addr.s_addr=htonl(INADDR_ANY); 
	server_addr.sin_addr.s_addr=inet_addr("192.168.1.101");;
	server_addr.sin_port=htons(portnum);

	if(-1 == bind(serverSock,(struct sockaddr *)(&server_addr), sizeof(struct sockaddr)))
	{
		 printf("bind fail !\r\n");
		 return -1;
	}

	if(-1 == listen(serverSock,5))
	{
		printf("listen fail !\r\n");
		return -1;
	}
	sin_size = sizeof(struct sockaddr_in);
	printf("wait to connect\r\n");

	clientSock = accept(serverSock, (struct sockaddr *)(&client_addr), (socklen_t *)(&sin_size));
	//printf("Server start get connect from %#x\r\n",ntohl(client_addr.sin_addr.s_addr));
	printf("accept client %s \n",inet_ntoa(client_addr.sin_addr));  

	recv(clientSock,receivedata,sizeof(receivedata),0);
	char makesuredata[10] ;
	memset(makesuredata,0,10);
	strncpy(makesuredata,receivedata,2);
	if (strcmp(makesuredata,"OK") == 0)
	{
		printf("OK , go to while loop\n");
	}
	else
	{
		printf("revdata is %s,but also go to while loop \n",makesuredata);
	}
  
	/* Poll socket forever waiting for a message */
	while (1)
	{
		/* Receive from socket with infinite timeout */
		ret = recv(sock_fd, buf, sizeof(buf), 0);
		if (ret == -1)
			exit_program_err(-1, "recv");
		cmsg = NLMSG_DATA(buf);
		if (count % SLOW_MSG_CNT == 0)
			printf("received %d bytes: id: %d val: %d seq: %d clen: %d\n", cmsg->len, cmsg->id.idx, cmsg->id.val, cmsg->seq, cmsg->len);
		l = (unsigned short) cmsg->len;
		l2 = htons(l);
		// fwrite(&l2, 1, sizeof(unsigned short), out);
		// if(-1 == write(clientSock,(char *)(&l2),sizeof(unsigned short)))
		// {
		//   printf("send lenth info fail!\r\n");
		//   return -1;
		// }
		// ret = fwrite(cmsg->data, 1, l, out);
		// if(-1 == write(clientSock,(char *)cmsg->data,l))
		// {
		//   printf("send data fail!\r\n");
		//   return -1;
		// }
		fwrite(&l2, 1, sizeof(unsigned short), out);
		ret = fwrite(cmsg->data, 1, l, out);
		
		char data[1024];
		memset(data,0,1024);
		char low,high;
		low = l & 0xff;
		high = ( l >> 8) & 0xff;
		data[0] = high;
		data[1] = low;
		memcpy(data+2,(char *)cmsg->data,l);
		
		//strcat(data,(char *)(&l2));
		//strcat(data,(char *)cmsg->data);
		if(-1 == write(clientSock,data,l+sizeof(unsigned short)))
		{
			printf("send data fail!\r\n");
			return -1;
		}

		if (count % 100 == 0)
		 	printf("wrote %d bytes [msgcnt=%u]\n", ret, count);
		++count;
		if (ret != l)
		 	exit_program_err(1, "fwrite");  
	}

	exit_program(0);
	return 0;
}

void check_usage(int argc, char** argv)
{
	if (argc != 2)
	{
		fprintf(stderr, "Usage: %s <output_file>\n", argv[0]);
		exit_program(1);
	}
}

FILE* open_file(char* filename, char* spec)
{
	FILE* fp = fopen(filename, spec);
	if (!fp)
	{
		perror("fopen");
		exit_program(1);
	}
	return fp;
}

void caught_signal(int sig)
{
	fprintf(stderr, "Caught signal %d\n", sig);
	exit_program(0);
}

void exit_program(int code)
{
	if (out)
	{
		fclose(out);
		out = NULL;
	}
	if (sock_fd != -1)
	{
		close(sock_fd);
		sock_fd = -1;
	}
	exit(code);
}

void exit_program_err(int code, char* func)
{
	perror(func);
	exit_program(code);
}
