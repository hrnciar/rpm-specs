# Generated by go2rpm
# Testing requires modules to be on
%bcond_with check

# https://github.com/DATA-DOG/godog
%global goipath         github.com/DATA-DOG/godog
Version:                0.7.13

%gometa

%global common_description %{expand:
Package Godog is the official Cucumber BDD framework for Golang, it merges
specification and test documentation into one cohesive whole.}

%global golicenses      LICENSE gherkin/LICENSE
%global godocs          examples CHANGELOG.md README.md gherkin/README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Official Cucumber BDD framework for Golang

# Upstream license specification: MIT and BSD-3-Clause
License:        MIT and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-sql-driver/mysql)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/DATA-DOG/go-txdb)
%endif

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
%license LICENSE gherkin/LICENSE
%doc examples CHANGELOG.md README.md gherkin/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 20:04:42 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.13-1
- Release 0.7.13

* Sun Mar 17 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.12-1
- Release 0.7.12 (#1689152)

* Wed Mar 13 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.11-1
- Release 0.7.11 (#1687703)

* Sun Mar 10 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.10-1
- Release 0.7.10 (#1687180)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.8-1
- Release 0.7.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.6-1
- First package for Fedora