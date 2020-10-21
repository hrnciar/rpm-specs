# python3-pip is provided by RHEL 7.7+
%global with_python3 0
%global with_python3_other 1
%global build_wheel 0
%global with_tests 0

%global srcname pip
%if 0%{?build_wheel}
%global python2_wheelname %{srcname}-%{version}-py2.py3-none-any.whl
%if 0%{?with_python3}
%global python3_wheelname %python2_wheelname
%endif
%endif

Name:           python-%{srcname}-epel
Version:        8.1.2
Release:        14%{?dist}
Summary:        A tool for installing and managing Python packages

# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:
# distlib: Python
# html5lib: MIT
# six: MIT
# colorama: BSD
# requests: ASL 2.0
# CacheControl: ASL 2.0
# lockfile: MIT
# progress: ISC
# ipaddress: Python
# packaging: ASL 2.0 or BSD
# pyparsing: MIT
# retrying ASL 2.0
# pkg_resources (setuptools): MIT
# chardet: LGPLv2+
# urllib3: MIT

License:        MIT and BSD and ASL 2.0 and ISC and Python and (ASL 2.0 or BSD) and LGPLv2+
URL:            http://www.pip-installer.org
Source0:        %{pypi_source}

BuildArch:      noarch

# to get tests:
# git clone https://github.com/pypa/pip && cd pip
# git checkout 8.0.2 && tar -czvf pip-8.0.2-tests.tar.gz tests/
%if 0%{?with_tests}
Source1:        pip-8.1.2-tests.tar.gz
%endif

# Patch until the following issue gets implemented upstream:
# https://github.com/pypa/pip/issues/1351
Patch0:         allow-stripping-given-prefix-from-wheel-RECORD-files.patch

# Fix `pip install` failure in FIPS mode
# Resolves: rhbz#1430774
Patch1:         Fix-pip-install-in-FIPS-mode.patch

# Patch for CVE in the bundled urllib3
# CVE-2018-20060 Cross-host redirect does not remove Authorization header allow for credential exposure
# https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2018-20060
Patch2:         CVE-2018-20060.patch

# Patch for CVE in the bundled urllib3
# CVE-2019-11236 CRLF injection due to not encoding the '\r\n' sequence leading to possible attack on internal service
# https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2019-11236
Patch3:         CVE-2019-11236.patch

# Patch for CVE in the bundled requests
# CVE-2018-18074 Redirect from HTTPS to HTTP does not remove Authorization header
# This patch fixes both the CVE
# https://bugzilla.redhat.com/show_bug.cgi?id=1643829
# and the subsequent regression
# https://github.com/psf/requests/pull/4851
Patch4:         CVE-2018-18074.patch

# Patch for pip install <url> allow directory traversal, leading to arbitrary file write
# - Upstream PR: https://github.com/pypa/pip/pull/6418/files
# - Bugzilla: https://bugzilla.redhat.com/show_bug.cgi?id=1868016
# Patch9 fixes the issue
# Patch10 adds unit tests for the issue
Patch9:         pip-directory-traversal-security-issue.patch
Patch10:        pip-directory-traversal-security-issue-tests.patch

%description
Pip is a replacement for easy_install.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.


%package -n python2-%{srcname}
Summary:        A tool for installing and managing Python 2 packages
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?with_tests}
BuildRequires:  git
BuildRequires:  bzr
BuildRequires:  python-mock
BuildRequires:  pytest
BuildRequires:  python-pretend
BuildRequires:  python-freezegun
BuildRequires:  python-pytest-capturelog
BuildRequires:  python-scripttest
BuildRequires:  python-virtualenv
%endif
%if 0%{?build_wheel}
BuildRequires:  python2-pip
BuildRequires:  python2-wheel
%endif
Requires:       python-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

# from pip/_vendor/vendor.txt
Provides:       bundled(python2-distlib) = 0.2.3
Provides:       bundled(python2-html5lib) = 1.0~b8
Provides:       bundled(python2-six) = 1.10.0
Provides:       bundled(python2-colorama) = 0.3.7
Provides:       bundled(python2-requests) = 2.10.0
Provides:       bundled(python2-CacheControl) = 0.11.6
Provides:       bundled(python2-lockfile) = 0.12.2
Provides:       bundled(python2-progress) = 1.2
Provides:       bundled(python2-ipaddress) = 1.0.16
Provides:       bundled(python2-packaging) = 16.7
Provides:       bundled(python2-pyparsing) = 2.1.1
Provides:       bundled(python2-retrying) = 1.3.3
# from pip/_vendor/README.rst
Provides:       bundled(python2-setuptools) = 21.0.0
# from pip/_vendor/requests/packages
Provides:       bundled(python2-chardet) = 2.3.0
Provides:       bundled(python2-urllib3) = 1.15.1

%description -n python2-%{srcname}
Pip is a replacement for easy_install.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A tool for installing and managing Python3 packages
%if 0%{?with_python3_other}
# The python3 subpackages share the pip3 bash completion file, so force them to
# be upgraded together.
Conflicts:      python%{python3_other_pkgversion}-%{srcname} < %{version}-%{release}
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-pytest-capturelog
BuildRequires:  python%{python3_pkgversion}-scripttest
BuildRequires:  python%{python3_pkgversion}-virtualenv
%endif
%if 0%{?build_wheel}
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
%endif
Requires:       python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

# from pip/_vendor/vendor.txt
Provides:       bundled(python%{python3_pkgversion}-distlib) = 0.2.3
Provides:       bundled(python%{python3_pkgversion}-html5lib) = 1.0~b8
Provides:       bundled(python%{python3_pkgversion}-six) = 1.10.0
Provides:       bundled(python%{python3_pkgversion}-colorama) = 0.3.7
Provides:       bundled(python%{python3_pkgversion}-requests) = 2.10.0
Provides:       bundled(python%{python3_pkgversion}-CacheControl) = 0.11.6
Provides:       bundled(python%{python3_pkgversion}-lockfile) = 0.12.2
Provides:       bundled(python%{python3_pkgversion}-progress) = 1.2
Provides:       bundled(python%{python3_pkgversion}-ipaddress) = 1.0.16
Provides:       bundled(python%{python3_pkgversion}-packaging) = 16.7
Provides:       bundled(python%{python3_pkgversion}-pyparsing) = 2.1.1
Provides:       bundled(python%{python3_pkgversion}-retrying) = 1.3.3
# from pip/_vendor/README.rst
Provides:       bundled(python%{python3_pkgversion}-setuptools) = 21.0.0
# from pip/_vendor/requests/packages
Provides:       bundled(python%{python3_pkgversion}-chardet) = 2.3.0
Provides:       bundled(python%{python3_pkgversion}-urllib3) = 1.15.1

%description -n python%{python3_pkgversion}-%{srcname}
Pip is a replacement for `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.
%endif # with_python3


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{srcname}
Summary:        A tool for installing and managing Python3 packages
%if 0%{?with_python3}
# The python3 subpackages share the pip3 bash completion file, so force them to
# be upgraded together.
Conflicts:      python%{python3_pkgversion}-%{srcname} < %{version}-%{release}
%endif
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%if 0%{?with_tests}
BuildRequires:  python%{python3_other_pkgversion}-mock
BuildRequires:  python%{python3_other_pkgversion}-pytest
BuildRequires:  python%{python3_other_pkgversion}-pretend
BuildRequires:  python%{python3_other_pkgversion}-freezegun
BuildRequires:  python%{python3_other_pkgversion}-pytest-capturelog
BuildRequires:  python%{python3_other_pkgversion}-scripttest
BuildRequires:  python%{python3_other_pkgversion}-virtualenv
%endif
%if 0%{?build_wheel}
BuildRequires:  python%{python3_other_pkgversion}-pip
BuildRequires:  python%{python3_other_pkgversion}-wheel
%endif
Requires:       python%{python3_other_pkgversion}-setuptools

# from pip/_vendor/vendor.txt
Provides:       bundled(python%{python3_other_pkgversion}-distlib) = 0.2.3
Provides:       bundled(python%{python3_other_pkgversion}-html5lib) = 1.0~b8
Provides:       bundled(python%{python3_other_pkgversion}-six) = 1.10.0
Provides:       bundled(python%{python3_other_pkgversion}-colorama) = 0.3.7
Provides:       bundled(python%{python3_other_pkgversion}-requests) = 2.10.0
Provides:       bundled(python%{python3_other_pkgversion}-CacheControl) = 0.11.6
Provides:       bundled(python%{python3_other_pkgversion}-lockfile) = 0.12.2
Provides:       bundled(python%{python3_other_pkgversion}-progress) = 1.2
Provides:       bundled(python%{python3_other_pkgversion}-ipaddress) = 1.0.16
Provides:       bundled(python%{python3_other_pkgversion}-packaging) = 16.7
Provides:       bundled(python%{python3_other_pkgversion}-pyparsing) = 2.1.1
Provides:       bundled(python%{python3_other_pkgversion}-retrying) = 1.3.3
# from pip/_vendor/README.rst
Provides:       bundled(python%{python3_other_pkgversion}-setuptools) = 21.0.0
# from pip/_vendor/requests/packages
Provides:       bundled(python%{python3_other_pkgversion}-chardet) = 2.3.0
Provides:       bundled(python%{python3_other_pkgversion}-urllib3) = 1.15.1

%description -n python%{python3_other_pkgversion}-%{srcname}
Pip is a replacement for easy_install.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.
%endif # with_python3_other


%prep
%setup -q -n %{srcname}-%{version}
%if 0%{?with_tests}
tar -xf %{SOURCE1}
%endif

%patch0 -p1
%patch1 -p1

# Patching of bundled libraries
pushd pip/_vendor/requests/packages/urllib3/
%patch2 -p1
%patch3 -p1
popd
pushd pip/_vendor/requests/
%patch4 -p1
popd

%patch9 -p1
%if 0%{?with_tests}
%patch10 -p1
%endif

sed -i '1d' pip/__init__.py


%build
%if 0%{?build_wheel}
%py2_build_wheel
%else
%py2_build
%endif

%if 0%{?with_python3}
%if 0%{?build_wheel}
%{?with_python3_other:%py3_other_build_wheel}
%py3_build_wheel
%else
%{?with_python3_other:%py3_other_build}
%py3_build
%endif
%endif # with_python3


%install
%if 0%{?build_wheel}
%if 0%{?with_python3_other}
%py3_other_install_wheel %{python3_wheelname}
# TODO: we have to remove this by hand now, but it'd be nice if we wouldn't have to
# (pip install wheel doesn't overwrite)
rm %{buildroot}%{_bindir}/pip{,3}
%endif # with_python3_other
%if 0%{?with_python3}
%py3_install_wheel %{python3_wheelname}
%endif # with_python3
# TODO: we have to remove this by hand now, but it'd be nice if we wouldn't have to
# (pip install wheel doesn't overwrite)
rm %{buildroot}%{_bindir}/pip
%else
%if 0%{?with_python3_other}
%py3_other_install
rm %{buildroot}%{_bindir}/pip{,3}
%endif
%if 0%{?with_python3}
%py3_install
rm %{buildroot}%{_bindir}/pip
%endif
%endif

%if 0%{?build_wheel}
%py2_install_wheel %{python2_wheelname}
%else
%py2_install
%endif

mkdir -p %{buildroot}%{bash_completion_dir}
PYTHONPATH=%{buildroot}%{python_sitelib} \
    %{buildroot}%{_bindir}/pip completion --bash \
    > %{buildroot}%{bash_completion_dir}/pip
%if 0%{?with_python3_other} && ! 0%{?with_python3}
PYTHONPATH=%{buildroot}%{python3_other_sitelib} \
    %{buildroot}%{_bindir}/pip%{python3_other_version} completion --bash \
    > %{buildroot}%{bash_completion_dir}/pip3
%endif
%if 0%{?with_python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{buildroot}%{_bindir}/pip3 completion --bash \
    > %{buildroot}%{bash_completion_dir}/pip3
%endif
pips2=pip
pips3=pip3
for pip in %{buildroot}%{_bindir}/pip*; do
    pip=$(basename $pip)
    case $pip in
        pip2*)
            pips2="$pips2 $pip"
            ln -s pip %{buildroot}%{bash_completion_dir}/$pip
            ;;
%if 0%{?with_python3}
        pip3?*)
            pips3="$pips3 $pip"
            ln -s pip3 %{buildroot}%{bash_completion_dir}/$pip
            ;;
%else
%if 0%{?with_python3_other}
        pip3?*)
            pips3="$pips3 $pip"
            mv %{buildroot}%{bash_completion_dir}/pip3 %{buildroot}%{bash_completion_dir}/$pip
            ;;
%endif
%endif
    esac
done
%if 0%{?with_python3}
sed -i -e "s/^\\(complete.*\\) pip\$/\\1 $pips3/" \
    -e s/_pip_completion/_pip3_completion/ \
    %{buildroot}%{bash_completion_dir}/pip3
%endif
sed -i -e "s/^\\(complete.*\\) pip\$/\\1 $pips2/" \
    %{buildroot}%{bash_completion_dir}/pip

%if 0%{?with_tests}
%check
py.test -m 'not network'
%{?with_python3:py.test-%{python3_version} -m 'not network'}
%{?with_python3_other:py.test-%{python3_other_version} -m 'not network'}
%endif


%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst docs
%{_bindir}/pip
%{_bindir}/pip2
%{_bindir}/pip%{python2_version}
%{python_sitelib}/pip
%{python_sitelib}/pip-%{version}-py%{python2_version}.egg-info
%dir %{_datadir}/bash-completion
%dir %{bash_completion_dir}
%{bash_completion_dir}/pip
%{bash_completion_dir}/pip2
%{bash_completion_dir}/pip%{python2_version}

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst docs
%{_bindir}/pip3
%{_bindir}/pip%{python3_version}
%{python3_sitelib}/pip
%{python3_sitelib}/pip-%{version}-py%{python3_version}.egg-info
%dir %{_datadir}/bash-completion
%dir %{bash_completion_dir}
%{bash_completion_dir}/pip3
%{bash_completion_dir}/pip%{python3_version}
%endif # with_python3

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst docs
%{_bindir}/pip%{python3_other_version}
%{python3_other_sitelib}/pip
%{python3_other_sitelib}/pip-%{version}-py%{python3_other_version}.egg-info
%dir %{_datadir}/bash-completion
%dir %{bash_completion_dir}
%{bash_completion_dir}/pip%{python3_other_version}
%if 0%{?with_python3}
%{bash_completion_dir}/pip3
%endif
%endif # with_python3_other

%changelog
* Wed Sep 02 2020 Tomas Orsava <torsava@redhat.com> - 8.1.2-14
- Patch for pip install <url> allow directory traversal, leading to arbitrary file write
Resolves: rhbz#1868137

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 29 2020 Lumír Balhar <lbalhar@redhat.com> - 8.1.2-12
- Add a patch to fix CVE-2018-18074 in bundled requests
Resolves: rhbz#1778149

* Mon Jan 13 2020 Lumír Balhar <lbalhar@redhat.com> - 8.1.2-11
- Add two new patches for CVEs in bundled urllib3
Resolves: rhbz#1649153
Resolves: rhbz#1700824

* Mon Aug 12 2019 Miro Hrončok <mhroncok@redhat.com> - 8.1.2-10
- python34-pip: Do not conflict with python36-pip when not needed

* Fri Aug 02 2019 Miro Hrončok <mhroncok@redhat.com> - 8.1.2-9
- Remove python36-pip (obsoleted by python3-pip from RHEL 7.7+)
- Rename the source package to python-pip-epel (python-pip is in RHEL 7.7+)

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 8.1.2-8
- Rebuilt to change main python from 3.4 to 3.6

* Thu Jan 10 2019 Carl George <carl@george.computer> - 8.1.2-7
- Simplify bash-completion just for EL7
- Add python36 subpackage

* Wed Apr 04 2018 Tomas Orsava <torsava@redhat.com> - 8.1.2-6
- Added Patch 1: Fix `pip install` failure in FIPS mode
Resolves: rhbz#1430774

* Fri Nov 18 2016 Orion Poplawski <orion@cora.nwra.com> - 8.1.2-5
- Enable EPEL Python 3 builds
- Use new python macros
- Cleanup spec
- Without wheel

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-4
- Updated the test sources

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-3
- Moved python-pip into the python2-pip subpackage
- Added the python_provide macro

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-1
- Update to 8.1.2
- Moved to a new PyPI URL format
- Updated the prefix-stripping patch because of upstream changes in pip/wheel.py

* Mon Feb 22 2016 Slavek Kabrda <bkabrda@redhat.com> - 8.0.2-1
- Update to 8.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 7.1.0-3
- Rebuilt for Python3.5 rebuild
- With wheel set to 1

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 7.1.0-2
- Rebuilt for Python3.5 rebuild

* Wed Jul 01 2015 Slavek Kabrda <bkabrda@redhat.com> - 7.1.0-1
- Update to 7.1.0

* Tue Jun 30 2015 Ville Skyttä <ville.skytta@iki.fi> - 7.0.3-3
- Install bash completion
- Ship LICENSE.txt as %%license where available

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 7.0.3-1
- Update to 7.0.3

* Fri Mar 06 2015 Matej Stuchlik <mstuchli@redhat.com> - 6.0.8-1
- Update to 6.0.8

* Thu Dec 18 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.5.6-5
- Only enable tests on Fedora.

* Mon Dec 01 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-4
- Add tests
- Add patch skipping tests requiring Internet access

* Tue Nov 18 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-3
- Added patch for local dos with predictable temp dictionary names
  (http://seclists.org/oss-sec/2014/q4/655)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-1
- Update to 1.5.6

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-4
- Rebuild as wheel for Python 3.4

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-3
- Disable build_wheel

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-2
- Rebuild as wheel for Python 3.4

* Mon Apr 07 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-1
- Updated to 1.5.4

* Mon Oct 14 2013 Tim Flink <tflink@fedoraproject.org> - 1.4.1-1
- Removed patch for CVE 2013-2099 as it has been included in the upstream 1.4.1 release
- Updated version to 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-4
- Fix for CVE 2013-2099

* Thu May 23 2013 Tim Flink <tflink@fedoraproject.org> - 1.3.1-3
- undo python2 executable rename to python-pip. fixes #958377
- fix summary to match upstream

* Mon May 06 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.1-2
- Fix main package Summary, it's for Python 2, not 3 (#877401)

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-1
- Update to 1.3.1, fix for CVE-2013-1888.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-2
- Fixing files for python3-pip

* Thu Oct 04 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-1
- Update to upstream 1.2.1
- Change binary from pip-python to python-pip (RHBZ#855495)
- Add alias from python-pip to pip-python, to be removed at a later date

* Tue May 15 2012 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- update to 1.0.2 and added python3 subpackage

* Wed Jun 22 2011 Tim Flink <tflink@fedoraproject.org> - 0.8.3-1
- update to 0.8.3 and project home page

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Luke Macken <lmacken@redhat.com> - 0.8.2-1
- update to 0.8.2 of pip
* Mon Aug 30 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.8-1
- update to 0.8 of pip
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 7 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.2-1
- update to 0.7.2 of pip
* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.1-1
- update to 0.7.1 of pip
* Fri Jan 1 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1.4
- fix dependency issue
* Fri Dec 18 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-2
- fix spec file 
* Thu Dec 17 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-1
- upgrade to 0.6.1 of pip
* Mon Aug 31 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.4-1
- Initial package

