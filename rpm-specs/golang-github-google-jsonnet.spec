# Generated by go2rpm 1
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/google/go-jsonnet
%global goipath         github.com/google/go-jsonnet
Version:                0.15.0

%gometa

%global common_description %{expand:
This an implementation of Jsonnet in pure Go. It is feature complete but is not
as heavily exercised as the Jsonnet C++ implementation. Please try it out and
give feedback.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Implementation of Jsonnet in pure Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}
# Prevent int overflow
# https://github.com/google/go-jsonnet/pull/377
Patch0:         0001-Prevent-int-overflow.patch

BuildRequires:  golang(github.com/fatih/color)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%build
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
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Feb 01 00:48:04 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.15.0-1
- Initial package
