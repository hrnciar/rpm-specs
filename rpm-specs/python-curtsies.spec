Summary:       Curses-like terminal wrapper, with colored strings
Name:          python-curtsies
Version:       0.3.1
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/thomasballinger/curtsies
Source0:       https://files.pythonhosted.org/packages/source/c/curtsies/curtsies-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%global _description\
Curtsies is curses-like terminal wrapper, can be to annotate portions\
of strings with terminal colors and formatting.\
\
Most terminals will display text in color if you use ANSI escape codes\
- curtsies makes rendering such text to the terminal easy. Curtsies\
assumes use of an VT-100 compatible terminal: unlike curses, it has no\
compatibility layer for other types of terminals.
%description %_description

%package     -n python3-curtsies
Summary:        %summary
Requires:       python3-blessings >= 1.5
Requires:       python3-wcwidth >= 0.1.4
%description -n python3-curtsies %_description

%prep
%setup -q -n curtsies-%{version}

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-curtsies
%license LICENSE
%doc readme.md
%{python3_sitelib}/curtsies
%{python3_sitelib}/curtsies-*-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.3.1-1
- 0.3.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.3.0-5
- Remove legacy

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Sun May 27 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.3.0-1
- 0.3.0

* Tue Feb 13 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.2.12-1
- 0.2.12

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.11-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.11-5
- Python 2 binary package renamed to python2-curtsies
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.11-2
- Rebuild for Python 3.6

* Tue Oct 25 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.11-1
- 0.2.11

* Tue Oct 11 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.10-1
- 0.2.10

* Sun Sep 18 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.9-1
- 0.2.9

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Terje Rosten <terje.rosten@ntnu.no> - 0.2.6-1
- 0.2.6

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.1.19-1
- 0.1.19
- bpython needs < 0.2

* Tue Jan 13 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.2.0-1
- 0.2.0

* Wed May 28 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.0.32-1
- initial package
