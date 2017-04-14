
What is Open vSwitch?
---------------------

Open vSwitch is a multilayer software switch licensed under the open
source Apache 2 license.  Open vSwitch is well suited to function as a virtual switch in VM
environments.  In addition to exposing standard control and visibility
interfaces to the virtual networking layer, it was designed to support
distribution across multiple physical servers.  Open vSwitch supports
multiple Linux-based virtualization technologies including
Xen/XenServer, KVM, and VirtualBox.

The bulk of the code is written in platform-independent C and is
easily ported to other environments.  The current release of Open
vSwitch supports the following features:

* Standard 802.1Q VLAN model with trunk and access ports
* NIC bonding with or without LACP on upstream switch
* NetFlow, sFlow(R), and mirroring for increased visibility
* QoS (Quality of Service) configuration, plus policing
* Geneve, GRE, GRE over IPSEC, VXLAN, and LISP tunneling
* 802.1ag connectivity fault management
* OpenFlow 1.0 plus numerous extensions
* Transactional configuration database with C and Python bindings
* High-performance forwarding using a Linux kernel module

The included Linux kernel module supports Linux 2.6.32 and up, with
testing focused on 2.6.32 with Centos and Xen patches.  Open vSwitch
also has special support for Citrix XenServer and Red Hat Enterprise
Linux hosts.

Open vSwitch can also operate, at a cost in performance, entirely in
userspace, without assistance from a kernel module.  This userspace
implementation should be easier to port than the kernel-based switch.
It is considered experimental.

What's here?
------------

The main components of this distribution are:

* ovs-vswitchd, a daemon that implements the switch, along with
  a companion Linux kernel module for flow-based switching.
* ovsdb-server, a lightweight database server that ovs-vswitchd
  queries to obtain its configuration.
* ovs-dpctl, a tool for configuring the switch kernel module.
* Scripts and specs for building RPMs for Citrix XenServer and Red
  Hat Enterprise Linux.  The XenServer RPMs allow Open vSwitch to
  be installed on a Citrix XenServer host as a drop-in replacement
  for its switch, with additional functionality.
* ovs-vsctl, a utility for querying and updating the configuration
  of ovs-vswitchd.
* ovs-appctl, a utility that sends commands to running Open
      vSwitch daemons.

Open vSwitch also provides some tools:

* ovs-ofctl, a utility for querying and controlling OpenFlow
  switches and controllers.
* ovs-pki, a utility for creating and managing the public-key
  infrastructure for OpenFlow switches.
* ovs-testcontroller, a simple OpenFlow controller that may be useful
  for testing (though not for production).
* A patch to tcpdump that enables it to parse OpenFlow messages.



