%global sum A Modbus Protocol Stack in Python
%global desc Pymodbus is a full Modbus protocol implementation using twisted for its \
asynchronous communications core. \
\
The library currently supports the following: \
\
Client Features \
\
    * Full read/write protocol on discrete and register \
    * Most of the extended protocol (diagnostic/file/pipe/setting/information) \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Payload builder/decoder utilities \
\
Server Features \
\
    * Can function as a fully implemented Modbus server \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Full server control context (device information, counters, etc) \
    * A number of backing contexts (database, redis, a slave device)

Name: pymodbus
Version: 2.3.0
Release: 4%{?dist}
Summary: %{sum}

License: BSD
URL: https://github.com/riptideio/pymodbus
Source0: https://github.com/riptideio/pymodbus/archive/v%{version}.tar.gz
# to avoid packaging ez_setup
Patch0: pymodbus-1.4.0-remove-ez_setup.patch
BuildArch: noarch
BuildRequires: python3-devel

%description
%{desc}


%package -n python3-%{name}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{name}}

BuildRequires: python3-setuptools
Requires: python3-twisted >= 12.2.0
Requires: python3-pyserial >= 2.6
# weak requirements for pymodbus.console
Recommends: python3-pyserial >= 3.4
Recommends: python3-prompt-toolkit >= 2.0
Recommends: python3-click

%description -n python3-%{name}
%{desc}


%prep
%setup -q -n %{name}-%{version}
%patch0 -F 2 -p1 -b .no_ez_setup

%build
%py3_build

%install
%py3_install

%{__rm} -rf $RPM_BUILD_ROOT%{python3_sitelib}/test

# install LICENSE, Changelog and READMEs
%{__mkdir} -p %{buildroot}%{_docdir}/%{name}
%{__install} -m 644 -p LICENSE %{buildroot}%{_docdir}/%{name}
%{__install} -m 644 -p CHANGELOG.rst %{buildroot}%{_docdir}/%{name}/CHANGELOG
%{__install} -m 644 -p README.rst %{buildroot}%{_docdir}/%{name}/
%{__install} -m 644 -p pymodbus/repl/README.md %{buildroot}%{_docdir}/%{name}/

%files -n python3-%{name}
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/{CHANGELOG,*.rst,*.md}
%{_bindir}/pymodbus.console
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Christian Krause <chkr@fedoraproject.org> - 2.3.0-1
- Updated to the latest upstream release 2.3.0
- Removed patch for dependency issue (fixed upstream)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Christian Krause <chkr@fedoraproject.org> - 2.2.0-2
- Fix dependency issue (package can't be installed since a fixed
  version of python-six was required)

* Fri May 10 2019 Christian Krause <chkr@fedoraproject.org> - 2.2.0-1
- Updated to the latest upstream release 2.2.0
- Add pymodbus.console with weak requirements to allow a minimal installation

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-4
- Remove python2 subpackage (#1627381)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Christian Krause <chkr@fedoraproject.org> - 1.5.1-1
- Updated to the latest upstream release 1.5.1

* Thu May 03 2018 Christian Krause <chkr@fedoraproject.org> - 1.5.0-1
- Updated to the latest upstream release 1.5.0

* Thu Apr 19 2018 Christian Krause <chkr@fedoraproject.org> - 1.4.0-1
- Updated to the latest upstream release 1.4.0
- Updated patch to disable ez_setup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Tomas Hozza <thozza@redhat.com> - 1.3.1-1
- Updated project and source URL, the original was redirected
- Updated to the latest upstream release 1.3.1
- Provide Python3 version of the package
- Install LICENSE and CHANGELOG
- Removed Requires on nosetest as tests are not shipped

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 09 2015 Christian Krause <chkr@fedoraproject.org> - 1.2.0-1
- Update to new upstream release 1.2.0
- Add patch to avoid installation of ez_setup
- Change URL and Source URL
- Adjust requirements

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.0-7
- Replace the python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Christian Krause <chkr@fedoraproject.org> - 0.9.0-1
- Initial Spec file

