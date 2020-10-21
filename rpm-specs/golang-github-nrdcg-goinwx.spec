# Generated by go2rpm
%bcond_without check

# https://github.com/nrdcg/goinwx
%global goipath         github.com/nrdcg/goinwx
Version:                0.7.0

%gometa

%global common_description %{expand:
This Go library implements some parts of the official INWX XML-RPC API.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        INWX Go API client

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fatih/structs)
BuildRequires:  golang(github.com/kolo/xmlrpc)
BuildRequires:  golang(github.com/mitchellh/mapstructure)

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 07:13:59 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 22:54:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Initial package
