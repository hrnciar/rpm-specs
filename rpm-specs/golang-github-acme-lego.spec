# Generated by go2rpm
%bcond_without check

# https://github.com/go-acme/lego
%global goipath         github.com/go-acme/lego
Version:                3.5.0

%gometa

%global goaltipaths     github.com/xenolf/lego

%global common_description %{expand:
Let's Encrypt client and ACME library written in Go.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Let's Encrypt client and ACME library written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(github.com/akamai/AkamaiOPEN-edgegrid-golang/configdns-v1)
BuildRequires:  golang(github.com/akamai/AkamaiOPEN-edgegrid-golang/edgegrid)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/alidns)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/client)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/lightsail)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/route53)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/services/dns/mgmt/2017-09-01/dns)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure/auth)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/to)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/cloudflare/cloudflare-go)
BuildRequires:  golang(github.com/cpu/goacmedns)
BuildRequires:  golang(github.com/dnsimple/dnsimple-go/dnsimple)
BuildRequires:  golang(github.com/exoscale/egoscale)
BuildRequires:  golang(github.com/gophercloud/gophercloud)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack/dns/v2/recordsets)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack/dns/v2/zones)
BuildRequires:  golang(github.com/iij/doapi)
BuildRequires:  golang(github.com/iij/doapi/protocol)
BuildRequires:  golang(github.com/labbsr0x/bindman-dns-webhook/src/client)
BuildRequires:  golang(github.com/linode/linodego)
BuildRequires:  golang(github.com/liquidweb/liquidweb-go/client)
BuildRequires:  golang(github.com/liquidweb/liquidweb-go/network)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/namedotcom/go/namecom)
BuildRequires:  golang(github.com/nrdcg/auroradns)
BuildRequires:  golang(github.com/nrdcg/dnspod-go)
BuildRequires:  golang(github.com/nrdcg/goinwx)
BuildRequires:  golang(github.com/nrdcg/namesilo)
BuildRequires:  golang(github.com/OpenDNS/vegadns2client)
BuildRequires:  golang(github.com/oracle/oci-go-sdk/common)
BuildRequires:  golang(github.com/oracle/oci-go-sdk/dns)
BuildRequires:  golang(github.com/ovh/go-ovh/ovh)
BuildRequires:  golang(github.com/rainycape/memcache)
BuildRequires:  golang(github.com/sacloud/libsacloud/api)
BuildRequires:  golang(github.com/sacloud/libsacloud/sacloud)
BuildRequires:  golang(github.com/timewasted/linode/dns)
BuildRequires:  golang(github.com/transip/gotransip)
BuildRequires:  golang(github.com/transip/gotransip/domain)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(github.com/vultr/govultr)
BuildRequires:  golang(golang.org/x/crypto/ocsp)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/idna)
BuildRequires:  golang(golang.org/x/net/publicsuffix)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/clientcredentials)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(google.golang.org/api/dns/v1)
BuildRequires:  golang(google.golang.org/api/googleapi)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(gopkg.in/ns1/ns1-go.v2/rest)
BuildRequires:  golang(gopkg.in/ns1/ns1-go.v2/rest/model/dns)
BuildRequires:  golang(gopkg.in/square/go-jose.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(github.com/timewasted/linode)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|github.com/cenkalti/backoff/v4|github.com/cenkalti/backoff|" "{}" +;

%build
%gobuild -o %{gobuilddir}/bin/lego %{goipath}/cmd/lego

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# Needs network
%gocheck -d challenge/dns01 \
         -t providers/dns
%endif

%files
%license LICENSE
%doc docs CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Apr 02 18:22:42 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Carl George <carl@george.computer> - 2.7.2-1
- Latest upstream v2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 16:35:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.5.0-1
- Initial package
