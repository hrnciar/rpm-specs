# Generated by go2rpm
%bcond_without check

# https://github.com/posener/complete
%global goipath         github.com/posener/complete
Version:                1.2.1

%gometa

%global common_description %{expand:
A tool for writing bash completion in Go, and bash completion for the Go
command line.}

%global golicenses      LICENSE.txt
%global godocs          example readme.md

Name:           gocomplete
Release:        5%{?dist}
Summary:        Tool for writing bash completion in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-multierror)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/gocomplete %{goipath}/gocomplete

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.txt
%doc example readme.md
%{_bindir}/gocomplete

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-3
- Update to latest Go macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Ed Marshall <esm@logic.net> - 1.2.1-1
- Update to latest upstream release.

* Tue Sep 25 2018 Ed Marshall <esm@logic.net> - 1.1.2-2
- Pull in upstream patch for go 1.11.

* Tue Sep 25 2018 Ed Marshall <esm@logic.net> - 1.1.2-1
- Update to latest upstream release.

* Thu Jul 19 2018 Ed Marshall <esm@logic.net> - 1.1.1-2
- Switch to forge-specific packaging.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 1.1.1-0
- Update to 1.1.1.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170908git88e5976
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Ed Marshall <esm@logic.net> - 0-0.2.20170908git88e5976
* Fix unit-test/devel dependency issue.

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170908git88e5976
- First package for Fedora
