%global _hardened_build 1

%global EXCLUDE_MODULES cachedb_cassandra %{!?_with_oracle:db_oracle} osp python sngtc

Summary:  Open Source SIP Server
Name:     opensips
Version:  3.0.2
Release:  7%{?dist}
License:  GPLv2+
Source0:  https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Fedora-specific patches
Patch001: opensips-0001-Consistently-use-rtpproxy-switches.patch
Patch002: opensips-0002-Cleanup-Oracle-s-makefiles.patch
Patch003: opensips-0003-db_ora-null-terminating-string-is-more-safely-most-m.patch
Patch004: opensips-0004-Return-actual-payload-ID-in-case-of-a-dynamic-payloa.patch
Patch005: opensips-0005-Don-t-remove-pthread-library-explicitly-from-mi_xmlr.patch
Patch006: opensips-0006-Dont-try-modifying-CFLAGS.patch
Patch007: opensips-0007-Add-missing-typedef-keyword.patch
Patch008: opensips-0008-Fix-building-with-gcc-10.patch
Patch009: opensips-0009-dispatcher-Fix-missing-tmb-definition.patch
Patch010: opensips-0010-Fix-more-gcc-10-compilation-errors.patch
Patch011: opensips-0011-Add-support-for-upcoming-json-c-0.14.0.patch

URL:      https://opensips.org

BuildRequires: GeoIP-devel
BuildRequires: bison
BuildRequires: docbook-xsl
BuildRequires: expat-devel
BuildRequires: flex
BuildRequires: gcc
BuildRequires: json-c-devel
BuildRequires: libconfuse-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt
BuildRequires: lynx
BuildRequires: ncurses-devel
BuildRequires: openldap-devel
BuildRequires: pcre-devel
# FIXME disable python2 until upstream adds support for Py3
#BuildRequires: python2-devel
BuildRequires: systemd-units
BuildRequires: xmlrpc-c-devel

# Users and groups
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Obsoletes: %{name}-auth_diameter
Obsoletes: %{name}-event_datagram
Obsoletes: %{name}-mi_xmlrpc
Obsoletes: %{name}-xmlrpc
Obsoletes: %{name}-python < 2.4.6-4
Obsoletes: python2-%{name} < 2.4.6-4

%description
OpenSIPS or Open SIP Server is a very fast and flexible SIP (RFC3261)
proxy server. Written entirely in C, opensips can handle thousands calls
per second even on low-budget hardware. A C Shell like scripting language
provides full control over the server's behaviour. It's modular
architecture allows only required functionality to be loaded.
Currently the following modules are available: digest authentication,
CPL scripts, instant messaging, MySQL and UNIXODBC support, a presence agent,
radius authentication, record routing, an SMS gateway, a jabber gateway, a
transaction and dialog module, OSP module, statistics support,
registrar and user location.

%package  aaa_radius
Summary:  RADIUS backend for AAA api
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: freeradius-client-devel

%description aaa_radius
This module provides the RADIUS backend for the AAA API - group, auth, uri
module use the AAA API for performing RADIUS ops.

%package  acc
Summary:  Accounts transactions information to different backends
Requires: %{name}%{?_isa} = %{version}-%{release}

%description acc
ACC module is used to account transactions information to different backends
like syslog, SQL, AAA.

%package  auth_aaa
Summary:  Performs authentication using an AAA server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description auth_aaa
This module contains functions that are used to perform authentication using
an AAA server.  Basically the proxy will pass along the credentials to the
AAA server which will in turn send a reply containing result of the
authentication. So basically the whole authentication is done in the AAA
server.

%package  b2bua
Summary:  Back-2-Back User Agent
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description b2bua
B2BUA is an implementation of the behavior of a B2BUA as defined in RFC 3261
that offers the possibility to build certain services on top of it.

%package  cachedb_couchbase
Summary:  Couchbase connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libcouchbase-devel

%description cachedb_couchbase
Couchbase module is an implementation of a cache system designed to
work with a Couchbase server.

%package  cachedb_memcached
Summary:  Memcached connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-memcached%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-memcached
BuildRequires: libmemcached-devel

%description cachedb_memcached
Memcached module is an implementation of a cache system designed to
work with a memcached server.

%package  cachedb_mongodb
Summary:  MongoDB connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: json-c-devel
BuildRequires: mongo-c-driver-devel
BuildRequires: snappy-devel

%description cachedb_mongodb
MongoDB module is an implementation of a cache system designed to
work with a MongoDB server.

%package  cachedb_redis
Summary:  Redis connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-redis%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-redis
BuildRequires: hiredis-devel

%description cachedb_redis
This module is an implementation of a cache system designed to work
with a Redis server.

%package  call_center
Summary:  An inbound call center system
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}

%description call_center
The Call Center module implements an inbound call center system with call flows
(for queueing the received calls) and agents (for answering the calls).

%package  carrierroute
Summary:  Routing extension suitable for carriers
Requires: %{name}%{?_isa} = %{version}-%{release}

%description carrierroute
A module which provides routing, balancing and blacklisting capabilities.

%package  cgrates
Summary:  Billing module for CGRates engine
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cgrates
This module can be used to communicate with the CGRates engine in order to do
call authorization and accounting for billing purposes. The OpenSIPS module
does not do any billing by itself, but provides an interface to communicate
with the CGRateS engine using efficient JSON-RPC APIs in both synchronous and
asynchronous ways.

%package  compression
Summary:  Message compression/decompression and base64 encoding
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: zlib-devel

%description compression
This module provides message compression/decompression and base64 encoding for
sip messages using deflate and gzip algorithm/headers. Another feature of this
module is reducing headers to compact for as specified in SIP RFC's, sdp body
codec unnecessary description removal (for codecs 0-97), whitelist for headers
not be removed (excepting necessary headers).

%package  cpl_c
Summary:  Call Processing Language interpreter
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-cpl-c%{?_isa} = %{version}-%{release}
Provides: %{name}-cpl-c = %{version}-%{release}
Obsoletes:%{name}-cpl-c < 2.2.2-1

%description cpl_c
This module implements a CPL (Call Processing Language) interpreter.
Support for uploading/downloading/removing scripts via SIP REGISTER method
is present.

%package  db_berkeley
Summary:  Berkeley DB backend support
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libdb-devel

%description db_berkeley
This is a module which integrates the Berkeley DB into OpenSIPS. It implements
the DB API defined in OpenSIPS.

%package  db_http
Summary:  HTTP DB backend support
Requires: %{name}%{?_isa} = %{version}-%{release}

%description db_http
This module provides access to a database that is implemented as a
HTTP server.

%package  db_mysql
Summary:  MySQL storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-mysql%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-mysql
BuildRequires: mysql-devel

%description db_mysql
This module contains the MySQL plugin for %{name}, which allows
a MySQL database to be used for persistent storage.

%if 0%{?_with_oracle}
%package  db_oracle
Summary:  Oracle storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-oracle%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-oracle
BuildRequires: oracle-instantclient-devel

%description db_oracle
This module package contains the Oracle plugin for %{name}, which allows
a Oracle database to be used for persistent storage.
%endif

%package  db_perlvdb
Summary:  Perl virtual database engine
# require perl-devel for >F7 and perl for <=F6
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-perl%{?_isa} = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides: %{name}-perlvdb%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-perlvdb

%description db_perlvdb
The Perl Virtual Database (VDB) provides a virtualization framework for
OpenSIPS's database access. It does not handle a particular database engine
itself but lets the user relay database requests to arbitrary Perl functions.

%package  db_postgresql
Summary:  PostgreSQL storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-postgresql%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-postgresql
BuildRequires: libpq-devel

%description db_postgresql
This module contains the PostgreSQL plugin for %{name},
which allows a PostgreSQL database to be used for persistent storage.

%package  db_sqlite
Summary:  SQLite sorage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: sqlite-devel

%description db_sqlite
This module contains the SQLite plugin for %{name}, which
allows SQLite to be used for persistent storage.

%package  db_unixodbc
Summary:  OpenSIPS unixODBC Storage support
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-unixodbc%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-unixodbc
BuildRequires: unixODBC-devel

%description db_unixodbc
This module contains the unixODBC plugin for %{name}, which
allows unixODBC to be used for persistent storage.

%package  event_rabbitmq
Summary:  Event RabbitMQ module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel

%description event_rabbitmq
This module provides the implementation of a RabbitMQ client for the Event Interface.
It is used to send AMQP messages to a RabbitMQ server each time the Event Interface
triggers an event subscribed for.

%package  emergency
Summary:  Emergency call treatment
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel

%description emergency
This module provides emergency call treatment for OpenSIPS, following the
architecture i2 specification of the American entity NENA. (National Emergency
Number Association).

%package  h350
Summary:  H350 implementation
Requires: %{name}%{?_isa} = %{version}-%{release}

%description h350
The OpenSIPS H350 module enables an OpenSIPS SIP proxy server to access SIP
account data stored in an LDAP [RFC4510] directory  containing H.350 [H.350]
commObjects.

%package  httpd
Summary:  HTTP transport layer implementation
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmicrohttpd-devel

%description httpd
This module provides an HTTP transport layer for OpenSIPS.

%package  identity
Summary:  Support for SIP Identity (see RFC 4474)
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(openssl)

%description identity
This module provides support for SIP Identity (see RFC 4474).

%package  jabber
Summary:  Gateway between OpenSIPS and a jabber server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description jabber
Jabber module that integrates XODE XML parser for parsing Jabber messages.

%package  json
Summary:  A JSON variables within the script
Requires: %{name}%{?_isa} = %{version}-%{release}

%description json
This module introduces a new type of variable that provides both serialization and
de-serialization from JSON format.

%package  ldap
Summary:  LDAP connector
Requires: %{name}%{?_isa} = %{version}-%{release}

%description ldap
The LDAP module implements an LDAP search interface for OpenSIPS.

%package  lua
Summary:  Helps implement your own OpenSIPS extensions in Lua
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: compat-lua-devel
BuildRequires: libmemcached-devel

%description lua
The time needed when writing a new OpenSIPS module unfortunately is quite
high, while the options provided by the configuration file are limited to
the features implemented in the modules. With this Lua module, you can
easily implement your own OpenSIPS extensions in Lua.

%package  mi_html
Summary:  A minimal web user interface for the Management Interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}

%description mi_html
This module implements a minimal web user interface for the OpenSIPS's
Management Interface.

%package  mi_http
Summary:  A JSON REST interface for the Management Interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}

%description mi_http
This module implements a JSON server for the Management Interface that handles
GET requests and generates JSON responses.

%package  mi_xmlrpc_ng
Summary:  A xmlrpc server for the Management Interface (new version)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}
Provides: %{name}-xmlrpc_ng%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-xmlrpc_ng

%description mi_xmlrpc_ng
This module implements a xmlrpc server that handles xmlrpc requests and generates
xmlrpc responses. When a xmlrpc message is received a default method is executed.

%package  mmgeoip
Summary:  Wrapper for the MaxMind GeoIP API
Requires: %{name}%{?_isa} = %{version}-%{release}

%description mmgeoip
Mmgeoip is a lightweight wrapper for the MaxMind GeoIP API. It adds
IP address-to-location lookup capability to OpenSIPS scripts.

%package  peering
Summary:  Radius peering
Requires: %{name}%{?_isa} = %{version}-%{release}

%description peering
Peering module allows SIP providers (operators or organizations)
to verify from a broker if source or destination  of a SIP request
is a trusted peer.

%package  perl
Summary:  Helps implement your own OpenSIPS extensions in Perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Embed), perl-devel
BuildRequires: perl-generators
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description perl
The time needed when writing a new OpenSIPS module unfortunately is quite
high, while the options provided by the configuration file are limited to
the features implemented in the modules. With this Perl module, you can
easily implement your own OpenSIPS extensions in Perl.  This allows for
simple access to the full world of CPAN modules. SIP URI rewriting could be
implemented based on regular expressions; accessing arbitrary data backends,
e.g. LDAP or Berkeley DB files, is now extremely simple.

%package  pi_http
Summary:  A HTTP provisioning interface for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}

%description pi_http
This module provides an HTTP provisioning interface for OpenSIPS. It is using
the OpenSIPS's internal database API to provide a simple way of manipulating
records inside OpenSIPS's tables.

%package  presence
Summary:  Presence server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description presence
This module implements a presence server. It handles PUBLISH and SUBSCRIBE
messages and generates NOTIFY messages. It offers support for aggregation
of published presence information for the same presentity using more devices.
It can also filter the information provided to watchers according to privacy
rules.

%package  presence_callinfo
Summary:  SIMPLE Presence extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_callinfo
The module enables the handling of "call-info" and "line-seize" events inside
the presence module. It is used with the general event handling module:
presence and it constructs and adds "Call-Info" headers to notification events.
To send "call-info" notification to watchers, a third-party application must
publish "call-info" events to the presence server.

%package  presence_dialoginfo
Summary:  Extension to Presence server for Dialog-Info
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_dialoginfo
The module enables the handling of "Event: dialog" (as defined
in RFC 4235) inside of the presence module. This can be used
distribute the dialog-info status to the subscribed watchers.

%package  presence_mwi
Summary:  Extension to Presence server for Message Waiting Indication
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description presence_mwi
The module does specific handling for notify-subscribe message-summary
(message waiting indication) events as specified in RFC 3842. It is used
with the general event handling module, presence. It constructs and adds
message-summary event to it.

%package  presence_xcapdiff
Summary:  Extension to Presence server for XCAP-DIFF event
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-pua_mi%{?_isa} = %{version}-%{release}

%description presence_xcapdiff
The presence_xcapdiff is an OpenSIPS module that adds support
for the "xcap-diff" event to presence and pua.

%package  presence_xml
Summary:  SIMPLE Presence extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xcap_client%{?_isa} = %{version}-%{release}

%description presence_xml
The module does specific handling for notify-subscribe events using xml bodies.
It is used with the general event handling module, presence.

%package  proto_sctp
Summary:  An optional SCTP transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lksctp-tools-devel

%description proto_sctp
This module is an optional transport module (shared library) which exports the
required logic in order to handle SCTP-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "sctp:" listeners in your
script.

%package  proto_tls
Summary:  An optional TLS transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(openssl)
Obsoletes: %{name}-tlsops

%description proto_tls
This module is an optional transport module (shared library) which exports the
required logic in order to handle TLS-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "tls:" listeners in your
script.

%package  proto_wss
Summary:  An optional Secure WebSocket transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(openssl)

%description proto_wss
This module is an optional transport module (shared library) which exports the
required logic in order to handle Secure WebSocket-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "wss:" listeners in your
script.

%package  pua
Summary:  Offer the functionality of a presence user agent client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pua
This module offer the functionality of a presence user agent client, sending
Subscribe and Publish messages.

%package  pua_bla
Summary:  BLA extension for PUA
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}

%description pua_bla
The pua_bla module enables Bridged Line Appearances support according to the
specifications in draft-anil-sipping-bla-03.txt.

%package  pua_dialoginfo
Summary:  Dialog-Info extension for PUA
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description pua_dialoginfo
The pua_dialoginfo retrieves dialog state information from the dialog module
and PUBLISHes the dialog-information using the pua module. Thus, in combination
with the presence_xml module this can be used to derive dialog-info from the
dialog module and NOTIFY the subscribed watchers about dialog-info changes.

%package  pua_mi
Summary:  Connector between usrloc and MI interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description pua_mi
The pua_mi sends offer the possibility to publish presence information
via MI transports.  Using this module you can create independent
applications/scripts to publish not sip-related information (e.g., system
resources like CPU-usage, memory, number of active subscribers ...)

%package  pua_usrloc
Summary:  Connector between usrloc and pua modules
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}

%description pua_usrloc
This module is the connector between usrloc and pua modules. It creates the
environment to send PUBLISH requests for user location records, on specific
events (e.g., when new record is added in usrloc, a PUBLISH with status open
(online) is issued; when expires, it sends closed (offline)). Using this
module, phones which have no support for presence can be seen as
online/offline.

%package  pua_xmpp
Summary:  SIMPLE-XMPP Presence gateway
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xmpp%{?_isa} = %{version}-%{release}

%description pua_xmpp
This module is a gateway for presence between SIP and XMPP. It translates one
format into another and uses xmpp, pua and presence modules to manage the
transmition of presence state information.

# FIXME disable python2 until upstream adds support for Py3
#%package  -n python2-opensips
#%{?python_provide:%python_provide python2-opensips}
# Remove before F30
#Provides: %{name}-python = %{version}-%{release}
#Provides: %{name}-python%{?_isa} = %{version}-%{release}
#Obsoletes: %{name}-python < %{version}-%{release}
#Summary:  Python scripting support
#Requires: %{name}%{?_isa} = %{version}-%{release}

#%description -n python2-opensips
#Helps implement your own OpenSIPS extensions in Python

%package  rabbitmq
Summary:  RabbitMQ module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel

%description rabbitmq
This module allows sending AMQP messages to a RabbitMQ server. Messages can be
easily customized according to the AMQP specifications, as well the RabbitMQ
extensions.

%package  rabbitmq_consumer
Summary:  RabbitMQ message receiver
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel

%description rabbitmq_consumer
This module allows managing received messages in queues, taking advantage of
the flexible AMQP protocol.

%package  regex
Summary:  RegExp via PCRE library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description regex
This module offers matching operations against regular
expressions using the powerful PCRE library.

%package  rest_client
Summary:  HTTP client module for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}

%description rest_client
This module provides a means of interacting with an HTTP server by doing
RESTful queries, such as GET and POST.

%package  rls
Summary:  Resource List Server
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xcap%{?_isa} = %{version}-%{release}

%description rls
The modules is a Resource List Server implementation following the
specification in RFC 4662 and RFC 4826.

%package  seas
Summary:  Transfers the execution logic control to a given external entity
Requires: %{name}%{?_isa} = %{version}-%{release}

%description seas
SEAS module enables OpenSIPS to transfer the execution logic control of a sip
message to a given external entity, called the Application Server. When the
OpenSIPS script is being executed on an incoming SIP message, invocation of
the as_relay_t() function makes this module send the message along with some
transaction information to the specified Application Server. The Application
Server then executes some call-control logic code, and tells OpenSIPS to take
some actions, ie. forward the message downstream, or respond to the message
with a SIP repy, etc

%package  siprec
Summary:  Call recording using SIPREC protocol
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}

%description siprec
This module provides the means to do calls recording using an external recorder
- the entity that records the call is not in the media path between the caller
and callee, but it is completely separate, thus it can not affect by any means
the quality of the conversation. This is done in a standardized manner, using
the SIPREC Protocol, thus it can be used by any recorder that implements this
protocol.

%package  sms
Summary:  Gateway between SIP and GSM networks via sms
Requires: %{name}%{?_isa} = %{version}-%{release}

%description sms
This module provides a way of communication between SIP network (via SIP
MESSAGE) and GSM networks (via ShortMessageService). Communication is
possible from SIP to SMS and vice versa.  The module provides facilities
like SMS confirmation--the gateway can confirm to the SIP user if his
message really reached its destination as a SMS--or multi-part messages--if
a SIP messages is too long it will be split and sent as multiple SMS.

%package  snmpstats
Summary:  SNMP management interface for the OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires: net-snmp-devel

%description snmpstats
The %{name}-snmpstats package provides an SNMP management interface to
OpenSIPS.  Specifically, it provides general SNMP queryable scalar statistics,
table representations of more complicated data such as user and contact
information, and alarm monitoring capabilities.

%package  tls_mgm
Summary:  Management for TLS certificates and parameters
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(openssl)

%description tls_mgm
This module provides an interfaces for all the modules that use the TLS
protocol. It also implements TLS related functions to use in the routing
script, and exports pseudo variables with certificate and TLS parameters.

%package  xcap
Summary:  XCAP common functions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xcap
The module contains several parameters and functions common to all modules
using XCAP capabilities.

%package  xcap_client
Summary:  XCAP client
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel

%description xcap_client
The modules is an XCAP client for OpenSIPS that can be used by other modules.
It fetches XCAP elements, either documents or part of them, by sending HTTP
GET requests. It also offers support for conditional queries. It uses libcurl
library as a client-side HTTP transfer library.

%package  xml
Summary:  Basic XML parsing and manipulation
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xml
This module exposes a script variable that provides basic parsing and
manipulation of XML documents or blocks of XML data. The processing does not
take into account any DTDs or schemas in terms of validation.

%package  xmpp
Summary:  Gateway between OpenSIPS and a jabber server
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xmpp
This modules is a gateway between Openser and a jabber server. It enables
the exchange of instant messages between SIP clients and XMPP(jabber)
clients.

%prep
%autosetup -p1

%build
LOCALBASE=/usr NICER=0 CFLAGS="%{optflags} -fgnu89-inline" LDFLAGS="%{?__global_ldflags}" %{?_with_oracle:ORAHOME="$ORACLE_HOME"} %{__make} all modules-readme %{?_smp_mflags} TLS=1 \
  exclude_modules="%EXCLUDE_MODULES" \
  PYTHON=/usr/bin/python3 \
  cfg_target=%{_sysconfdir}/opensips/

%install
make install TLS=1 LIBDIR=%{_lib} \
  exclude_modules="%EXCLUDE_MODULES" \
  basedir=%{buildroot} prefix=%{_prefix} \
  cfg_prefix=%{buildroot} \
  DBTEXTON=yes # fixed dbtext documentation installation

# clean some things
mkdir -p %{buildroot}/%{perl_vendorlib}
if [ -d "%{buildroot}/%{_prefix}/perl" ]; then
  # for fedora>=11
  mv %{buildroot}/%{_prefix}/perl/* \
    %{buildroot}/%{perl_vendorlib}/
else
  # for fedora<=10
  mv %{buildroot}/%{_libdir}/opensips/perl/* \
    %{buildroot}/%{perl_vendorlib}/
fi
mv %{buildroot}/%{_sysconfdir}/opensips/tls/README \
  %{buildroot}/%{_docdir}/opensips/README.tls
rm -f %{buildroot}%{_docdir}/opensips/INSTALL
mv %{buildroot}/%{_docdir}/opensips docdir

# install systemd files
install -D -m 0644 -p packaging/redhat_fedora/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p packaging/redhat_fedora/%{name}.tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}

#install sysconfig file
install -D -p -m 644 packaging/redhat_fedora/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{_localstatedir}/run/%{name} -s /sbin/nologin \
-c "OpenSIPS SIP Server" %{name} 2>/dev/null || :

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%{_sbindir}/opensips
%{_sbindir}/osipsconfig

%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/rootCA
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/rootCA/certs
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/rootCA/private
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/opensips/tls/user
%dir %{_libdir}/opensips/
%dir %{_libdir}/opensips/modules/

%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755, opensips, opensips) %{_localstatedir}/run/%{name}

%config(noreplace) %{_sysconfdir}/opensips/dictionary.opensips
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(640,%{name},%{name}) %config(noreplace) %{_sysconfdir}/opensips/opensips.cfg
# these files are just an examples so no need to restrict access to them
%config(noreplace) %{_sysconfdir}/opensips/tls/ca.conf
%config(noreplace) %{_sysconfdir}/opensips/tls/request.conf
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/cacert.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/certs/01.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/index.txt
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/private/cakey.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/rootCA/serial
%config(noreplace) %{_sysconfdir}/opensips/tls/user.conf
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-calist.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-cert.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-cert_req.pem
%config(noreplace) %{_sysconfdir}/opensips/tls/user/user-privkey.pem

%dir %{_datadir}/opensips/
%dir %{_datadir}/opensips/dbtext/
%dir %{_datadir}/opensips/dbtext/opensips/
%dir %{_datadir}/opensips/menuconfig_templates/

%{_datadir}/opensips/dbtext/opensips/*
%{_datadir}/opensips/menuconfig_templates/*.m4

%{_mandir}/man5/opensips.cfg.5*
%{_mandir}/man8/opensips.8*

%doc docdir/AUTHORS
%doc docdir/NEWS
%doc docdir/README
%doc docdir/README-MODULES
%doc docdir/README.tls
%license COPYING

%{_libdir}/opensips/modules/acc.so
%{_libdir}/opensips/modules/alias_db.so
%{_libdir}/opensips/modules/auth.so
%{_libdir}/opensips/modules/auth_db.so
%{_libdir}/opensips/modules/avpops.so
%{_libdir}/opensips/modules/benchmark.so
%{_libdir}/opensips/modules/cachedb_local.so
%{_libdir}/opensips/modules/cachedb_sql.so
%{_libdir}/opensips/modules/call_control.so
%{_libdir}/opensips/modules/cfgutils.so
%{_libdir}/opensips/modules/clusterer.so
%{_libdir}/opensips/modules/db_cachedb.so
%{_libdir}/opensips/modules/db_flatstore.so
%{_libdir}/opensips/modules/db_text.so
%{_libdir}/opensips/modules/db_virtual.so
%{_libdir}/opensips/modules/dialog.so
%{_libdir}/opensips/modules/dialplan.so
%{_libdir}/opensips/modules/dispatcher.so
%{_libdir}/opensips/modules/diversion.so
%{_libdir}/opensips/modules/dns_cache.so
%{_libdir}/opensips/modules/domain.so
%{_libdir}/opensips/modules/domainpolicy.so
%{_libdir}/opensips/modules/drouting.so
%{_libdir}/opensips/modules/enum.so
%{_libdir}/opensips/modules/event_datagram.so
%{_libdir}/opensips/modules/event_flatstore.so
%{_libdir}/opensips/modules/event_jsonrpc.so
%{_libdir}/opensips/modules/event_route.so
%{_libdir}/opensips/modules/event_routing.so
%{_libdir}/opensips/modules/event_virtual.so
%{_libdir}/opensips/modules/event_xmlrpc.so
%{_libdir}/opensips/modules/exec.so
%{_libdir}/opensips/modules/fraud_detection.so
%{_libdir}/opensips/modules/freeswitch.so
%{_libdir}/opensips/modules/freeswitch_scripting.so
%{_libdir}/opensips/modules/gflags.so
%{_libdir}/opensips/modules/group.so
%{_libdir}/opensips/modules/imc.so
%{_libdir}/opensips/modules/jsonrpc.so
%{_libdir}/opensips/modules/load_balancer.so
%{_libdir}/opensips/modules/mangler.so
%{_libdir}/opensips/modules/mathops.so
%{_libdir}/opensips/modules/maxfwd.so
%{_libdir}/opensips/modules/mediaproxy.so
%{_libdir}/opensips/modules/mi_datagram.so
%{_libdir}/opensips/modules/mi_fifo.so
%{_libdir}/opensips/modules/mid_registrar.so
%{_libdir}/opensips/modules/msilo.so
%{_libdir}/opensips/modules/nat_traversal.so
%{_libdir}/opensips/modules/nathelper.so
%{_libdir}/opensips/modules/options.so
%{_libdir}/opensips/modules/path.so
%{_libdir}/opensips/modules/permissions.so
%{_libdir}/opensips/modules/pike.so
%{_libdir}/opensips/modules/proto_bin.so
%{_libdir}/opensips/modules/proto_hep.so
%{_libdir}/opensips/modules/proto_smpp.so
%{_libdir}/opensips/modules/proto_ws.so
%{_libdir}/opensips/modules/qos.so
%{_libdir}/opensips/modules/ratelimit.so
%{_libdir}/opensips/modules/registrar.so
%{_libdir}/opensips/modules/rr.so
%{_libdir}/opensips/modules/rtpengine.so
%{_libdir}/opensips/modules/rtpproxy.so
%{_libdir}/opensips/modules/script_helper.so
%{_libdir}/opensips/modules/signaling.so
%{_libdir}/opensips/modules/sip_i.so
%{_libdir}/opensips/modules/sipcapture.so
%{_libdir}/opensips/modules/sipmsgops.so
%{_libdir}/opensips/modules/sl.so
%{_libdir}/opensips/modules/speeddial.so
%{_libdir}/opensips/modules/sql_cacher.so
%{_libdir}/opensips/modules/sst.so
%{_libdir}/opensips/modules/statistics.so
%{_libdir}/opensips/modules/stun.so
%{_libdir}/opensips/modules/textops.so
%{_libdir}/opensips/modules/tm.so
%{_libdir}/opensips/modules/topology_hiding.so
%{_libdir}/opensips/modules/tracer.so
%{_libdir}/opensips/modules/uac.so
%{_libdir}/opensips/modules/uac_auth.so
%{_libdir}/opensips/modules/uac_redirect.so
%{_libdir}/opensips/modules/uac_registrant.so
%{_libdir}/opensips/modules/userblacklist.so
%{_libdir}/opensips/modules/usrloc.so

%doc docdir/README.acc
%doc docdir/README.alias_db
%doc docdir/README.auth
%doc docdir/README.auth_db
%doc docdir/README.avpops
%doc docdir/README.benchmark
%doc docdir/README.cachedb_local
%doc docdir/README.cachedb_sql
%doc docdir/README.call_control
%doc docdir/README.cfgutils
%doc docdir/README.clusterer
%doc docdir/README.db_cachedb
%doc docdir/README.db_flatstore
%doc docdir/README.db_text
%doc docdir/README.db_virtual
%doc docdir/README.dialog
%doc docdir/README.dialplan
%doc docdir/README.dispatcher
%doc docdir/README.diversion
%doc docdir/README.dns_cache
%doc docdir/README.domain
%doc docdir/README.domainpolicy
%doc docdir/README.drouting
%doc docdir/README.enum
%doc docdir/README.event_datagram
%doc docdir/README.event_flatstore
%doc docdir/README.event_jsonrpc
%doc docdir/README.event_route
%doc docdir/README.event_routing
%doc docdir/README.event_virtual
%doc docdir/README.event_xmlrpc
%doc docdir/README.exec
%doc docdir/README.fraud_detection
%doc docdir/README.freeswitch
%doc docdir/README.freeswitch_scripting
%doc docdir/README.gflags
%doc docdir/README.group
%doc docdir/README.imc
%doc docdir/README.jsonrpc
%doc docdir/README.load_balancer
%doc docdir/README.mangler
%doc docdir/README.mathops
%doc docdir/README.maxfwd
%doc docdir/README.mediaproxy
%doc docdir/README.mi_datagram
%doc docdir/README.mi_fifo
%doc docdir/README.mid_registrar
%doc docdir/README.msilo
%doc docdir/README.nat_traversal
%doc docdir/README.nathelper
%doc docdir/README.options
%doc docdir/README.path
%doc docdir/README.permissions
%doc docdir/README.pike
%doc docdir/README.proto_bin
%doc docdir/README.proto_hep
%doc docdir/README.proto_smpp
%doc docdir/README.proto_ws
%doc docdir/README.qos
%doc docdir/README.ratelimit
%doc docdir/README.registrar
%doc docdir/README.rr
%doc docdir/README.rtpengine
%doc docdir/README.rtpproxy
%doc docdir/README.script_helper
%doc docdir/README.signaling
%doc docdir/README.sip_i
%doc docdir/README.sipcapture
%doc docdir/README.sipmsgops
%doc docdir/README.sl
%doc docdir/README.speeddial
%doc docdir/README.sql_cacher
%doc docdir/README.sst
%doc docdir/README.statistics
%doc docdir/README.stun
%doc docdir/README.textops
%doc docdir/README.tm
%doc docdir/README.topology_hiding
%doc docdir/README.tracer
%doc docdir/README.uac
%doc docdir/README.uac_auth
%doc docdir/README.uac_redirect
%doc docdir/README.uac_registrant
%doc docdir/README.userblacklist
%doc docdir/README.usrloc

%files aaa_radius
%{_libdir}/opensips/modules/aaa_radius.so
%doc docdir/README.aaa_radius

%files acc
%{_libdir}/opensips/modules/acc.so
%doc docdir/README.acc

%files auth_aaa
%{_libdir}/opensips/modules/auth_aaa.so
%doc docdir/README.auth_aaa

%files b2bua
%{_libdir}/opensips/modules/b2b_entities.so
%{_libdir}/opensips/modules/b2b_logic.so
%{_libdir}/opensips/modules/b2b_sca.so
%doc docdir/README.b2b_entities
%doc docdir/README.b2b_logic
%doc docdir/README.b2b_sca

%files cachedb_couchbase
%{_libdir}/opensips/modules/cachedb_couchbase.so
%doc docdir/README.cachedb_couchbase

%files cachedb_memcached
%{_libdir}/opensips/modules/cachedb_memcached.so
%doc docdir/README.cachedb_memcached

%files cachedb_mongodb
%{_libdir}/opensips/modules/cachedb_mongodb.so
%doc docdir/README.cachedb_mongodb

%files cachedb_redis
%{_libdir}/opensips/modules/cachedb_redis.so
%doc docdir/README.cachedb_redis

%files call_center
%attr(640,%{name},%{name}) %config(noreplace) %{_sysconfdir}/opensips/scenario_callcenter.xml
%{_libdir}/opensips/modules/call_center.so
%doc docdir/README.call_center

%files carrierroute
%{_libdir}/opensips/modules/carrierroute.so
%doc docdir/README.carrierroute

%files cgrates
%{_libdir}/opensips/modules/cgrates.so
%doc docdir/README.cgrates

%files compression
%{_libdir}/opensips/modules/compression.so
%doc docdir/README.compression

%files cpl_c
%{_libdir}/opensips/modules/cpl_c.so
%doc docdir/README.cpl_c

%files db_berkeley
%{_sbindir}/bdb_recover
%{_libdir}/opensips/modules/db_berkeley.so
%dir %{_datadir}/opensips/db_berkeley
%dir %{_datadir}/opensips/db_berkeley/opensips
%{_datadir}/opensips/db_berkeley/opensips/*
%doc docdir/README.db_berkeley

%files db_http
%{_libdir}/opensips/modules/db_http.so
%doc docdir/README.db_http

%files db_mysql
%{_libdir}/opensips/modules/db_mysql.so
%dir %{_datadir}/opensips/mysql
%{_datadir}/opensips/mysql/*.sql
%doc docdir/README.db_mysql

%if 0%{?_with_oracle}
%files db_oracle
%{_sbindir}/opensips_orasel
%{_libdir}/opensips/modules/db_oracle.so
%dir %{_datadir}/opensips/oracle
%{_datadir}/opensips/oracle/*
%doc docdir/README.db_oracle
%endif

%files db_perlvdb
%dir %{perl_vendorlib}/OpenSIPS/VDB
%dir %{perl_vendorlib}/OpenSIPS/VDB/Adapter
%{_libdir}/opensips/modules/db_perlvdb.so
%{perl_vendorlib}/OpenSIPS/VDB.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/AccountingSIPtrace.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Alias.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Auth.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Describe.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/Speeddial.pm
%{perl_vendorlib}/OpenSIPS/VDB/Adapter/TableVersions.pm
%{perl_vendorlib}/OpenSIPS/VDB/Column.pm
%{perl_vendorlib}/OpenSIPS/VDB/Pair.pm
%{perl_vendorlib}/OpenSIPS/VDB/ReqCond.pm
%{perl_vendorlib}/OpenSIPS/VDB/Result.pm
%{perl_vendorlib}/OpenSIPS/VDB/VTab.pm
%{perl_vendorlib}/OpenSIPS/VDB/Value.pm
%doc docdir/README.db_perlvdb

%files db_postgresql
%{_libdir}/opensips/modules/db_postgres.so
%dir %{_datadir}/opensips/postgres
%{_datadir}/opensips/postgres/*.sql
%doc docdir/README.db_postgres

%files db_sqlite
%{_libdir}/opensips/modules/db_sqlite.so
%dir %{_datadir}/opensips/sqlite
%{_datadir}/opensips/sqlite/*.sql
%doc docdir/README.db_sqlite

%files db_unixodbc
%{_libdir}/opensips/modules/db_unixodbc.so
%doc docdir/README.db_unixodbc

%files emergency
%{_libdir}/opensips/modules/emergency.so
%doc docdir/README.emergency

%files event_rabbitmq
%{_libdir}/opensips/modules/event_rabbitmq.so
%doc docdir/README.event_rabbitmq

%files h350
%{_libdir}/opensips/modules/h350.so
%doc docdir/README.h350

%files httpd
%{_libdir}/opensips/modules/httpd.so
%doc docdir/README.httpd

%files identity
%{_libdir}/opensips/modules/identity.so
%doc docdir/README.identity

%files jabber
%{_libdir}/opensips/modules/jabber.so
%doc docdir/README.jabber

%files json
%{_libdir}/opensips/modules/json.so
%doc docdir/README.json

%files ldap
%{_libdir}/opensips/modules/ldap.so
%doc docdir/README.ldap

%files lua
%{_libdir}/opensips/modules/lua.so
%doc docdir/README.lua

%files mi_html
%{_libdir}/opensips/modules/mi_html.so
%doc docdir/README.mi_html

%files mi_http
%{_libdir}/opensips/modules/mi_http.so
%doc docdir/README.mi_http

%files mi_xmlrpc_ng
%{_libdir}/opensips/modules/mi_xmlrpc_ng.so
%doc docdir/README.mi_xmlrpc_ng

%files mmgeoip
%{_libdir}/opensips/modules/mmgeoip.so
%doc docdir/README.mmgeoip

%files peering
%{_libdir}/opensips/modules/peering.so
%doc docdir/README.peering

%files perl
%dir %{perl_vendorlib}/OpenSIPS
%dir %{perl_vendorlib}/OpenSIPS/LDAPUtils
%dir %{perl_vendorlib}/OpenSIPS/Utils
%{_libdir}/opensips/modules/perl.so
%{perl_vendorlib}/OpenSIPS.pm
%{perl_vendorlib}/OpenSIPS/Constants.pm
%{perl_vendorlib}/OpenSIPS/LDAPUtils/LDAPConf.pm
%{perl_vendorlib}/OpenSIPS/LDAPUtils/LDAPConnection.pm
%{perl_vendorlib}/OpenSIPS/Message.pm
%{perl_vendorlib}/OpenSIPS/Utils/PhoneNumbers.pm
%{perl_vendorlib}/OpenSIPS/Utils/Debug.pm
%doc docdir/README.perl

%files pi_http
%{_libdir}/opensips/modules/pi_http.so
%{_datadir}/opensips/pi_http/
%doc docdir/README.pi_http

%files presence
%{_libdir}/opensips/modules/presence.so
%doc docdir/README.presence

%files presence_callinfo
%{_libdir}/opensips/modules/presence_callinfo.so
%doc docdir/README.presence_callinfo

%files presence_dialoginfo
%{_libdir}/opensips/modules/presence_dialoginfo.so
%doc docdir/README.presence_dialoginfo

%files presence_mwi
%{_libdir}/opensips/modules/presence_mwi.so
%doc docdir/README.presence_mwi

%files presence_xcapdiff
%{_libdir}/opensips/modules/presence_xcapdiff.so

%files presence_xml
%{_libdir}/opensips/modules/presence_xml.so
%doc docdir/README.presence_xml

%files proto_sctp
%{_libdir}/opensips/modules/proto_sctp.so
%doc docdir/README.proto_sctp

%files proto_tls
%{_libdir}/opensips/modules/proto_tls.so
%doc docdir/README.proto_tls

%files proto_wss
%{_libdir}/opensips/modules/proto_wss.so
%doc docdir/README.proto_wss

%files pua
%{_libdir}/opensips/modules/pua.so
%doc docdir/README.pua

%files pua_bla
%{_libdir}/opensips/modules/pua_bla.so
%doc docdir/README.pua_bla

%files pua_dialoginfo
%{_libdir}/opensips/modules/pua_dialoginfo.so
%doc docdir/README.pua_dialoginfo

%files pua_mi
%{_libdir}/opensips/modules/pua_mi.so
%doc docdir/README.pua_mi

%files pua_usrloc
%{_libdir}/opensips/modules/pua_usrloc.so
%doc docdir/README.pua_usrloc

%files pua_xmpp
%{_libdir}/opensips/modules/pua_xmpp.so
%doc docdir/README.pua_xmpp

# FIXME disable python2 until upstream adds support for Py3
#%files -n python2-opensips
#%{_libdir}/opensips/modules/python.so

%files rabbitmq
%{_libdir}/opensips/modules/rabbitmq.so
%doc docdir/README.rabbitmq

%files rabbitmq_consumer
%{_libdir}/opensips/modules/rabbitmq_consumer.so
%doc docdir/README.rabbitmq_consumer

%files regex
%{_libdir}/opensips/modules/regex.so
%doc docdir/README.regex

%files rest_client
%{_libdir}/opensips/modules/rest_client.so
%doc docdir/README.rest_client

%files rls
%{_libdir}/opensips/modules/rls.so
%doc docdir/README.rls

%files seas
%{_libdir}/opensips/modules/seas.so
%doc docdir/README.seas

%files siprec
%{_libdir}/opensips/modules/siprec.so
%doc docdir/README.siprec

%files sms
%{_libdir}/opensips/modules/sms.so
%doc docdir/README.sms

%files snmpstats
%{_libdir}/opensips/modules/snmpstats.so
%doc docdir/README.snmpstats
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/OPENSER-MIB
%{_datadir}/snmp/mibs/OPENSER-REG-MIB
%{_datadir}/snmp/mibs/OPENSER-SIP-COMMON-MIB
%{_datadir}/snmp/mibs/OPENSER-SIP-SERVER-MIB
%{_datadir}/snmp/mibs/OPENSER-TC

%files tls_mgm
%{_libdir}/opensips/modules/tls_mgm.so
%doc docdir/README.tls_mgm

%files xcap
%{_libdir}/opensips/modules/xcap.so
%doc docdir/README.xcap

%files xcap_client
%{_libdir}/opensips/modules/xcap_client.so
%doc docdir/README.xcap_client

%files xml
%{_libdir}/opensips/modules/xml.so
%doc docdir/README.xml

%files xmpp
%{_libdir}/opensips/modules/xmpp.so
%doc docdir/README.xmpp


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.2-7
- Perl 5.32 rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 3.0.2-6
- Rebuild (json-c)

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 3.0.2-5
- Add patch for upcoming json-c 0.14.0

* Tue Feb 11 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.0.2-4
- Improve building with GCC 10 again

* Sun Feb  9 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.0.2-3
- Improve building with GCC 10

* Thu Feb  6 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.0.2-2
- Fix building with GCC 10

* Tue Jan 28 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.0.2-1
- Ver. 3.0.2
- Removed patch #5 (opensips-0005-Use-additional-auth-field-Sip-Source-IP-Address.patch).
  Use $acc_extra variable instead.

* Thu Nov 28 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.0.1-1
- Ver. 3.0.1
- Module mi_json was renamed to mi_http
- Module siptrace was renamed to tracer
- Module uri was removed
- New module - mi_html
- New module - proto_smpp
- New module - rabbitmq_consumer
- Opensipsctl/dbctl scripts were removed in favour of https://github.com/OpenSIPS/opensips-cli

* Thu Sep 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.4.6-5
- Remove python2 script (dbtextdb auxiliary module)

* Wed Sep 11 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.4.6-4
- Disable python2 module

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Petr Pisar <ppisar@redhat.com> - 2.4.6-2
- Fix obsoleting opensips-cpl-c (bug #1721570)

* Thu Jun 13 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.4.6-1
- Ver. 2.4.6

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.5-2
- Perl 5.30 rebuild

* Mon Mar 11 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.4.5-1
- Ver. 2.4.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.4.4-1
- Ver. 2.4.4

* Sun Dec 02 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.4.3-1
- Ver. 2.4.3
- Removed unused BR: lm_sensors-devel, subversion
- Added modules: event_jsonrpc, freeswitch_scripting, jsonrpc, siprec

* Tue Nov 20 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.3.6-1
- Ver. 2.3.6

* Thu Sep 20 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.3.5-1
- Ver. 2.3.5

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 2.3.4-4
- Rebuild for new net-snmp

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.4-2
- Perl 5.28 rebuild

* Fri Jun 15 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.3.4-1
- Ver. 2.3.4

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 2.3.3-3
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.3.3-2
- Enabled modules - cachedb_couchbase, cachedb_mongodb

* Thu Feb 22 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.3.3-1
- Ver. 2.3.3
- Enabled module - lua
- New modules - cgrates, event_routing, freeswitch, mid_registrar, rabbitmq,
  sip_i, xml

* Tue Feb 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.2.6-1
- Ver. 2.2.6

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.5-6
- Rebuilt for switch to libxcrypt

* Tue Dec 12 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.5-5
- Updated patch for json-c v0.13 with final upstream version

* Mon Dec 11 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.5-4
- Updated patch for json-c v0.13 with upstreamed version

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.5-3
- Rebuilt for libjson-c.so.3

* Tue Nov 21 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.2.5-2
- Backport few more patches
- Fix building with MariaDB in F-27

* Wed Oct 04 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.2.5-1
- Ver. 2.2.5

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.3-11
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.3-10
- Python 2 binary package renamed to python2-opensips
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.3-9
- Rebuilt after RPM update (№ 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.3-8
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.3-7
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Adam Williamson <awilliam@redhat.com> - 2.2.3-4
- Rebuild against MariaDB 10.2

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.3-3
- Perl 5.26 rebuild

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.2.3-2
- libconfuse rebuild.

* Thu Mar  9 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.2.3-1
- Ver. 2.2.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.2-3
- Rebuild for xmlrpc-c

* Fri Jan 13 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.2.2-2
- Don't modify/override CFLAGS

* Wed Nov 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.2.2-1
- Ver. 2.2.2

* Thu Oct 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.11.9-1
- Ver. 1.11.9

* Tue Sep  6 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.11.8-1
- Ver. 1.11.8
- Switch to freeradius-client from radiusclient-ng
- Remove ifdefs for el6 - we're not going to upgrade it in EPEL6.

* Wed Jun 15 2016 Jon Ciesla <limburgher@gmail.com> - 1.11.6-4
- libconfuse rebuild.

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.11.6-3
- Perl 5.24 rebuild

* Sat Feb 27 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.11.6-2
- Fixed incompatibility with latest Perl

* Sun Feb 21 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.11.6-1
- Ver. 1.11.6
- Removed compatibility with EPEL5
- New module - b2b_sca
- New module - call_center
- New module - mi_json
- New module - rtpengine (experimental!)
- New module - script_helper

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> -  1.10.5-8
- Rebuild for libmicrohttpd.so.12.

* Thu Nov 05 2015 Kalev Lember <klember@redhat.com> - 1.10.5-7
- Rebuilt for libmicrohttpd soname bump

* Tue Sep 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.10.5-6
- rebuild (hiredis)

* Wed Jul 29 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.10.5-5
- Rebuilt for rpm 4.12.90

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Peter Lemenkov <lemenkov@gmail.com> - 1.10.5-3
- Fix building on EPEL6

* Fri Jun 12 2015 Peter Lemenkov <lemenkov@gmail.com> - 1.10.5-2
- Install missing script (required for a systemd service). See rhbz #1019014.

* Fri Jun 12 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.10.5-1
- Update to upstream.
- Added -fgnu89-inline parameter to fix builds for inline functions.
- Removed broken and obsolete patches.

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.4-2
- Perl 5.22 rebuild

* Sat May  2 2015 Peter Lemenkov <lemenkov@gmail.com> - 1.10.4-1
- Ver. 1.10.4
- Dropped EL5 compatibility

* Tue Apr 21 2015 Remi Collet <remi@fedoraproject.org> - 1.10.3-2
- rebuild for new librabbitmq

* Mon Nov 03 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.10.3-1
- Ver. 1.10.3
- Fixed FTBFS in F22 (see rhbz #1124390)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.1-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.10.1-1
- Ver. 1.10.1
- Link mi_xmlrpc against -lpthread
- Enable snmpstats on EL6

* Thu Mar 06 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.10.0-3
- Fix missing directory on EL6

* Tue Oct 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.10.0-2
- Run as opensips user even in EL6
- Unconditionally add another one auth field (SIP IP address)

* Wed Sep 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.10.0-1
- Ver. 1.10.0
- Drop support for Fedora 17 and earlier (still maintain support for EL5)
- New external module - rest_client
- New external module - xmlrpc_ng (contains mi_xmlrpc_ng)
- New internal module - db_cachedb
- New internal module - mathops
- Disabled new external module - sngtc (requires a proprietary library)

* Fri Sep 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.9.1-2
- Proper directory for storing tmpfile

* Tue Aug 20 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.9.1-1
- Ver. 1.9.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.8.2-7
- Perl 5.18 rebuild

* Wed Mar 13 2013 Remi Collet <remi@fedoraproject.org> - 1.8.2-6
- rebuild for new librabbitmq

* Mon Mar  4 2013 Thomas Spura <tomspur@fedoraproject.org> - 1.8.2-5
- Fix Berk(e)ley typo in summary

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.8.2-3
- Revert systemd macros

* Thu Jan 10 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.8.2-2
- Allow rtpproxy module to accept avps
- Few bugfixes

* Tue Nov 06 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.8.2-1
- Ver. 1.8.2 (Bugfix release)

* Sat Sep 22 2012  Remi Collet <remi@fedoraproject.org> - 1.8.1-3
- rebuild against libmemcached.so.11 without SASL

* Fri Aug 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.8.1-2
- Enabled json module
- Enabled xmlrpc module
- Enabled cachedb_memcached module on EL5, EL6
- Enabled cachedb_redis module on EL6

* Wed Aug 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.8.1-1
- Ver. 1.8.1
- Dropped all upstreamed patches

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 1.8.0-2
- Perl 5.16 rebuild

* Tue Jul 03 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.8.0-1
- update to 1.8.0

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.7.2-8
- Perl 5.16 rebuild

* Sat May 12 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.2-7
- Change %%define to %%global

* Sat May 12 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.2-6
- Added missing docs

* Fri May 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.2-5
- Fixed conditional building with Oracle DB

* Sat Apr 28 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.2-4
- Fixes for systemd unit

* Sun Apr 22 2012  Remi Collet <remi@fedoraproject.org> - 1.7.2-3
- rebuild against libmemcached.so.10

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.2-2
- Fix building on EPEL

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.2-1
- update to 1.7.2 (bugfix release).
- enable systemd support where possible

* Fri Apr 13 2012 Jindrich Novy <jnovy@redhat.com> - 1.7.1-6
- rebuild against new librpm and libdb

* Sat Mar 03 2012  Remi Collet <remi@fedoraproject.org> - 1.7.1-5
- rebuild against libmemcached.so.9

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.7.1-4
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 01 2011 John Khvatov <ivaxer@fedoraproject.org> - 1.7.1-2
- upstream tarball rebuild

* Thu Nov 24 2011 John Khvatov <ivaxer@fedoraproject.org> - 1.7.1-1
- update to 1.7.1 (bugfix release).

* Mon Nov 07 2011 John Khvatov <ivaxer@fedoraproject.org> - 1.7.0-1
- update to 1.7.0
- dropped upstreamed patches
- added new modules: event_datagram and python
- removed lcr module

* Sat Sep 17 2011  Remi Collet <remi@fedoraproject.org> - 1.6.4-13
- rebuild against libmemcached.so.8

* Mon Aug 22 2011 John Khvatov <ivaxer@fedoraproject.org> - 1.6.4-12
- rebuild against new libnetsnmp

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.6.4-11
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.6.4-10
- Perl mass rebuild

* Mon Jul 11 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.6.4-9
- Updated init-script

* Mon Jul 11 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.6.4-8
- Upstream re-released traball with several new patches (API compatible)

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6.4-7
- Perl mass rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.6.4-6
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 John Khvatov <ivaxer@fedoraproject.org> - 1.6.4-1
- dropped upstreamed patch (opensips-build.patch)
- update to 1.6.4
- added new module: presence_callinfo

* Sat Oct 30 2010 John Khvatov <ivaxer@fedoraproject.org> - 1.6.3-4
- rebuild against new libnetsnmp

* Wed Oct 06 2010 Remi Collet <fedora@famillecollet.com> - 1.6.3-3
- rebuilt against new libmemcached

* Wed Sep 08 2010 Dan Horák <dan[at]danny.cz> - 1.6.3-2
- fix a build issue

* Thu Aug 12 2010 John Khvatov <ivaxer@gmail.com> - 1.6.3-1
- update to 1.6.3

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1.6.2-5
- recompiling .py files against Python 2.7 (rhbz#623343)

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.6.2-4
- Mass rebuild with perl-5.12.0

* Wed May 05 2010 Remi Collet <fedora@famillecollet.com> - 1.6.2-3
- rebuilt against new libmemcached

* Thu Apr 15 2010 John Khvatov <ivaxer@fedoraproject.org> - 1.6.2-2
- Disabled build of the memcached subpackage for EPEL

* Thu Apr 15 2010 John Khvatov <ivaxer@fedoraproject.org> - 1.6.2-1
- Updated to 1.6.2

* Sun Feb 07 2010 Remi Collet <fedora@famillecollet.com> - 1.6.1-2
- rebuilt against new libmemcached

* Tue Dec 22 2009 John Khvatov <ivaxer@fedoraproject.org> - 1.6.1-1
- Updated to 1.6.1
- Dropped upstreamed patches

* Wed Nov 04 2009 John Khvatov <ivaxer@fedoraproject.org> - 1.6.0-4
- Fixed typo: pia_mi to pua_mi in presence_xcapdiff dependencies

* Tue Nov 03 2009 John Khvatov <ivaxer@fedoraproject.org> - 1.6.0-3
- Added patch for compatibility with new openssl

* Thu Oct 29 2009 John Khvatov <ivaxer@fedoraproject.org> - 1.6.0-2
- Added patch for init script to fix malformed comment block
- Added COPYING file
- Fixed not-capitalized summory of memcached subpackage

* Mon Oct 19 2009 John Khvatov <ivaxer@fedoraproject.org> - 1.6.0-1
- Created new package from openser package
- Upgrade to OpenSIPS 1.6
- New modules
- Added osipconsole tool

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.4-8
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.4-6
- allow build of this package on fedora<=10

* Sat Feb 28 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.4-5
- fix module path

* Sat Feb 28 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.4-3
- addedd subversion build dependency to avoid svnversion error messages
- fixed installation of perl modules in rawhide

* Fri Jan 23 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.3.4-2
- Rebuild for new mysql.

* Mon Dec  8 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.4-1
- Ver. 1.3.4
- Added sysconfig-file

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.3-3
- Include lots of unowned directories.

* Thu Aug 28 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.3-2
- Removed dialplan and drouting modules from upstream

* Thu Aug 28 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.3-1
- Ver. 1.3.3
- Dropped upstreamed patch

* Mon Aug 11 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.2-5
- Typo fix

* Mon Aug 11 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.2-4
- Fix build with --fuzz=0

* Mon Aug 11 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.2-3
- Fixed urls
- Restricted access to openser.cfg and openserctl.cfg
- Service won't start by default (BZ# 441297)

* Fri May 16 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.2-2
- New modules - dialplan and drouting (this one still has no README)

* Thu May 15 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.2-1
- Ver. 1.3.2

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.1-3
- add Requires for versioned perl (libperl.so)
- drop silly file Requires

* Fri Mar 14 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.1-2
- removed perl patch, which is not necessary

* Thu Mar 13 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.1-1
- update to upstream
- removed obsolete patches

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.0-12
- patch perl code to use PERL_SYS_INIT3_BODY

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.0-11
- fix perl build requires

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.0-10
- Rebuild for new perl

* Sat Feb 23 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.3.0-9
- ia64 build fix

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-8.1
- typo fix

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-8
- Rebuild for GCC 4.3

* Sat Jan 26 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.3.0-7
- Updated syntax error in default config

* Sat Jan 26 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-5
- Merge of acc module into main package

* Fri Jan 25 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.3.0-4
- modify and apply forgotten patch4

* Thu Jan 17 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.3.0-2
- removed openser.init and replaced by upstream version
- fixed configuration path for openserdbctl (#428799)

* Sun Jan 13 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-1.4
- 4th try to remove lm_sensors-devel from EL-[45] at ppc{64}

* Thu Dec 13 2007 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-1
- Final ver. 1.3.0
- Removed some leftovers from spec-file

* Wed Dec 12 2007 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-0.1.pre1
- Latest snapshot - 1.3.0pre1

* Mon Dec 10 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.2.2-11
- added ETCDIR into openserctlrc (need openser-1.3 to work)

* Mon Sep 24 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.2.2-10
- perl scripts moved to perl_vendorlib directory
- added LDAPUtils and Utils subdirectories
- changed perl module BuildRequires

* Mon Sep 24 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.2.2-9
- added reload section to init script
- init script specified with initrddir macro
- documentation converted to UTF-8
- added doc macro for documentation
- documentation moved do proper place (/usr/share/doc/NAME-VERSION/)
- which removed from BuildRequires, it's in guidelines exceptions
- unixodbc subpackage summary update

* Thu Sep  6 2007 Peter Lemenkov <lemenkov@gmail.com> 1.2.2-8
- Added another one missing BR - which (needs by snmpstats module)
- Cosmetic: dropped commented out 'Requires'

* Thu Sep 06 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.2.2-7
- added attr macro for init script
- added -p to install arguments to preserve timestamp
- parallel make used

* Sun Aug 26 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.2.2-6
- Fedora Core 6 build updates
- changed attributes for openser.init to be rpmlint more silent

* Sun Aug 26 2007 Peter Lemenkov <lemenkov@gmail.com> 1.2.2-5
- fixed paths for openssl libs and includes

* Sun Aug 26 2007 Peter Lemenkov <lemenkov@gmail.com> 1.2.2-4
- Introduced acc and acc_radius modules (Jan Ondrej)
- Dropped radius_accounting condition

* Sat Aug 25 2007 Peter Lemenkov <lemenkov@gmail.com> 1.2.2-3
- Changed license according to Fedora's policy
- Make rpmlint more silent

* Fri Aug 24 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.2.2-2
- added openser.init script
- removed Patch0: openser--Makefile.diff and updated build section
- spec file is 80 characters wide
- added radius_accounting condition

* Wed Aug 22 2007 Peter Lemenkov <lemenkov@gmail.com> 1.2.2-1
- Ver. 1.2.2

* Tue Jul 24 2007 Peter Lemenkov <lemenkov@gmail.com> 1.2.1-1
- Initial spec.
