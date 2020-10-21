# Generated by go2rpm 1
%bcond_without check

# https://github.com/jcmturner/dnsutils
%global goipath         gopkg.in/jcmturner/dnsutils.v1
%global forgeurl        https://github.com/jcmturner/dnsutils
Version:                1.0.1

%gometa

%global common_description %{expand:
DNS utilities for Go.}

%global golicenses      LICENSE

Name:           %{goname}
Release:        2%{?dist}
Summary:        DNS utilities for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 20:42:49 EST 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Initial package
