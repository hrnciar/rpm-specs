Name:           python-virtualenv
Version:        20.0.23
Release:        1%{?dist}
Summary:        Tool to create isolated Python environments

License:        MIT
URL:            http://pypi.python.org/pypi/virtualenv
Source0:        %{pypi_source virtualenv}

# Add /usr/share/python-wheels to extra_search_dir
Patch1: rpm-wheels.patch

BuildArch:      noarch

BuildRequires:  python3-appdirs
BuildRequires:  python3-devel
BuildRequires:  python3-distlib
BuildRequires:  python3-filelock
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six

# docs need sphinx >= 3
# docs need towncrier and that is not yet available when bootstrapping Python
%bcond_with docs
%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-towncrier
%endif

%bcond_without tests
%if %{with tests}
BuildRequires:  fish
BuildRequires:  gcc
BuildRequires:  python3-coverage
BuildRequires:  python3-flaky
BuildRequires:  python3-packaging
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-randomly
BuildRequires:  python3-pytest-timeout
# FTBFS with Py 3.9: https://bugzilla.redhat.com/show_bug.cgi?id=1817770
# BuildRequires:  xonsh
%endif

# RPM installed wheels
BuildRequires:  python-pip-wheel
BuildRequires:  python-setuptools-wheel
BuildRequires:  python-wheel-wheel

%description
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project. It is
licensed under an MIT-style permissive license.


%package -n     python3-virtualenv
Summary:        Tool to create isolated Python environments

Requires:       python3-appdirs
Requires:       python3-distlib
Requires:       python3-filelock
Requires:       python3-setuptools
Requires:       python3-six
Obsoletes:      python3-virtualenv-python26 < 16.6
%{?python_provide:%python_provide python3-virtualenv}

# Provide "virtualenv" for convenience
Provides:       virtualenv = %{version}-%{release}

# RPM installed wheels
Requires:       python-pip-wheel
Requires:       python-setuptools-wheel
Requires:       python-wheel-wheel

%description -n python3-virtualenv
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project. It is
licensed under an MIT-style permissive license


%if %{with docs}
%package -n     python-virtualenv-doc
Summary:        Documentation for python virtualenv

%description -n python-virtualenv-doc
Documentation for python virtualenv.
%endif


%prep
%autosetup -p1 -n virtualenv-%{version}
%{__sed} -i -e "1s|#!/usr/bin/env python||" tasks/update_embedded.py

# Remove the wheels provided by RPM packages
rm src/virtualenv/seed/embed/wheels/pip-*
rm src/virtualenv/seed/embed/wheels/setuptools-*
rm src/virtualenv/seed/embed/wheels/wheel-*

test ! -f src/virtualenv/seed/embed/wheels/*.whl

%build
# Build code
%{py3_build}

# Build docs
%if %{with docs}
PYTHONPATH=src %{python3} setup.py build_sphinx
rm -f build/sphinx/html/.buildinfo
%endif

%install
%{py3_install}

%if %{with tests}
%check
mkdir tmp_path
ln -s $(realpath %{__python3}) tmp_path/python
export PATH="$(pwd)/tmp_path:$PATH"
unset SOURCE_DATE_EPOCH

# Skip tests which requires internet or some extra dependencies
# Requires internet:
# - test_base_bootstrap_via_pip_invoke
# - test_seed_link_via_app_data
# Detects system Python even it should not (problem with mock?):
# - test_py_info_to_system_raises
# Uses disabled functionalities around bundled wheels:
# - test_wheel_support_no_python_requires
# Requires xonsh (FTBFS with Py 3.9)
# - test_xonsh
# Does not work with beta release of Python:
# - test_version_satisfies_nok
%pytest -vv -k "not test_base_bootstrap_via_pip_invoke and not test_seed_link_via_app_data and not test_py_info_to_system_raises and not test_wheel_support_no_python_requires and not test_xonsh and not test_version_satisfies_nok"

rm -r tmp_path
%endif

%files -n python3-virtualenv
%license LICENSE
%doc docs/*rst README.md
%{_bindir}/virtualenv
%{python3_sitelib}/virtualenv/
%{python3_sitelib}/virtualenv-*.egg-info/

%if %{with docs}
%files -n python-virtualenv-doc
%doc build/sphinx/*
%endif


%changelog
* Mon Jun 15 2020 Lumír Balhar <lbalhar@redhat.com> - 20.0.23-1
- Update to 20.0.23 (#1742034)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 16.7.10-2
- Rebuilt for Python 3.9

* Tue Feb 25 2020 Miro Hrončok <mhroncok@redhat.com> - 16.7.10-1
- Update to 16.7.10
- Explicitly require setuptools < 44 with Python 3.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Miro Hrončok <mhroncok@redhat.com> - 16.7.3-2
- Prefer wheels bundled in Python's ensurepip module over the RPM built ones
- This allows continuing support for Python 3.4 in Fedora 32+

* Wed Aug 21 2019 Charalampos Stratakis <cstratak@redhat.com> - 16.7.3-1
- Update to 16.7.3 (#1742034)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 16.6.1-3
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Miro Hrončok <mhroncok@redhat.com> - 16.6.1-2
- Drop python2-virtualenv

* Thu Jul 11 2019 Miro Hrončok <mhroncok@redhat.com> - 16.6.1-1
- Update to 16.6.1 (#1699031)
- No more Python 2.6 or Jython support
- Drop runtime dependency on pythonX-devel

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Miro Hrončok <mhroncok@redhat.com> - 16.0.0-6
- Don't fail on missing certifi's cert bundle (#1655253)

* Wed Aug 15 2018 Miro Hrončok <mhroncok@redhat.com> - 16.0.0-5
- Use wheels from RPM packages
- Put wheels needed for Python 2.6 into a subpackage
- Only have one /usr/bin/virtualenv (#1599422)
- Provide "virtualenv" (#1502670)

* Wed Jul 18 2018 Miro Hrončok <mhroncok@redhat.com> - 16.0.0-4
- Reintroduce support for Python 2.6 (#1602347)
- Add missing bundled provides

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 16.0.0-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Steve Milner <smilner@redhat.com> - 16.0.0-1
- Updated for upstream release.

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 15.1.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 15.1.0-3
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Steve Milner <smilner@redhat.com> - 15.1.0-1
- Update to 15.1.0 per https://bugzilla.redhat.com/show_bug.cgi?id=1454962

* Fri Feb 17 2017 Michal Cyprian <mcyprian@redhat.com> - 15.0.3-6
- Check if exec_dir exists before listing it's content during venv create process

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan  4 2017 Steve Milner <smilner@redhat.com> - 15.0.3-4
- Updated version binaries per discussion at bz#1385240.

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 15.0.3-3
- Rebuild for Python 3.6

* Mon Oct 17 2016 Steve Milner <smilner@redhat.com> - 15.0.3-2
- Added MAJOR symlinks per bz#1385240.

* Mon Aug  8 2016 Steve Milner <smilner@redhat.com> - 15.0.3-1
- Update for upstream release.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 21 2016 Orion Poplawski <orion@cora.nwra.com> - 14.0.6-1
- Update to 14.0.6

* Tue Feb 2 2016 Orion Poplawski <orion@cora.nwra.com> - 13.1.2-4
- Modernize spec
- Fix python3 package file ownership

* Wed Dec 2 2015 Orion Poplawski <orion@cora.nwra.com> - 13.1.2-3
- Move documentation to separate package (bug #1219139)

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 13.1.2-2
- Rebuilt for Python3.5 rebuild

* Mon Aug 24 2015 Steve Milner <smilner@redhat.com> - 13.1.2-1
- Update for upstream release.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Matej Stuchlik <mstuchli@redhat.com> - 12.0.7-1
- Update to 12.0.7

* Thu Jan 15 2015 Matthias Runge <mrunge@redhat.com> - 1.11.6-2
- add a python3-package, thanks to Matej Stuchlik (rhbz#1179150)

* Wed Jul 09 2014 Matthias Runge <mrunge@redhat.com> - 1.11.6-1
- update to 1.11.6:
  Upstream updated setuptools to 3.6, updated pip to 1.5.6

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.10.1-1
- Upstream upgraded pip to v1.4.1
- Upstream upgraded setuptools to v0.9.8 (fixes CVE-2013-1633)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.9.1-1
- Update to upstream 1.9.1 because of security issues with the bundled
  python-pip in older releases.  This is just a quick fix until a
  python-virtualenv maintainer can unbundle the python-pip package
  see: https://bugzilla.redhat.com/show_bug.cgi?id=749378

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Steve Milner <me@stevemilner.org> - 1.7.2-1
- Update for upstream bug fixes.
- Added path for versioned binary.
- Patch no longer required.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.7.1.2-1
- Update for upstream bug fixes.
- Added patch for sphinx building

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.7-1
- Update for https://bugzilla.redhat.com/show_bug.cgi?id=769067

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 16 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.5.1-1
- Added _weakrefset requirement for Python 2.7.1.
- Add support for PyPy.
- Uses a proper temporary dir when installing environment requirements.
- Add --prompt option to be able to override the default prompt prefix.
- Add fish and csh activate scripts.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul  7 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.8-3
- Fixed EPEL installation issue from BZ#611536

* Wed Jun  9 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.8-2
- Only replace the python shebang on the first line (Robert Buchholz)

* Wed Apr 28 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.8-1
- update pip to 0.7
- move regen-docs into bin/
- Fix #31, make activate_this.py work on Windows (use Lib/site-packages)
unset PYTHONHOME envioronment variable -- first step towards fixing the PYTHONHOME issue; see e.g. https://bugs.launchpad.net/virtualenv/+bug/290844
- unset PYTHONHOME in the (Unix) activate script (and reset it in deactivate())
- use the activate.sh in virtualenv.py via running bin/rebuild-script.py
- add warning message if PYTHONHOME is set

* Fri Apr 2 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.6-1
- allow script creation without setuptools
- fix problem with --relocate when bin/ has subdirs (fixes #12)
- Allow more flexible .pth file fixup
- make nt a required module, along with posix. it may not be a builtin module on jython
- don't mess with PEP 302-supplied __file__, from CPython, and merge in a small startup optimization for Jython, from Jython

* Tue Dec 22 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.3-1
- Updated for upstream release.

* Thu Nov 12 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.2-1
- Updated for upstream release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.3-1
- Updated for upstream release.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.2-1
- Updated for upstream release.

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.1-4
- Rebuild for Python 2.6

* Mon Dec  1 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.1-3
- Added missing dependencies.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.1-2
- Rebuild for Python 2.6

* Fri Nov 28 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.1-1
- Updated for upstream release

* Sun Sep 28 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3-1
- Updated for upstream release

* Sat Aug 30 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.2-1
- Updated for upstream release

* Fri Aug 29 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1-3
- Updated from review notes

* Thu Aug 28 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1-2
- Updated from review notes

* Tue Aug 26 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1-1
- Initial Version
