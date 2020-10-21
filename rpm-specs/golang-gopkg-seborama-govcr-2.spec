# Generated by go2rpm
%bcond_without check

# https://github.com/seborama/govcr
%global goipath         gopkg.in/seborama/govcr.v2
%global forgeurl        https://github.com/seborama/govcr
%global tag             2.4.2
Version:                2.4.2

%gometa

%global common_description %{expand:
HTTP mock for Golang: record and replay HTTP/HTTPS interactions for offline
testing.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        HTTP mock for Golang

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 23:27:39 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.2-1
- Initial package
