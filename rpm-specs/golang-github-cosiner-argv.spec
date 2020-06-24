# Generated by go2rpm
%bcond_without check

# https://github.com/cosiner/argv
%global goipath         github.com/cosiner/argv
Version:                0.1.0

%gometa

%global common_description %{expand:
Package Argv parse command line string into arguments array using the bash
syntax.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Library for Go to split command line string into arguments array

License:        MIT
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
* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 16:45:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-3
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.1-1
- Update to first tagged version

* Fri Nov 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180815git13bacc3
- Cleanup SPEC

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.2.20180815git13bacc3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180815git13bacc3
- First package for Fedora
