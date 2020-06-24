# Generated by go2rpm 1
%bcond_without check

# https://github.com/google/go-cmp
%global goipath         github.com/google/go-cmp
Version:                0.4.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-google-go-cmp-devel < 0.2.0-6
}

%global common_description %{expand:
This package is intended to be a more powerful and safer alternative
to reflect.DeepEqual for comparing whether two values are semantically
equal.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package for comparing Go values in tests

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/xerrors)

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
* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-2
- Add Obsoletes for old name

* Tue Apr 23 09:54:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Release 0.3.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-4
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Ed Marshall <esm@logic.net> - 0.2.0-1
* Update to upstream release 0.2.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 Ed Marshall <esm@logic.net> - 0.1.0-1
- First package for Fedora
