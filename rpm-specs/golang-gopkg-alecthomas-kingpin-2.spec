# Generated by go2rpm
%bcond_without check

# https://github.com/alecthomas/kingpin
%global goipath         gopkg.in/alecthomas/kingpin.v2
%global forgeurl        https://github.com/alecthomas/kingpin
Version:                2.2.6

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-alecthomas-kingpin-devel < 2.2.6-3
}

%global common_description %{expand:
Kingpin is a fluent-style, type-safe command-line parser. It supports flags,
nested commands, and positional arguments.}

%global golicenses      COPYING
%global godocs          _examples README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Go command line and flag parser

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/template)
BuildRequires:  golang(github.com/alecthomas/units)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.6-4
- Add Obsoletes for old name

* Sat Apr 20 22:48:28 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.6-3
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.6-1
- Release 2.2.6
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3.git1087e65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2.git1087e65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 mosquito <sensor.wen@gmail.com> - 2.2.5-1
- Release 2.2.5

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.3-1.gite9044be
- Initial package build
