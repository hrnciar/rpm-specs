%global pname pykwalify

%if 0%{?rhel} && 0%{?rhel} < 8
%global with_python2 1
%global default_python 2
%else
%global default_python 3
%endif
%global with_python3 1

Name:           python-%{pname}
Version:        1.7.0
Release:        9%{?dist}
Summary:        Python lib/cli for JSON/YAML schema validation

License:        MIT
URL:            https://github.com/grokzen/pykwalify
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
It is a YAML/JSON validation library.
This framework is a port with a lot added functionality
of the java version of the framework kwalify that can be
found at: http://www.kuwata-lab.com/kwalify/

%if 0%{?with_python2}
%package -n     python2-%{pname}
Summary:        Python lib/cli for JSON/YAML schema validation
%{?python_provide:%python_provide python2-%{pname}}

Requires:       python2-docopt
Requires:       python2-pyyaml
Requires:       python2-dateutil
Requires:       python2-setuptools

%description -n python2-%{pname}
It is a YAML/JSON validation library.
This framework is a port with a lot added functionality
of the java version of the framework kwalify that can be
found at: http://www.kuwata-lab.com/kwalify/
%endif

%if 0%{?with_python3}
%package -n     python3-%{pname}
Summary:        Python lib/cli for JSON/YAML schema validation
%{?python_provide:%python_provide python3-%{pname}}

Requires:       python3-docopt
Requires:       python3-PyYAML
Requires:       python3-dateutil
Requires:       python3-setuptools

%description -n python3-%{pname}
It is a YAML/JSON validation library.
This framework is a port with a lot added functionality
of the java version of the framework kwalify that can be
found at: http://www.kuwata-lab.com/kwalify/
%endif

%prep
%autosetup -n %{pname}-%{version}
rm -rf *.egg-info

sed -i "s|^PyYAML.*|PyYAML|g" requirements.txt
sed -i "s|PyYAML.*|PyYAML',|g" setup.py
sed -i "s|^python-dateutil.*|python-dateutil|g" requirements.txt
sed -i "s|python-dateutil.*|python-dateutil',|g" setup.py

%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
mv %{buildroot}%{_bindir}/%{pname} %{buildroot}%{_bindir}/python2-%{pname}
%endif

%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/%{pname} %{buildroot}%{_bindir}/python3-%{pname}
%endif

%if 0%{?default_python} >= 3
ln -s %{_bindir}/python3-%{pname} %{buildroot}%{_bindir}/%{pname}
%else
ln -s %{_bindir}/python2-%{pname} %{buildroot}%{_bindir}/%{pname}
%endif

%if 0%{?with_python2}
%files -n python2-%{pname}
%license LICENSE
%doc README.md
%if 0%{?default_python} <= 2
%{_bindir}/%{pname}
%endif
%{_bindir}/python2-%{pname}
%{python2_sitelib}/%{pname}
%{python2_sitelib}/%{pname}-%{version}-py?.?.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{pname}
%license LICENSE
%doc README.md
%if 0%{?default_python} >= 3
%{_bindir}/%{pname}
%endif
%{_bindir}/python3-%{pname}
%{python3_sitelib}/%{pname}
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Orion Poplawski <orion@nwra.com> - 1.7.0-8
- Build for python3 on EL7 (bz#1763554)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Michael Goodwin <xenithorb@fedoraproject.org> - 1.7.0-5
- Don't build python2 package for Fedora 31+
- New maintainer

* Fri Aug 30 2019 Marek Goldmann <mgoldman@redhat.com> - 1.7.0-4
- Use Python 3 for EPEL 8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Marek Goldmann <mgoldman@redhat.com> - 1.7.0-1
- Release 1.7.0
- Update url to fetch source from GitHub
- Drop strict version requirements in requirements.txt

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-3
- Rebuild for Python 3.6

* Mon Oct 17 2016 Chandan Kumar <chkumar@redhat.com> - 1.5.1-2
- Removed versions of BR
- Removed unnecessary files

* Thu Oct 13 2016 Chandan Kumar <chkumar@redhat.com> - 1.5.1-1
- Initial package.
