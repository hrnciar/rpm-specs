# Generated by go2rpm
%bcond_without check

# https://github.com/lucas-clemente/quic-go
%global goipath         github.com/lucas-clemente/quic-go
Version:                0.11.1

%gometa

%global common_description %{expand:
Quic-go is an implementation of the QUIC protocol in Go. It roughly implements
the IETF QUIC draft, although we don't fully support any of the draft versions
at the moment.}

%global golicenses      LICENSE
%global godocs          docs example Changelog.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        QUIC implementation in pure go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cheekybits/genny/generic)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/marten-seemann/qtls)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(golang.org/x/crypto/hkdf)
BuildRequires:  golang(golang.org/x/net/http/httpguts)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/hpack)
BuildRequires:  golang(golang.org/x/net/idna)

%if %{with check}
# Tests
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 18:51:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.1-1
- Initial package
