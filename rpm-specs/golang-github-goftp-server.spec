# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/goftp/server
%global goipath         github.com/goftp/server
%global commit          eabccc535b5a216dfa00bb8194563f73224a546d

%gometa

%global common_description %{expand:
A FTP server framework written in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        FTP server framework written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf exampleftpd

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 16:41:23 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190530giteabccc5
- Bump to commit eabccc535b5a216dfa00bb8194563f73224a546d

* Mon Feb 25 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20190225git88de73f
- Bump to commit 88de73f463afc77e1410b843e85bde37b5e261eb

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git1fd52c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20181105git1fd52c8
- First package for Fedora
