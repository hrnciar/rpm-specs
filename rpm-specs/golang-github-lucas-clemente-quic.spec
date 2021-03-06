# Generated by go2rpm
%bcond_without check

# https://github.com/lucas-clemente/quic-go
%global goipath         github.com/lucas-clemente/quic-go
Version:                0.18.0

%gometa

%global common_description %{expand:
Quic-go is an implementation of the QUIC protocol in Go. It roughly implements
the IETF QUIC draft, although we don't fully support any of the draft versions
at the moment.}

%global golicenses      LICENSE
%global godocs          docs example Changelog.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        QUIC implementation in pure go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cheekybits/genny/generic)
BuildRequires:  golang(github.com/francoispqt/gojay)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/marten-seemann/qpack)
BuildRequires:  golang(github.com/marten-seemann/qtls-go1-15)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(golang.org/x/crypto/chacha20)
BuildRequires:  golang(golang.org/x/crypto/hkdf)
BuildRequires:  golang(golang.org/x/net/http/httpguts)
BuildRequires:  golang(golang.org/x/net/http2/hpack)
BuildRequires:  golang(golang.org/x/net/idna)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/onsi/gomega/gbytes)
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
* Sun Aug 23 21:30:18 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 00:03:54 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.2-1
- Update to 0.17.2 (#1803692, #1742501)

* Wed Feb 12 23:43:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.3-1.20200213gitdd035c2
- Update to 0.14.3, commit dd035c2f12fcfe656333a419a18a930af351a268

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 18:51:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.1-1
- Initial package
