# Generated by go2rpm
%bcond_without check

# https://github.com/rsc/letsencrypt
%global goipath         rsc.io/letsencrypt
%global forgeurl        https://github.com/rsc/letsencrypt
Version:                0.0.1

%gometa

%global common_description %{expand:
Package Letsencrypt obtains TLS certificates from LetsEncrypt.org.}

%global golicenses      LICENSE
%global godocs          README

%global gosupfiles      "${vendor[@]}"

Name:           %{goname}
Release:        3%{?dist}
Summary:        Manage tls certificates automatically via letsencrypt.org

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

# We use vendored version as letsencrypt depends on lego v1
# v1 can't easily be packaged as it also depends on old libraries
# the vendored version is also customised
# BuildRequires:  golang(github.com/xenolf/lego/acme)
# BuildRequires:  golang(golang.org/x/net/context)
# BuildRequires:  golang(golang.org/x/time/rate)

%description
%{common_description}

%gopkg

%prep
%goprep -k

%install
mapfile -t vendor <<< $(find vendor -type f)
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 16:32:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- Initial package
