%global pypi_name jsonpickle

Name:           python-jsonpickle
# version is inserted into setup.cfg manually (see %%prep). Please be careful
# to use a Python-compatible version number if you need to set an "uncommon"
# version for this RPM.
Version:        1.4.1
Release:        5%{?dist}
Summary:        A module that allows any object to be serialized into JSON

License:        BSD
URL:            https://pypi.io/project/jsonpickle/
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
# upstream does not indicate which key ids are used to sign releases so this is
# purely "trust on first use":
#    https://github.com/jsonpickle/jsonpickle/issues/310
# gpg2 --recv-keys "FA41 BF59 C1B4 8E8C 5F3D A61C 8CE2 6BF4 A9F6 06B0"
# gpg2 --export --export-options export-minimal "FA41 BF59 C1B4 8E8C 5F3D A61C 8CE2 6BF4 A9F6 06B0" > gpgkey-FA41_BF59_C1B4_8E8C_5F3D_A61C_8CE2_6BF4_A9F6_06B0.gpg
Source2:        gpgkey-FA41_BF59_C1B4_8E8C_5F3D_A61C_8CE2_6BF4_A9F6_06B0.gpg

# Use importlib.metadata from the standard library on Python 3.8+
# https://github.com/jsonpickle/jsonpickle/commit/8debff4511089dad850930c702106a436275f118
Patch0:         jsonpickle-1.4.1-fix-py38.patch

# upstream ships a pytest.ini which also enables modules like cov/flake8.
# Some of these plugins are not available in Fedora and/or are just useful for
# developers (not distro releases).
Patch1:         jsonpickle-remove-pytest-modules.patch

# upstream relies on setuptools_scm >= 3.4.1 to get the version number from git
# metadata but RHEL only ships python3-setuptools_scm = 1.15.7.
# However we can just set the version explicitely with sed.
Patch2:         jsonpickle-drop-setuptools_scm.patch

%global _docdir_fmt %{name}

BuildArch:      noarch

%description
This module allows python objects to be serialized to JSON in a similar fashion
to the pickle module.

%package -n python3-jsonpickle
Summary:        A module that allows any object to be serialized into JSON
%{?python_provide:%python_provide python3-jsonpickle}

BuildRequires:  gnupg2
%if 0%{?rhel} || 0%{?fedora} <= 31
# Fedora 32+ uses Python 3.8
BuildRequires:  python3-importlib-metadata
%endif
%if 0%{?fedora} && 0%{?fedora} >= 33
# Upstream requires setuptools_scm[toml]>=3.4.1, that is:
BuildRequires:  python3-setuptools_scm >= 3.4.1
%else
# RHEL 8, Fedora <= 32
BuildRequires:  sed
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

# dependencies to test to run optional tests
BuildRequires:  python3-ecdsa
BuildRequires:  python3-numpy
BuildRequires:  python3-bson
# most of the test suite treats pandas as options but some test cases do not
BuildRequires:  python3-pandas
BuildRequires:  python3-pytest

BuildRequires:  python3-pymongo
BuildRequires:  python3-simplejson
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-toml
BuildRequires:  python3-ujson
%if 0%{?fedora}
# not packaged for Fedora EPEL 8
BuildRequires:  python3-demjson
BuildRequires:  python3-feedparser
# https://bugzilla.redhat.com/show_bug.cgi?id=1238787
# BuildRequires:  python3-ujson
%endif

%if 0%{?rhel} || 0%{?fedora} <= 31
Requires:  python3-importlib-metadata
%endif


%description -n python3-jsonpickle
This module allows python objects to be serialized to JSON in a similar fashion
to the pickle module.

This is the version for Python 3.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{pypi_name}-%{version}
%if 0%{?fedora} && 0%{?fedora} >= 32
%patch0 -p1
%endif
%patch1 -p1

rm -r *.egg-info
%if 0%{?rhel} || 0%{?fedora} <= 32
%patch2 -p1
sed -i 's/@@VERSION@@/%{version}/' setup.cfg
sed -i 's/setup_requires.*$//' setup.cfg
%endif


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version}


%files -n python3-jsonpickle
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-5
- Rebuilt for Python 3.9

* Mon May 18 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.1-4
- add EPEL 8 version

* Wed May 13 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.1-3
- add source file verification

* Mon Apr 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.1-2
- Add patch to fix build until 1.5.1 is released

* Tue Apr 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Mon Apr 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4-1
- 1.4

* Fri Feb 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.3-1
- 1.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.2-1
- 1.2, drop Python 2.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.1-1
- 1.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.4-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-2
- Conditionalize python3 package for EPEL7 compat.

* Thu Mar 30 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-2
- Rebuild for Python 3.6

* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.3-1
- 0.9.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Jon Ciesla <limburgher@gmail.com> - 0.9.2-3
- Disable tests to fix build.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul  2 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.2-1
- Update to latest version
- Clean up spec file a bit
- Add python3 subpackage (#1233915)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.0-1
- Latest upstream release, 0.4.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jan 23 2010 Ben Boeckel <MathStuf@gmail.com> - 0.3.1-1
- Update to 0.3.1

* Mon Nov 02 2009 Ben Boeckel <MathStuf@gmail.com> - 0.2.0-1
- Initial package
