# Generated by go2rpm
%bcond_without check

# https://gitlab.com/opennota/wd
%global goipath         gitlab.com/opennota/wd
%global forgeurl        https://gitlab.com/opennota/wd
%global commit          236695b0ea6304781f21dd55e2f07476c36bed72

%gometa

%global common_description %{expand:
A package for comparing strings on a word per word basis and generating a
coloured diff.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Comparing strings on a word per word basis and generating a coloured diff

License:        GPLv3
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
* Wed Aug 05 13:41:53 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200805git236695b
- Bump to commit 236695b0ea6304781f21dd55e2f07476c36bed72

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 21:46:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701gitc5d65f6
- Initial package
