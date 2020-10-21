# Generated by go2rpm
%bcond_without check
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(\\.\\/vhd\\)$

# https://github.com/rubiojr/go-vhd
%global goipath         github.com/rubiojr/go-vhd
%global commit          ccecf6c0760f5698115dda767d15ba2b9a31469a

%gometa

%global common_description %{expand:
Go package and CLI to work with VHD images.}

%global golicenses      LICENSE
%global godocs          README.md notes.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Go package and CLI to work with VHD images

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(golang.org/x/text/encoding/unicode)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Aug 01 23:56:41 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200801gitccecf6c
- Bump to commit ccecf6c0760f5698115dda767d15ba2b9a31469a

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 23:00:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702git0bfd3b3
- Initial package
