# Python2 macros for EPEL
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python3}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global pypi_name gertty


Name:           python-gertty
Version:        1.6.0
Release:        6%{?dist}
Summary:        Gertty is a console-based interface to the Gerrit Code Review system

License:        ASL 2.0 
URL:            https://pypi.python.org/pypi/gertty
Source0:        https://pypi.python.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz 
Patch0:         fix_setup.cfg.patch

BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  python3-pbr



%global _description\
Gertty is a console-based interface to the Gerrit Code Review system. As\
compared to the web interface, the main advantages are: (a) Work flow -- the\
interface is designed to support a work flow similar to reading network news or\
mail. In particular, it is designed to deal with a large number of review\
requests across a large number of projects. (b) Offline Use -- Gertty syncs\
information about changes in subscribed projects to a local database and local\
git repositories. All review operations are performed against that database\
and then synced back to Gerrit. (c) Speed -- user actions modify locally\
cached content and need not wait for server interaction. (d) Convenience --\
because Gertty downloads all changes to local git repositories, a single\
command instructs it to checkout a change into that repositories for detailed\
examination or testing of larger changes.

%description %_description

%package -n python3-gertty
Summary: %summary
Requires: python3-pbr
Requires: python3-urwid
Requires: python3-sqlalchemy
Requires: python3-GitPython
Requires: python3-dateutil
Requires: python3-requests
Requires: python3-alembic
Requires: python3-pyyaml
Requires: python3-voluptuous
Requires: python3-ply
Requires: python3-six
%{?python_provide:%python_provide python3-gertty}

%description -n python3-gertty %_description

%prep
%setup -q -n %{pypi_name}-%{version}
%patch0 -p1 -b .

# Remove egg-info
rm -rf gertty.egg-info

# We handle requirements ourselves, remove requirements.txt
rm -rf requirements.txt

# Fix the wrong-file-end-of-line-encoding warning from rpmlint
sed -i 's/\r$//' LICENSE

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%files -n python3-gertty
%doc README.rst LICENSE CONTRIBUTING.rst
%doc %{_datadir}/%{pypi_name}/examples/*
%{_bindir}/*
%{python3_sitelib}/gertty-%{version}*
%{python3_sitelib}/%{pypi_name}


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild


* Mon May 20 2019 Kashyap Chamarthy - 1.6.0-1
- Update spec to Python 3
- New upstream release 1.6.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.5.0-1
- New upstream release 1.5.0

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-4
- Python 2 binary package renamed to python2-gertty
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.4.0-1
- New upstream release 1.4.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 27 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.2-1
- New upstream release 1.3.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.0-1
- New upstream release 1.3.0

* Wed Jun 10 2015 1.2.1 <kashyapc@fedoraproject.org> - 1.2.1-1
- New upstream release 1.2.1
- Thanks Paul Belanger <pabelanger@redhat.com> for the SPEC file
  changes:
   - Add missing dependency on python-six
   - Fix spelling-error lint warnings

* Fri Mar 6 2015 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.1.0-1
- New upstream release 1.1.0

* Mon Jan 5 2015 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.0.3-4
- New build that properly installs Alembic (with the help of
  package-data in setup.cfg)
- Fixes rhbz # 1178754

* Mon Dec 1 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.0.3-3
- Remove python-ordered dict from Requires, it is obsolete and
  is now provided by Python 2.7. Fedora is now at Python 2.7 (1022220)

* Wed Nov 19 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.0.3-2
- Fix rpmlint warnings (wrong-file-end-of-line-encoding)
- Fix and simplify RPM macros

* Mon Nov 17 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.0.3-1
- Initial package
