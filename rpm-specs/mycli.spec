%if 0%{?fedora} > 32
%global prompt_toolkit 3.0.0
%else
%global prompt_toolkit 2.0.6
%endif

%if 0%{?fedora} < 32
%global sqlparse 0.2.4
%else
%global sqlparse 0.3.0
%endif

Summary:        Interactive CLI for MySQL Database with auto-completion and syntax highlighting
Name:           mycli
Version:        1.21.1
Release:        5%{?dist}
License:        BSD
URL:            http://mycli.net
Source0:        https://files.pythonhosted.org/packages/source/m/mycli/mycli-%{version}.tar.gz
%if 0%{?fedora} > 32
Patch0:         mycli-1.21.1-prompt-toolkit.patch
%endif
%if 0%{?fedora} < 32
Patch0:         mycli-1.21.1-sqlparse.patch
%endif

Patch1:         0001-Try-list-of-known-socket-file-locations-by-default.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-cli-helpers >= 1.0.1
Requires:       python3-click >= 4.1
Requires:       python3-configobj >= 5.0.5
Requires:       python3-cryptography => 1.0.0
Requires:       python3-pygments >= 1.6
Requires:       python3-PyMySQL >= 0.9.2
Requires:       python3-prompt-toolkit >= %{prompt_toolkit}
Requires:       python3-setuptools
Requires:       python3-sqlparse >= %{sqlparse}
#BuildRequires for tests
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  %{py3_dist twine} >= 1.8.1
BuildRequires:  python3-cli-helpers >= 1.0.1
BuildRequires:  python3-click >= 4.1
BuildRequires:  python3-configobj >= 5.0.5
BuildRequires:  python3-cryptography => 1.0.0
BuildRequires:  python3-pygments >= 1.6
BuildRequires:  python3-PyMySQL >= 0.9.2
BuildRequires:  python3-prompt-toolkit >= %{prompt_toolkit}
BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlparse >= %{sqlparse}
%description
Nice interactive shell for MySQL Database with auto-completion and
syntax highlighting.

%prep
%autosetup -p1
rm -rf mycli.egg-info

%build
%{py3_build}

%install
%{py3_install}
rm -rf %{buildroot}%{python3_sitelib}/test

%check
PYTHONPATH=build/lib/ py.test-3

%files
%license LICENSE.txt
%doc mycli/AUTHORS README.md mycli/SPONSORS
%{_bindir}/mycli
%{python3_sitelib}/mycli
%{python3_sitelib}/mycli-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.21.1-5
- Rebuilt for Python 3.9

* Thu May 07 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-4
- Use prompt toolkit 3.0.0 on f33+

* Tue May 05 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-3
- Use sqlparse 0.3.0 on f32+

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-2
- Add patch to find default socket file

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.1-1
- 1.21.1

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.21.0-1
- 1.21.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.20.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.1-1
- 1.20.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.20.0-4
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.0-3
- Don't mask failures

* Wed Aug 14 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.0-2
- Add sqlparse 0.2.4 patch from Dick Marinus, thanks!

* Tue Aug 13 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.20.0-1
- 1.20.0

* Fri Aug 09 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.19.0-4
- Fix build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.19.0-1
- 1.19.0

* Mon Nov 12 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.18.2-2
- Fix prompt_toolkit 1 patch, update by Dick

* Wed Nov 07 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.18.2-1
- 1.18.2
- Add patch for compat with prompt_toolkit 1, thanks to Dick Marinus
- Add patch to work with prompt_toolkit > 2.0.6

* Fri Oct 19 2018 Carl George <carl@george.computer> - 1.18.0-2
- Add patch0 for prompt_toolkit 2 compatibility

* Sun Sep 30 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.18.0-1
- 1.18.0

* Sat Jul 14 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.17.0-4
- Tests started to fail again

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.17.0-1
- 1.17.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.16.0-1
- 1.16.0

* Sun Oct 01 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.13.1-1
- 1.13.1

* Sun Sep 24 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.13.0-2
- Skip tests on older releases

* Sat Sep 23 2017 Dick Marinus <dick@mrns.nl> - 1.13.0-1
- 1.13.0

* Sat Sep 02 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.12.1-2
- Fix date
- Remove sedding

* Thu Aug 31 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.12.1-1
- 1.12.1
- Adjust reqs.
- Remove all patches

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 20 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.10.0-2
- Add patch from Dick Marinus to fix sqlparse issue

* Sat May 06 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.10.0-1
- 1.10.0

* Tue Feb 14 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.8.1-4
- Add patch to work with sqlparse >= 0.2.2 (rhbz#1422211)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-2
- Rebuild for Python 3.6

* Tue Oct 25 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.8.1-1
- 1.8.1

* Sat Sep 17 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.8.0-2
- Add patch from Dick Marinus to fix issue with newer sqlparse

* Tue Aug 09 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.8.0-1
- 1.8.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 13 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.7.0-1
- 1.7.0

* Sun Mar 27 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.6.0-1
- 1.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-4
- Add patch to enable prompt_toolkit 0.57 support.

* Thu Jan 07 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-3
- Remove configobj patch
- Use name macro

* Sun Jan 03 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-2
- remove egginfo
- fix deps and summary

* Sat Jan 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.5.2-1
- initial package

