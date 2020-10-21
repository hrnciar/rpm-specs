# Generated by go2rpm
%bcond_without check

# https://github.com/Shopify/sarama
%global goipath         github.com/Shopify/sarama
Version:                1.27.0

%gometa

%global common_description %{expand:
Sarama is an MIT-licensed Go client library for Apache Kafka version 0.8 (and later).}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for Apache Kafka 0.8, and up

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/eapache/go-resiliency/breaker)
BuildRequires:  golang(github.com/eapache/go-xerial-snappy)
BuildRequires:  golang(github.com/eapache/queue)
BuildRequires:  golang(github.com/jcmturner/gofork/encoding/asn1)
BuildRequires:  golang(github.com/klauspost/compress/zstd)
BuildRequires:  golang(github.com/pierrec/lz4)
BuildRequires:  golang(github.com/rcrowley/go-metrics)
BuildRequires:  golang(github.com/xdg/scram)
BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/asn1tools)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/client)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/config)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/credentials)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/gssapi)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/iana/chksumtype)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/iana/keyusage)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/keytab)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/messages)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/types)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/fortytw2/leaktest)
BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/krberror)
# kerberos_client_test.go
# BuildRequires:  golang(gopkg.in/jcmturner/gokrb5.v7/test/testdata)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in tools/kafka-console-consumer tools/kafka-console-partitionconsumer tools/kafka-console-producer tools/kafka-producer-performance; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# fails because gopkg.in/jcmturner/gokrb5.v7/test/testdata is not packaged
rm -rf kerberos_client_test.go
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Sep 17 22:37:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.27.0-1
- Update to 1.27.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.22.0-2
- Add Obsoletes for old names

* Tue Apr 23 18:29:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.22.0-1
- Release 1.22.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.9.git87ec8d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-0.8.git87ec8d7
- Disable tests
  resolves: #1555780

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.7.git87ec8d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.6.git87ec8d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.5.git87ec8d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.4.git87ec8d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.3.git87ec8d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-0.2.git87ec8d7
- https://fedoraproject.org/wiki/Changes/golang1.7

* Fri Apr 15 2016 jchaloup <jchaloup@redhat.com> - 1.7.0-0.1.git87ec8d7
- First package for Fedora
  resolves: #1327762
