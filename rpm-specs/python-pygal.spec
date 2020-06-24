
%global modname pygal

Name:               python-pygal
Version:            2.4.0
Release:            14%{?dist}
Summary:            A python svg graph plotting library

License:            LGPLv3+
URL:                https://pypi.io/project/pygal
Source0:            https://pypi.io/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pyquery
BuildRequires:      python3-flask
BuildRequires:      python3-pytest-runner

# See https://bugzilla.redhat.com/show_bug.cgi?id=1263793
#BuildRequires:      python3-cairosvg
BuildRequires:      python3-CairoSVG
BuildRequires:      python3-cairocffi

BuildRequires:      python3-pytest
BuildRequires:      python3-lxml

%global _description\
A python svg graph plotting library.

%description %_description

%package -n python3-pygal
Summary:            A python svg graph plotting library

Requires:           python3-lxml

%description -n python3-pygal
A python svg graph plotting library

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%py3_build


%install
%py3_install


%check
## python3 tests aren't quite working yet.  something to do with cairocffi, but
## I can't duplicate it locally....
#py.test-%{python3_version} pygal/test


%files -n python3-pygal
%doc README
%{_bindir}/pygal_gen.py
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 2.4.0-9
- Fix FTBFS bug #1675774

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-8
- Subpackage python2-pygal has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.4.0-6
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.4.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Sep 15 2017 Kevin Fenzi <kevin@scrye.com> - 2.4.0-1
- Update to 2.4.0. Fixes bug #1467884

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.1-4
- Python 2 binary package renamed to python2-pygal
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Kevin Fenzi <kevin@scrye.com> - 2.3.1-1
- Update to 2.3.1. Fixes bug #1400596

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Rebuild for Python 3.6

* Tue Sep 06 2016 Ralph Bean <rbean@redhat.com> - 2.3.0-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 01 2016 Kevin Fenzi <kevin@scrye.com> - 2.2.3-1
- Update to 2.2.3. Fixes bug #1341395

* Thu Apr 28 2016 Kevin Fenzi <kevin@scrye.com> - 2.2.2-1
- Update to 2.2.2. Fixes bug #1330791

* Sat Apr 23 2016 Kevin Fenzi <kevin@scrye.com> - 2.2.1-1
- Update to 2.2.1. Fixes bug #1329207

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 2.1.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Ralph Bean <rbean@redhat.com> - 2.0.10-1
- new version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov  6 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.8-2
- Ship the pygal_gen.py script in python3-pygal.  Several reasons for this:
  * It uses /usr/bin/python3 so it was creating a dep on python3 in the
    python2 package
  * It wouldn't function without manual user intervention as it needed
    the python3-pygal package but didn't have a dep on that.

* Tue Oct 20 2015 Ralph Bean <rbean@redhat.com> - 2.0.8-1
- new version

* Mon Sep 28 2015 Ralph Bean <rbean@redhat.com> - 2.0.7-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 2.0.6-1
- Latest upstream.
- Enabled python3 tests.  We can do this now!!
  It's like I'm living in the future.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Ralph Bean <rbean@redhat.com> - 1.6.1-1
- new version

* Mon Nov 10 2014 Ralph Bean <rbean@redhat.com> - 1.5.1-1
- Latest upstream RHBZ#1140143.

* Thu Sep 04 2014 Ralph Bean <rbean@redhat.com> - 1.5.0-2
- Disable tests for epel.

* Mon Aug 18 2014 Ralph Bean <rbean@redhat.com> - 1.5.0-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Apr 22 2014 Ralph Bean <rbean@redhat.com> - 1.4.6-1
- Latest upstream.

* Fri Mar 07 2014 Ralph Bean <rbean@redhat.com> - 1.4.5-1
- Latest upstream.

* Thu Feb 27 2014 Ralph Bean <rbean@redhat.com> - 1.4.2-1
- Latest upstream.
- Reenabled tests.

* Wed Feb 26 2014 Ralph Bean <rbean@redhat.com> - 1.4.1-1
- Latest upstream.
- Disable tests for https://github.com/Kozea/pygal/issues/97

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 1.3.1-1
- Latest upstream.

* Sun Feb 02 2014 Ralph Bean <rbean@redhat.com> - 1.2.3-1
- Latest upstream
- Re-enabled tests.

* Thu Jan 30 2014 Ralph Bean <rbean@redhat.com> - 1.2.2-1
- Latest upstream.
- Remove patch, now upstreamed.
- Disable tests.. pytest is behaving strangely.

* Fri Nov 15 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- Latest upstream.
- Re-enabled python3 subpackage.
- Patch to get around encoding issues in the build step.
- Updated comment about requirements for python3 tests.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Ralph Bean <rbean@redhat.com> - 0.13.0-2
- Updated license with clarification from usptream
  https://github.com/Kozea/pygal/pull/32

* Sat Apr 13 2013 Ralph Bean <rbean@redhat.com> - 0.13.0-1
- Initial package for Fedora
