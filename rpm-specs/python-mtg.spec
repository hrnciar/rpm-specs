%global pypi_name mtg

Name:           python-%{pypi_name}
Version:        1.6.1
Release:        15%{?dist}
Summary:        Console-based access to the Gatherer Magic Card Database

License:        MIT
URL:            https://github.com/chigby/mtg

# Documentation, license, and unit tests aren't available from PyPI, so pull from github.
# Unfortunately, we have to modify the github tarball to remove Gatherer data. (tests/_data).
# https://github.com/chigby/mtg/archive/%{version}/mtg-%{version}.tar.gz
Source0:        %{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-lxml, python3-cssselect, python3-nose

%description
Search for Magic cards from the command line. Limit your results by card name,
color, type, rules text, converted mana cost, power, toughness, or expansion
set. Rulings and flavor text also available. Clean interface and output.

%package -n     python3-%{pypi_name}
Summary:        Console-based access to the Gatherer Magic Card Database
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-lxml
Requires:       python3-cssselect

# This is (primarily) a CLI application; provide "mtg".
Provides:       mtg

%description -n python3-%{pypi_name}
Search for Magic cards from the command line. Limit your results by card name,
color, type, rules text, converted mana cost, power, toughness, or expansion
set. Rulings and flavor text also available. Clean interface and output.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove unit tests that depend on _data (which is copyright WoTC and probably not shippable).
rm -f tests/card_extractor_test.py

%build
%py3_build

%install
%py3_install

# Since there's no potential collision, we don't need to version the mtg binary.
# cp %{buildroot}/%{_bindir}/mtg %{buildroot}/%{_bindir}/mtg-3
# ln -sf %{_bindir}/mtg-3 %{buildroot}/%{_bindir}/mtg-%{python3_version}

%check
nosetests-3 -v

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/mtg
%{python3_sitelib}/mtglib
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.1-9
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Sep 18 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.6.1-8
- Remove python2 subpackage (rhbz#1630081).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.6.1-2
- Remove mtg-2* binaries, as they should behave the same as the python3 versions.
- Get rid of the versioned mtg-3 binaries, as there's no potential collision with python2 binaries.
- Remove card_extractor_test.py, as those tests require tests/_data directory.
- Remove tests/_data directory from tarball, as Fedora probably can't ship it in a source package.

* Wed Feb 22 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.6.1-1
- Initial package.
