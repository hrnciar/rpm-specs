%bcond_without check

%global goipath         github.com/caddyserver/dnsproviders
Version:                0.3.0

%gometa

%global common_description %{expand:
Caddy supports solving the ACME DNS challenge. This challenge is unique because
the server that is requesting a TLS certificate does not need to start a
listener and be accessible from external networks. This quality is essential
when behind load balancers or in other advanced networking scenarios.

The DNS challenge sets a DNS record and the ACME server verifies its
correctness in order to issue the certificate. Caddy can do this for you
automatically, but it needs credentials to your DNS provider to do so. Since
every DNS provider is different, we have these adapters you can plug into Caddy
in order to complete this challenge.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        DNS providers for Caddy to solve the ACME DNS challenge
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/caddyserver/dnsproviders/pull/78
Patch0:         fix-typo-in-stackpath-test.patch

BuildRequires:  golang(github.com/caddyserver/caddy/caddytls)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/acmedns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/alidns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/auroradns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/azure)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/cloudflare)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/cloudxns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/conoha)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/digitalocean)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/dnsimple)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/dnsmadeeasy)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/dnspod)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/duckdns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/dyn)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/exec)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/exoscale)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/fastdns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/gandi)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/gandiv5)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/gcloud)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/glesys)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/godaddy)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/httpreq)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/inwx)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/lightsail)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/linode)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/linodev4)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/namecheap)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/namedotcom)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/namesilo)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/nifcloud)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/ns1)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/otc)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/ovh)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/pdns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/rackspace)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/rfc2136)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/route53)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/selectel)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/stackpath)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/transip)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/vscale)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/vultr)

%description %{common_description}

%gopkg

%prep
%goprep
%patch0 -p 1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Carl George <carl@george.computer> - 0.3.0-1
- Initial package rhbz#1747855
