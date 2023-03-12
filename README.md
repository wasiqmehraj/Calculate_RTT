Description:

This Github repository contains code that implements data transfer between two endpoints. One file is responsible for initiating the data transfer and sending the data, while the other file bounces the data back to the initiator. Additionally, there is a third file that is used for testing purposes, which sends the data only once.

The initiator file allows the user to specify how many times they want to send the data. It keeps track of when the data was sent and when it was received back from the other endpoint. At the end of the data transfer, the initiator file calculates the average round trip time for all of the data that was sent.

The code is written in a modular and extensible way, allowing for easy modification and customization. The data transfer protocol is implemented using low-level socket programming in Python, making it efficient and reliable.

This project is useful for testing network connectivity and latency between two endpoints. It can be used to benchmark network performance or to troubleshoot network issues. The code can be easily integrated into other projects and customized to meet specific requirements.

Overall, this repository provides a simple and effective way to transfer data between two endpoints and measure network performance.
