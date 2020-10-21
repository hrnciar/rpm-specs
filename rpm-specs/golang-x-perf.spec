# Generated by go2rpm
%bcond_without check

# https://github.com/golang/perf
%global goipath         golang.org/x/perf
%global forgeurl        https://github.com/golang/perf
%global commit          9c9101da83161dff5e53fc89bf35ed49ea286db8

%gometa

%global common_description %{expand:
This package holds the source for various tools related to performance
measurement, storage, and analysis.

 - cmd/benchstat contains a command-line tool that computes and 7
 compares statistics about benchmarks.
 - cmd/benchsave contains a command-line tool for publishing benchmark
 results.
 - storage contains the https://perfdata.golang.org/ benchmark result
 storage system.
 - analysis contains the https://perf.golang.org/ benchmark result analysis
 system.}

%global golicenses      LICENSE PATENTS
%global godocs          AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

Name:           %{goname}
Version:        0
Release:        0.9%{?dist}
Summary:        Performance measurement, storage, and analysis

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/storage)
BuildRequires:  golang(github.com/aclements/go-gg/generic/slice)
BuildRequires:  golang(github.com/aclements/go-gg/ggstat)
BuildRequires:  golang(github.com/aclements/go-gg/table)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(google.golang.org/api/oauth2/v2)
BuildRequires:  golang(google.golang.org/appengine)
BuildRequires:  golang(google.golang.org/appengine/log)
BuildRequires:  golang(google.golang.org/appengine/user)

%description
%{common_description}

%gopkg

%prep
%goprep

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
%license LICENSE PATENTS
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Aug 07 20:50:42 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20200807git9c9101d
- Bump to commit 9c9101da83161dff5e53fc89bf35ed49ea286db8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 21:40:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20190516git6835260
- Bump to commit 6835260b7148966b8510e0165e066287164de4cb

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git2ce0818
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3-20180422git2ce0818
- Disable a test that fails on s390x

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git2ce0818
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180422git2ce0818
- First package for Fedora
