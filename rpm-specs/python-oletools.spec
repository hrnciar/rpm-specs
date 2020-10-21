Name:           python-oletools
Version:        0.55
Release:        5%{?dist}
Summary:        Tools to analyze Microsoft OLE2 files

# oletools/*.py: BSD
# oletools/olevba*.py: BSD and MIT
# oletools/thirdparty/xxxswf/*.py: No license specified
# oletools/thirdparty/xglob/*.py: BSD
# oletools/thirdparty/tablestream/*.py: BSD
# oletools/thirdparty/zipfile27/*.py: Python
# oletools/thirdparty/msoffcrypto/*.py: MIT
License:        BSD and MIT and Python
URL:            https://www.decalage.info/python/oletools
#               https://github.com/decalage2/oletools/releases
#               https://github.com/nolze/msoffcrypto-tool/releases

%global         srcname oletools


# Build with python3 package by default
%bcond_without  python3

# Build without python2 package for newer releases f32+ and rhel8+
# Use python3 executables by default on releases f32+ and rhel8+
%if (0%{?fedora} && 0%{?fedora} >= 32 ) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
%bcond_with     python2
%bcond_without  python3_default
%else
%bcond_without  python2
%bcond_with     python3_default
%endif

# Bundles taken from oletools-0.54.2b/oletools/thirdparty
%global         _provides \
Provides:       bundled(oledump) = 0.0.5 \
Provides:       bundled(tablestream) = 0.09 \
Provides:       bundled(xglob) = 0.07 \
Provides:       bundled(xxxswf) = 0.1


%global         _description %{expand:
The python-oletools is a package of python tools from Philippe Lagadec
to analyze Microsoft OLE2 files (also called Structured Storage,
Compound File Binary Format or Compound Document File Format),
such as Microsoft Office documents or Outlook messages, mainly for
malware analysis, forensics and debugging.
It is based on the olefile parser.
See http://www.decalage.info/python/oletools for more info.
}

Source0:        https://github.com/decalage2/oletools/archive/v%{version}/%{srcname}-%{version}.tar.gz

# For now bundle the msoffcrypto-tool for python2 - new requirement for the oletools not used by anything else
# but in Fedora we have only the python3 package for it
Source1:        https://github.com/nolze/msoffcrypto-tool/archive/v4.10.1/msoffcrypto-tool-4.10.1.tar.gz

# Remove the bundled libraries from the build. Use the system libraries instead
Patch0:         %{name}-01-thirdparty.patch

%if 0%{?with_python2}
# Bundle msoffcrypto instead of using one from pip
Patch1:         %{name}-02-msoffcrypto.patch
%endif

BuildArch:      noarch

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-colorclass
BuildRequires:  python%{python3_pkgversion}-easygui
BuildRequires:  python%{python3_pkgversion}-olefile
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pymilter
BuildRequires:  python%{python3_pkgversion}-prettytable
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-msoffcrypto
%endif

# python2-pymilter at F28+, python-pymilter at EPEL 7
# python2-pyparsing and python3-pyparsing at Fedora, pyparsing at RHEL 7
# python2-easygui only at F28+ and EPEL7+
# python2-prettytable and python3-prettytable at Fedora, python-prettytable at EPEL 7
%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-colorclass
BuildRequires:  python2-easygui
BuildRequires:  python2-olefile
BuildRequires:  python2-cryptography
%endif

%if 0%{?with_python2} && 0%{?fedora}
BuildRequires:  python2-pymilter
BuildRequires:  python2-pyparsing
BuildRequires:  python2-prettytable
%endif

# python2 packages for EPEL 7
%if 0%{?with_python2} && 0%{?rhel}
BuildRequires:  pyparsing
BuildRequires:  python-prettytable
BuildRequires:  python-pymilter
%endif

%description    %{_description}



%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
%{_provides}

Requires:       python2-olefile
Requires:       python2-colorclass

# python2-pymilter only at F28+, python-pymilter at EPEL 7
# python2-pyparsing at Fedora, pyparsing at RHEL 7
# python2-prettytable only at Fedora 28+, python-prettytable at EPEL 7
%if 0%{?fedora}
Requires:       python2-pyparsing
Requires:       python2-prettytable
Requires:       python2-pymilter
%else
Requires:       pyparsing
Requires:       python-prettytable
Requires:       python-pymilter
%endif

# python2-easygui only at F28+ and EPEL 7
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 7
Requires:       python2-easygui
%else
Requires:       python-easygui
%endif

# Used by msoffcrypto
Requires:       python2-cryptography
Provides:       bundled(msoffcrypto-tool) = 4.10.1

%description -n python2-%{srcname} %{_description}

Python2 version.
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%{_provides}

Requires:       python%{python3_pkgversion}-pymilter
Requires:       python%{python3_pkgversion}-pyparsing
Requires:       python%{python3_pkgversion}-colorclass
Requires:       python%{python3_pkgversion}-easygui
Requires:       python%{python3_pkgversion}-olefile
Requires:       python%{python3_pkgversion}-prettytable
Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-msoffcrypto

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python3 version.

%endif


%package -n python-%{srcname}-doc
Summary:        Documentation files for %{name}
%if 0%{?with_python2}
%{?python_provide:%python_provide python2-%{srcname}-doc}
%endif
%if 0%{?with_python3}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-doc}
%endif

%description -n python-%{srcname}-doc %{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}

# Use globally installed python modules instead of bundled ones
for i in colorclass easygui olefile prettytable pyparsing; do
  rm -rf "oletools/thirdparty/${i}"
done

sed -i -e '
  s|from oletools.thirdparty import olefile|import olefile|;
  s|from oletools.thirdparty.olefile import olefile|from olefile import olefile|;
  s|from oletools.thirdparty.prettytable import prettytable|import prettytable|;
  s|from oletools.thirdparty.pyparsing.pyparsing import|from pyparsing import|;
  s|from thirdparty.pyparsing.pyparsing import|from pyparsing import|;
  s|from .thirdparty import olefile|import olefile|;
  s|from oletools.thirdparty.easygui import easygui|import easygui|;
' */*.py

%if 0%{?with_python2}
# for now bundle msoffcrypto-tool for python2
tar xvf %{SOURCE1}
mv msoffcrypto-tool-4.10.1/msoffcrypto oletools/thirdparty/
cp msoffcrypto-tool-4.10.1/LICENSE.txt oletools/thirdparty/msoffcrypto/LICENSE.txt
sed -i -e 's|import msoffcrypto| from oletools.thirdparty import msoffcrypto|;' oletools/crypto.py
%endif

%if ( 0%{?rhel} && 0%{?rhel} == 8 )
# pyparsing on epel8 is 2.1.10
sed -i -e 's|pyparsing>=2\.2\.0|pyparsing>=2.1.10|g' requirements.txt setup.py
%endif


%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?with_python2} && 0%{?rhel} <= 7 
# on rhel7 weaken the pyparse requirements
sed -i -e 's|pyparsing>=2.2.0|pyparsing|' setup.py
%endif



%install
%if 0%{?with_python2}
# Install python2 files
%py2_install

# Move executables to python2 versioned names
pushd %{buildroot}%{_bindir}
  main=$(%{__python2} -c "import sys; sys.stdout.write('{0.major}'.format(sys.version_info))")  # e.g. 2
  full=$(%{__python2} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 2.7

  for i in ezhexviewer msodde mraptor olebrowse oledir olefile oleid olemap olemeta oleobj oletimes olevba pyxswf rtfobj; do
    mv -f "${i}" "${i}-${full}"
    ln -s "${i}-${full}" "${i}-${main}"

  done
popd

# Remove '\r' line ending and shebang from non-executable python libraries
for file in %{buildroot}%{python2_sitelib}/%{srcname}/{.,*,*/*}/*.py; do
  sed -e '1{\@^#![[:space:]]*/usr/bin/env python@d}' -e 's|\r$||' "${file}" > "${file}.new"
  touch -c -r "${file}" "${file}.new"
  mv -f "${file}.new" "${file}"
done
# Remove files that should either go to %%doc or to %%license
rm -rf %{buildroot}%{python2_sitelib}/%{srcname}/{doc,LICENSE.txt,README.*}
rm -f %{buildroot}%{python2_sitelib}/%{srcname}/thirdparty/xglob/LICENSE.txt
rm -f %{buildroot}%{python2_sitelib}/%{srcname}/thirdparty/xxxswf/LICENSE.txt
rm -f %{buildroot}%{python2_sitelib}/%{srcname}/thirdparty/msoffcrypto/LICENSE.txt
%endif

# Old pyparsing in RHEL 7 -> replace pyparsing.infixNotation by pyparsing.operatorPrecedence
%if 0%{?with_python2} && 0%{?rhel} && 0%{?rhel} < 8
sed -e 's|infixNotation|operatorPrecedence|g' -i %{buildroot}%{python2_sitelib}/%{srcname}/olevba.py
%endif



%if 0%{?with_python3}
# Install python3 files
%py3_install

# Move executables to python3 versioned names
pushd %{buildroot}%{_bindir}
  main=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}'.format(sys.version_info))")  # e.g. 3
  full=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 3.4

  # olevba and msraptor not considered stable by the author so are created with "3" by default
  mv olevba3 olevba
  mv mraptor3 mraptor

  for i in ezhexviewer msodde mraptor olebrowse oledir olefile oleid olemap olemeta oleobj oletimes olevba pyxswf rtfobj; do
    mv -f "${i}" "${i}-${full}"
    ln -s "${i}-${full}" "${i}-${main}"
  done
popd

# Remove '\r' line ending and shebang from non-executable python libraries
for file in %{buildroot}%{python3_sitelib}/%{srcname}/{.,*,*/*}/*.py; do
  sed -e '1{\@^#![[:space:]]*/usr/bin/env python@d}' -e 's|\r$||' "${file}" > "${file}.new"
  touch -c -r "${file}" "${file}.new"
  mv -f "${file}.new" "${file}"
done

%if 0%{?with_python2}
# Remove the msoffcrypto bundling for python3 and use the system package instead
sed -i -e 's|from oletools.thirdparty import msoffcrypto|import msoffcrypto|;' %{buildroot}%{python3_sitelib}/%{srcname}/crypto.py
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/msoffcrypto
%else
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/msoffcrypto/LICENSE.txt
%endif

# Remove files that should either go to %%doc or to %%license
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/{doc,LICENSE.txt,README.*}
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/xglob/LICENSE.txt
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/xxxswf/LICENSE.txt
%endif

# Create trivial name symlinks to the default executables of preffered python version
# For example in FC31 exists python3 package, but puthon2 is the preffered one
pushd %{buildroot}%{_bindir}
for i in ezhexviewer msodde mraptor olebrowse oledir olefile oleid olemap olemeta oleobj oletimes olevba pyxswf rtfobj; do
%if 0%{?with_python3_default}
    full=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 3.4
%else
    # For now the 2.7 is the default version, python3 support is experimental
    full=$(%{__python2} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 2.7
%endif
    ln -s "${i}-${full}" "${i}"
done
popd


# Prepare licenses from bundled code for later %%license usage
mv -f %{srcname}/thirdparty/xglob/LICENSE.txt xglob-LICENSE.txt
mv -f %{srcname}/thirdparty/xxxswf/LICENSE.txt xxxswf-LICENSE.txt
%if 0%{?with_python2}
mv -f %{srcname}/thirdparty/msoffcrypto/LICENSE.txt msoffcrypto-LICENSE.txt
%endif


%check
%if 0%{?with_python2}

# On Fedora the oleobj test fails with python2 and version 0.54.2b.
# Run the test, but pass it for now.
# https://github.com/decalage2/oletools/issues/503
%if 0%{?fedora}
PYTHONIOENCODING=utf8 %{__python2} setup.py test || true
%endif

%if 0%{?rhel}
# On RHEL7 the tests fail due to version incompatibilities with unit tests
%{__python2} setup.py test || true
%endif

%endif

%if 0%{?with_python3}

%if 0%{?fedora}
# FC31 - ooxml.py fails
# https://github.com/decalage2/oletools/issues/504
%{__python3} setup.py test || true
%endif

# RHEL7 - tests should pass OK when executed manually, but fail on ascii encoding
# https://kojipkgs.fedoraproject.org//work/tasks/1422/38871422/build.log
# RHEL8 - absence of dependency pyparsing>=2.2.0, pyparsing on RHEL8 is 2.1.10-7.el8
%if 0%{?rhel}
%{__python3} setup.py test || true
%endif

%endif


%if 0%{?with_python2}
# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%license %{srcname}/LICENSE.txt xglob-LICENSE.txt xxxswf-LICENSE.txt msoffcrypto-LICENSE.txt
%doc README.md
%{python2_sitelib}/*
%{_bindir}/ezhexviewer-2*
%{_bindir}/mraptor-2*
%{_bindir}/msodde-2*
%{_bindir}/olebrowse-2*
%{_bindir}/oledir-2*
%{_bindir}/oleid-2*
%{_bindir}/olefile-2*
%{_bindir}/olemap-2*
%{_bindir}/olemeta-2*
%{_bindir}/oleobj-2*
%{_bindir}/oletimes-2*
%{_bindir}/olevba-2*
%{_bindir}/pyxswf-2*
%{_bindir}/rtfobj-2*
%endif
%if 0%{?with_python2} && ! 0%{?with_python3_default}
%{_bindir}/ezhexviewer
%{_bindir}/mraptor
%{_bindir}/msodde
%{_bindir}/olebrowse
%{_bindir}/oledir
%{_bindir}/oleid
%{_bindir}/olefile
%{_bindir}/olemap
%{_bindir}/olemeta
%{_bindir}/oleobj
%{_bindir}/oletimes
%{_bindir}/olevba
%{_bindir}/pyxswf
%{_bindir}/rtfobj
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license %{srcname}/LICENSE.txt xglob-LICENSE.txt xxxswf-LICENSE.txt
%doc README.md
%{python3_sitelib}/*
%{_bindir}/ezhexviewer-3*
%{_bindir}/msodde-3*
%{_bindir}/olebrowse-3*
%{_bindir}/oledir-3*
%{_bindir}/oleid-3*
%{_bindir}/olefile-3*
%{_bindir}/olemap-3*
%{_bindir}/olemeta-3*
%{_bindir}/oleobj-3*
%{_bindir}/oletimes-3*
# ModuleNotFoundError: No module named 'cStringIO'
%{_bindir}/olevba-3*
# ModuleNotFoundError: No module named 'cStringIO'
%{_bindir}/mraptor-3*
%{_bindir}/pyxswf-3*
%{_bindir}/rtfobj-3*
%endif
%if 0%{?with_python3} && 0%{?with_python3_default}
%{_bindir}/ezhexviewer
%{_bindir}/mraptor
%{_bindir}/msodde
%{_bindir}/olebrowse
%{_bindir}/oledir
%{_bindir}/oleid
%{_bindir}/olefile
%{_bindir}/olemap
%{_bindir}/olemeta
%{_bindir}/oleobj
%{_bindir}/oletimes
%{_bindir}/olevba
%{_bindir}/pyxswf
%{_bindir}/rtfobj
%endif


%files -n python-%{srcname}-doc
%doc %{srcname}/doc/*
%doc cheatsheet


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Robert Scheck <robert@fedoraproject.org> 0.55-4
- Require python-setuptools during build-time explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.55-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Michal Ambroz <rebus AT_ seznam.cz> - 0.55-1
- bump to bugfix release 0.55

* Sun Nov 10 2019 Michal Ambroz <rebus AT_ seznam.cz> - 0.54.2-2
- use the msoffcrypto bundling only for python2 subpackage
- use python3-msoffcrypto for python3 package

* Fri Nov 08 2019 Michal Ambroz <rebus AT_ seznam.cz> - 0.54.2-1
- bump to release 0.54.2
- stop building the python2 for fc32+ epel8+
- add missing msoffcrypto python module
- fix python36 dependencies for EPEL7

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.51-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.51-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.51-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Robert Scheck <robert@fedoraproject.org> 0.51-3
- Correct line endings and remove shebang from non-executable
  python libraries (#1505374 #c5)
- Clarify python3 related scripts in %%description (#1505374 #c4)
- Correct summary of -doc subpackage (#1505374 #c2)

* Thu Oct 05 2017 Robert Scheck <robert@fedoraproject.org> 0.51-2
- Various spec file enhancements (#1471561)
- Added spec file conditionals to build for EPEL 7

* Thu Jun 22 2017 Michal Ambroz <rebus at, seznam.cz> 0.51-1
- bump to 0.51 release

* Thu Jun 22 2017 Michal Ambroz <rebus at, seznam.cz> 0.51-0.3.dev11.b4b52d22
- gaps in python3 detected, using python2 as default

* Thu Jun 15 2017 Michal Ambroz <rebus at, seznam.cz> 0.51-0.2.dev11.b4b52d22
- initial version
