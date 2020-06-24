# Generated by go2rpm
%bcond_without check

# https://github.com/containernetworking/cni
%global goipath         github.com/containernetworking/cni
Version:                0.7.0

%gometa

%global common_description %{expand:
CNI (Container Network Interface), a Cloud Native Computing Foundation project,
consists of a specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number of supported
plugins. CNI concerns itself only with network connectivity of containers and
removing allocated resources when the container is deleted. Because of this
focus, CNI has a wide range of support and the specification is simple to
implement.}

%global golicenses      LICENSE
%global godocs          CODE-OF-CONDUCT.md CONTRIBUTING.md CONVENTIONS.md\\\
                        GOVERNANCE.md README.md RELEASING.md ROADMAP.md\\\
                        SPEC.md Documentation

Name:           %{goname}
Release:        3%{?dist}
Summary:        Container Network Interface - networking for Linux containers

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/ginkgo/extensions/table)
BuildRequires:  golang(github.com/onsi/gomega)
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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 23:22:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Initial package
