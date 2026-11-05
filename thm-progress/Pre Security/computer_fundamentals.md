# Module 2: Computer Fundamentals

We use computers everyday without even knowing how it runs, how many types it ahs and just how much work is put into making it
secure for us to use it daily.

## Inside a Computer

A computer processes instructions through hardware components operating in coordination:

- CPU (Central Processing Unit): The "brain." Executes instructions via the fetch-decode-execute cycle.
- RAM (Random Access Memory): High-speed, volatile temporary workspace. All running programs and files reside here while active; data disappears when powered off.
- Storage (SSD / HDD): Non-volatile long-term storage where the OS, applications, and saved files live permanently.
- Motherboard: The printed circuit board that physically connects and routes electrical signals between the CPU, RAM, storage, and peripheral devices.
- Network Interface Card (NIC): Hardware enabling communication over physical Ethernet or wireless radio waves.

## Types of Computers
There are many different types of computers, the traditional desktops, laptops to devices which you wouldn't think are
computers but in fact are computers, we list some of them below:

- Microcontrollers & Embedded Systems: Single-purpose chips embedded inside appliances, IoT devices, medical equipment, and automotive controllers.
- Personal Computers (Desktops / Laptops): General-purpose workstations designed for individual end-user productivity.
- Servers: High-capacity, robust machines built to run continuously without downtime, handling incoming client requests over a network.
- Supercomputers / Mainframes: Massive clustered systems configured to process large-scale simulations, high-volume transactions, or data-intensive scientific calculations.

## Client-Server Basics

Modern network architecture primarily operates on a request-response model:

- Client: The requesting party (e.g., your web browser on a laptop).
- Server: The serving party waiting on an open port (e.g., an Nginx or Apache web server).
- Workflow: The client sends a request (e.g., “GET /login”), the server parses the request, executes required backend queries, and sends back a response containing status codes and payload data.

## Virtualization Basics

Virtualization uses a software layer called a Hypervisor to run multiple isolated virtual machines (VMs) with independent operating systems on a single physical host machine.
- Type 1 (Bare-Metal): Runs directly on hardware without a host OS (e.g., VMware ESXi, Proxmox VE). Preferred in enterprise environments for speed and low overhead.
- Type 2 (Hosted): Runs as an application inside a host OS (e.g., VirtualBox, VMware Workstation).
Security Relevance: Provides safe, disposable sandboxes to execute suspected malware and isolate network services.

## Cloud Computing Fundamentals

Cloud computing refers to on-demand delivery of computing services (servers, storage, databases, networking) over the internet with pay-as-you-go pricing.
Service Models:

- IaaS (Infrastructure as a Service): Rent raw VMs, networks, and storage (e.g., AWS EC2, Azure VMs).
- PaaS (Platform as a Service): Deploy code directly without managing OS or runtime patches (e.g., Heroku, Google App Engine).
- SaaS (Software as a Service): Access turnkey software hosted remotely (e.g., Microsoft 365, Google Workspace).
- Shared Responsibility Model: Cloud providers protect the physical hardware and data centers; the customer is responsible for configuring access rights, credentials, data encryption, and software updates.
