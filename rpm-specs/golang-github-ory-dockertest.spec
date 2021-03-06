# Generated by go2rpm 1
%bcond_without check
# Checks need a running Docker instance
%bcond_with docker

# https://github.com/ory/dockertest
%global gourl           https://github.com/ory/dockertest
%global goipath         github.com/ory/dockertest
Version:                3.6.0

%gometa

%global common_description %{expand:
Use Docker to run your Go language integration tests against third party
services.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md SECURITY.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Support for ephermal Docker images for Go tests

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gotest.tools)
BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/user)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/containerd/continuity)
BuildRequires:  golang(github.com/Azure/go-ansiterm)
BuildRequires:  golang(github.com/Nvveen/Gotty)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check} && %{with docker}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
find . -type f -name "*.go" -exec sed -i "s|github.com/cenkalti/backoff/v3|github.com/cenkalti/backoff|" "{}" +;

%install
%gopkginstall

%if %{with check} && %{with docker}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.6.0-1
- Fix license (rhbz#1822469)
- Update to latest upstream release 3.6.0

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.5.5-1
- Initial package
