# Generated by go2rpm 1
%bcond_without check

# https://github.com/jsonnet-bundler/jsonnet-bundler
%global goipath         github.com/jsonnet-bundler/jsonnet-bundler
Version:                0.4.0

%gometa

%global common_description %{expand:
A jsonnet package manager.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A jsonnet package manager

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

Requires:       git

%description
%{common_description}

%gopkg

%prep
%goprep

%build
export LDFLAGS="-X main.Version=%{version} "
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu May 21 2020 Olivier Lemasle <o.lemasle@gmail.com> - 0.4.0-1
- Update to 0.4.0 (#1836659)

* Sun Mar 29 2020 Olivier Lemasle <o.lemasle@gmail.com> - 0.3.1-2
- Add Requires: git

* Fri Mar 06 12:18:47 CET 2020 Olivier Lemasle <o.lemasle@gmail.com> - 0.3.1-1
- Initial package

