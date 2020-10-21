# Generated by go2rpm
%bcond_without check

# https://github.com/jessevdk/go-assets
%global goipath         github.com/jessevdk/go-assets
%global commit          4f4301a06e153ff90e17793577ab6bf79f8dc5c5

%gometa

%global common_description %{expand:
Go-assets is a simple embedding asset generator and consumer library for Go. The
main use of the library is to generate and embed small in-memory file systems
ready to be integrated in webservers or other services which have a small amount
of assets used at runtime. This is great for being able to do single binary
deployments with assets.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Simple embedding of assets in Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 15:31:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git4f4301a
- Initial package
