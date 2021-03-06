# Generated by go2rpm 1
%bcond_without check

# https://github.com/kubernetes/system-validators
%global goipath         k8s.io/system-validators
%global forgeurl        https://github.com/kubernetes/system-validators
Version:                1.2.0

%gometa

%global common_description %{expand:
A set of system-oriented validators for kubeadm preflight checks.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md RELEASE.md code-of-\\\
                        conduct.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A set of system-oriented validators for kubeadm preflight checks

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/blang/semver)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(golang.org/x/sys/unix)

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
* Tue Sep 29 18:18:58 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Initial package
