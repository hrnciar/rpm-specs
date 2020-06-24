# Generated by go2rpm
%bcond_without check

# https://github.com/SAP/go-hdb
%global goipath         github.com/SAP/go-hdb
Version:                0.14.1

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-SAP-go-hdb-devel < 0.14.1-2
}

%global common_description %{expand:
A Go implementation of an SAP HANA Database Client.}

%global golicenses      LICENSE NOTICE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        SAP HANA Database Client for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/transform)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# The driver tests require a running SAP DB, sadly.
%gocheck -d driver
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14.1-3
- Add Obsoletes for old name

* Sun Jun 02 15:21:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.1-2
- Update to new macros

* Sun Mar 17 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.1-1
- Release 0.14.1 (#1689530)

* Thu Mar 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.0-1
- Release 0.14.0 (#1687170)
- Re-enable s390x

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Ed Marshall <esm@logic.net> - 0.12.1-2
- Exclude builds on s390x. (#1595083)

* Mon Jun 25 2018 Ed Marshall <esm@logic.net> - 0.12.1-1
- Update to 0.12.1.
- Update spec to latest go packaging macros.

* Tue Mar 27 2018 Ed Marshall <esm@logic.net> - 0.11.0-1
- Update to 0.11.0.

* Fri Mar 23 2018 Ed Marshall <esm@logic.net> - 0.10.0-1
- Update to 0.10.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Ed Marshall <esm@logic.net> - 0.9.5-1
- Update to 0.9.5. (#1523964)

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 0.9.1-1
- First package for Fedora