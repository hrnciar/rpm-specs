# Generated by go2rpm
%bcond_without check

# https://github.com/jpillora/ansi
%global goipath         github.com/jpillora/ansi
Version:                1.0.2

%gometa

%global common_description %{expand:
Easy to use ANSI control codes.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Easy to use ANSI control codes

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.2-1
- Add LICENSE file
- Update to latest upstream release 1.0.2 (rhbz#1820856)

* Wed Feb 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora

