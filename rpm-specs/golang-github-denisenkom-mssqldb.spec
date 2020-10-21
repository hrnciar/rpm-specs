# Generated by go2rpm
# https://github.com/denisenkom/go-mssqldb/issues/485
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/denisenkom/go-mssqldb
%global goipath         github.com/denisenkom/go-mssqldb
%global commit          36b6ff1bbc103b7b9497bb3c0c6f2788015ea02f

%gometa

%global common_description %{expand:
Package Mssql implements the TDS protocol used to connect to MS SQL Server
database servers.}

%global golicenses      LICENSE.txt
%global godocs          doc examples README.md

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        Microsoft SQL server driver written in Go language

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/golang-sql/civil)
BuildRequires:  golang(golang.org/x/crypto/md4)

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
* Wed Sep 09 14:16:21 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.11.20200909git36b6ff1
- Bump to commit 36b6ff1bbc103b7b9497bb3c0c6f2788015ea02f

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.7.20190626git731ef37
- Add Obsoletes for old name

* Tue Apr 30 00:27:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20190626git731ef37
- Bump to commit 731ef375ac027e24d275c5432221dbec5007a647

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20180725git242fa5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Ed Marshall <esm@logic.net> - 0-0.4.20180725git242fa5a
- Switch to forge-specific packaging.
- Update to latest upstream commit.
- Fix build failure with Go 1.11 beta.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180314git94099f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Ed Marshall <esm@logic.net> - 0-0.2.20180314git94099f0
- Bump release. Whoops!

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 0-0.1.20180314git94099f0
- Switch to upstream version with patch applied.

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 0-0.1.20180314gitb2a6258
- Update to latest git commit, for Go 1.10 test fixes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170919gitc7ee415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170919gitc7ee415
- First package for Fedora
