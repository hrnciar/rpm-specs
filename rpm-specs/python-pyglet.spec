%global srcname pyglet
%global srcversion 1.5.7
%global versionedname %{srcname}-%{srcversion}

%bcond_without tests

Name: python-%{srcname}
Version: %{srcversion}
Release: 1%{?dist}
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

# Tests (and possibly sound synthesis?) fail on big-endian.
# Reported: https://github.com/pyglet/pyglet/issues/278
# Fedora bug: https://bugzilla.redhat.com/show_bug.cgi?id=1877849
ExcludeArch: s390x

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

# Tests need OpenGL
# See also: https://bugzilla.redhat.com/show_bug.cgi?id=904851
%global __pytest xvfb-run -s '-screen 0 640x480x24' pytest
%if %{with tests}
BuildRequires: /usr/bin/xvfb-run mesa-dri-drivers
BuildRequires: python3-pytest
# libpurple has sound files unbundled in the repacked tarball
BuildRequires: libpurple
%endif


%global _description %{expand:
This library provides an object-oriented programming interface for developing
games and other visually-rich applications with Python.
pyglet has virtually no external dependencies. For most applications and game
requirements, pyglet needs nothing else besides Python, simplifying
distribution and installation. It also handles multiple windows and
fully aware of multi-monitor setups.

pyglet might be seen as an alternative to PyGame.
}

%generate_buildrequires
%pyproject_buildrequires


%description %_description


%package -n python3-%{srcname}
Summary: A cross-platform windowing and multimedia library for Python 3

%{?python_provide:%python_provide python3-%{srcname}}

# The libraries are imported dynamically using ctypes, so rpm can't find them.
Requires: libGL
Requires: libGLU
Requires: libX11
Requires: fontconfig

# Pillow is technically optional, but in Fedora we always pull it in.
# It can open PNG images, so we can remove the bundled "png.py"
Requires: python3-pillow

%if %{with tests}
BuildRequires: libGL
BuildRequires: libGLU
BuildRequires: libX11
BuildRequires: fontconfig
BuildRequires: python3-pillow
%endif


%description -n python3-%{srcname} %_description


%prep
%setup -q -n %{versionedname}

# Remove the bundled pypng library (python-pillow provides the same functionality)
rm pyglet/image/codecs/png.py
rm pyglet/extlibs/png.py

# Get rid of hashbang lines. This is a library, it has no executable scripts.
# Also remove Windows newlines
find . -name '*.py' | xargs sed --in-place -e's|#!/usr/bin/\(env \)\?python||;s/\r//'


%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pyglet


%if %{with tests}
%check
# Skip flaky tests
export CI=on

# The files are unbundled in the repacked tarball
ln -s %{_datadir}/sounds/purple/*.wav tests/data/media/

# Interactive tests are skipped for obvious reasons.
# Media player tests are skipped -- we don't have PulseAudio running.
# test_find_font_match & test_have_font skipped -- they look for a font named 'arial'
# test_freetype_face tests are is skipped -- they depend on non-free font we remove
%pytest \
    -vv \
    --non-interactive \
    --ignore=tests/interactive \
    --ignore=tests/integration/media \
    -m 'not (requires_user_action or requires_user_validation or only_interactive)' \
    -k 'not (test_find_font_match or test_have_font or test_freetype_face)' \
    tests
%endif


%files -n python3-%{srcname} -f %%{pyproject_files}
%license LICENSE
%doc README.md
%doc RELEASE_NOTES
%doc NOTICE


%changelog
* Wed Sep 09 2020 Petr Viktorin <pviktori@redhat.com> - 1.5.7-1
- Update to 1.5.7
- Switch to pyproject macros
- Run tests

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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
