# Generated by go2rpm
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/grpc-ecosystem/go-grpc-prometheus
%global goipath         github.com/grpc-ecosystem/go-grpc-prometheus
Version:                1.2.0
%global commit          9abf3eb82b4a313b1a28f370a7ef8ffe0667c681

%gometa

%global common_description %{expand:
Prometheus monitoring for your gRPC Go servers and clients.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Prometheus monitoring for your gRPC Go servers and clients

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/testutil)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 18:05:02 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-6.20200727git9abf3eb
- Bump to commit 9abf3eb82b4a313b1a28f370a7ef8ffe0667c681

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-3.20190624gitae0d866
- Add Obsoletes for old name

* Mon Jun 24 21:41:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-2.20190624gitae0d866
- Bump to commit ae0d8660c5f2108ca70a3776dbe0fb53cf79f1da

* Sat Apr 27 17:25:03 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Release 1.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.8.20161111git6b7015e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.1-0.7.20161111git6b7015e
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.5.20161111git6b7015e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1-0.5.20161111git6b7015e
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.4.git6b7015e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.3.git6b7015e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.2.git6b7015e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1-0.1.git6b7015e
- First package for Fedora
  resolves: #1433121
