# Generated by go2rpm 1
%bcond_without check

# https://gitea.com/goftp/server
%global goipath         goftp.io/server
%global forgeurl        https://gitea.com/goftp/server
Version:                0.4.0
%global repo            server
%global archivename     %{repo}-%{version}
%global archiveext      tar.gz
%global archiveurl      %{forgeurl}/archive/v%{version}.%{archiveext}
%global topdir          %{repo}
%global extractdir      %{repo}
%global scm             git

%gometa

%global goaltipaths     github.com/goftp/server

%global common_description %{expand:
A FTP server framework written in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        FTP server framework written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/minio/minio-go/v6)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/jlaffaye/ftp)
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
* Wed Aug 05 14:21:20 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 16:08:39 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.4-1
- Initial package
