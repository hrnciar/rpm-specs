# Generated by go2rpm 1
%bcond_without check

# https://github.com/gobuffalo/packd
%global goipath         github.com/gobuffalo/packd
Version:                1.0.0

%gometa

%global common_description %{expand:
This is a collection of interfaces designed to make using
github.com/gobuffalo/packr easier, and to make the transition between v1 and v2
as seamless as possible.}

%global golicenses      LICENSE
%global godocs          README.md SHOULDERS.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Gobuffalo/packr interfaces

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 12:05:58 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Initial package
