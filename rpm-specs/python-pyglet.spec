%global srcname pyglet
%global srcversion 1.4.6
%global versionedname %{srcname}-%{srcversion}

Name: python-%{srcname}
Version: %{srcversion}
Release: 3%{?dist}
Summary: A cross-platform windowing and multimedia library for Python

License: BSD
URL: http://www.pyglet.org/

# The upstream tarball includes some non-free files in the examples and tests,
# and a patented texture compression algorithm.
# Run the following (in rpmbuild/SOURCES) to generate the distributed tarball:
# $ bash pyglet-get-tarball.sh 1.3.2
# See the script for details.
Source0: %{versionedname}-repacked.tar.gz
Source1: pyglet-get-tarball.sh

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This library provides an object-oriented programming interface for developing
games and other visually-rich applications with Python.
pyglet has virtually no external dependencies. For most applications and game
requirements, pyglet needs nothing else besides Python, simplifying
distribution and installation. It also handles multiple windows and
fully aware of multi-monitor setups.

pyglet might be seen as an alternative to PyGame.


%package -n python3-%{srcname}
Summary: A cross-platform windowing and multimedia library for Python 3

%{?python_provide:%python_provide python3-%{srcname}}

Requires: python3
Requires: python3-pillow
Requires: python3-future

# The libraries are imported dynamically using ctypes, so rpm can't find them.
Requires: libGL
Requires: libGLU
Requires: libX11

%description -n python3-%{srcname}
This library provides an object-oriented programming interface for developing
games and other visually-rich applications with Python 3.
pyglet has virtually no external dependencies. For most applications and game
requirements, pyglet needs nothing else besides Python, simplifying
distribution and installation. It also handles multiple windows and
fully aware of multi-monitor setups.

pyglet might be seen as an alternative to PyGame.


%prep
%setup -q -n %{versionedname}

# Remove the bundled pypng library (python-pillow provides the same functionality)
rm pyglet/image/codecs/png.py
rm pyglet/extlibs/png.py

# The future library can be unbundled (upstream even does it for the wheel distribution)
rm -r pyglet/extlibs/future

# Get rid of hashbang lines. This is a library, it has no executable scripts.
# Also remove Windows newlines
find . -name '*.py' | xargs sed --in-place -e's|#!/usr/bin/\(env \)\?python||;s/\r//'


%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%doc RELEASE_NOTES
%doc NOTICE
%{python3_sitelib}/%{versionedname}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Petr Viktorin <pviktori@redhat.com> - 1.4.6-1
- Update to release 1.4.6
- Update upstream release URL

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Petr Viktorin <pviktori@redhat.com> - 1.4.1-1
- Update to release 1.4.1

* Tue Jul 23 2019 Petr Viktorin <pviktori@redhat.com> - 1.3.2-3
- Bump release for to fix upgrade from 29
  https://bugzilla.redhat.com/show_bug.cgi?id=1695261

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Petr Viktorin <pviktori@redhat.com> - 1.3.2-1
- Update to 1.3.2 and drop Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.7

* Tue Feb 06 2018 Petr Viktorin <pviktori@redhat.com> - 1.3.1-1
- Update to upstream 1.3.1 bugfix release
- Always build for Python 3; conditionalize the Python 2 library

* Fri Jan 26 2018 Petr Viktorin <pviktori@redhat.com> - 1.3.0-1
- Update to upstream 1.3.0

* Thu Aug 10 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.4-5
- Use versioned python prefix for python-setuptools

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-2
- Rebuild for Python 3.6

* Tue Aug 09 2016 Petr Viktorin <pviktori@redhat.com> - 1.2.4-1
- Update to upstream 1.2.4
- Specfile cleanup

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Petr Viktorin <pviktori@redhat.com> - 1.2.1-0
- Update to upstream 1.2.1 release

* Wed Jan 28 2015 Petr Viktorin <pviktori@redhat.com> - 1.2-0.13
- Actually use the 1.2.0 release

* Wed Jan 28 2015 Petr Viktorin <pviktori@redhat.com> - 1.2-0.12
- Use the official 1.2 release

* Wed Jan 28 2015 Petr Viktorin <pviktori@redhat.com> - 1.2-0.11.alpha1
- Install LICENSE as a license file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.10.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-0.9.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Jan 17 2014 Petr Viktorin <encukou@gmail.com> - 1.2-0.8.alpha1
- Remove Python 3 from BuildRequires if building without python3 support
  (needed for EPEL)

* Mon Oct 07 2013 Petr Viktorin <encukou@gmail.com> - 1.2-0.7.alpha1
- Enable Python 3 build

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.6.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Petr Viktorin <encukou@gmail.com> - 1.2-0.5.alpha1
- Add python3-devel to BuildRequires

* Wed Jun 05 2013 Petr Viktorin <encukou@gmail.com> - 1.2-0.4.alpha1
- Replace dos2unix by an additional sed command
- Remove bundled pypng, replace by a dependency in python-pillow
- Add a Python 3 build

* Fri Oct 19 2012 Petr Viktorin <encukou@gmail.com> - 1.2-0.1.alpha1
- initial version of package
