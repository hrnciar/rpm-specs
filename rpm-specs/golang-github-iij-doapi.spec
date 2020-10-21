# Generated by go2rpm
%bcond_without check

# https://github.com/iij/doapi
%global goipath         github.com/iij/doapi
%global commit          8803795a9b7b938fa88ddbd63a77893beee14cd8

%gometa

%global common_description %{expand:
Golang binding for DO API.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Golang binding for DO API

# https://github.com/iij/doapi/issues/2
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://raw.githubusercontent.com/iij/doapi/master/LICENSE.md

BuildRequires:  golang(github.com/sirupsen/logrus)

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} .

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

* Thu May 02 21:17:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190502git8803795
- Initial package
