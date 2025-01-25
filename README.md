# Load Balancer Project

## Overview
This project demonstrates a distributed load-balancing system with server health monitoring. It is designed to:
- Minimize response time.
- Maximize server utilization.
- Ensure that no server is overloaded.

The load balancer uses the **Round Robin algorithm** to distribute traffic among servers, while monitoring their health to ensure efficient and reliable request handling.

---

## Features

### 1. **Load Balancer**
- Routes client requests to multiple backend servers.
- Monitors server health via periodic health checks.
- Handles server failures gracefully by rerouting traffic to healthy servers.

### 2. **Backend Servers**
- Simulates multiple servers responding to client requests.
- Provides simple responses to demonstrate the load balancer's request distribution.

### 3. **Health Monitoring**
- Automatically detects server failures and removes unhealthy servers from the pool.
- Re-adds servers to the pool once they are healthy again.

---

## How It Works

1. **Server Initialization**:
   - Three backend servers are started, running on ports **5001**, **5002**, and **5003**.

2. **Load Balancer Setup**:
   - The load balancer is initialized and listens for client requests on port **5432**.

3. **Request Handling**:
   - Clients send HTTP requests to the load balancer.
   - The load balancer distributes these requests among the available backend servers using the **Round Robin algorithm**.

4. **Server Failure and Recovery**:
   - If a server goes down, the load balancer detects the failure via health checks.
   - Requests are routed to the remaining healthy servers.
   - When the failed server is restored, it is reintegrated into the pool.

---

## Showcase

To better understand the workflow, visit https://loadbalancer-tau.vercel.app/. This page provides visual demonstrations of the load balancer in action.
