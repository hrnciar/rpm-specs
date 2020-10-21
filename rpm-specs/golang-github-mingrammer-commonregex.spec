# Generated by go2rpm 1

# https://github.com/mingrammer/commonregex
%global goipath         github.com/mingrammer/commonregex
Version:                1.0.1

%gometa

%global common_description %{expand:
A collection of common regular expressions for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        A collection of common regular expressions for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/stretchr/testify/assert)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%check
%gocheck

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.1-1
- Initial package

