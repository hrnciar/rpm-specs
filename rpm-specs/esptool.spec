Name:           esptool
Version:        2.8
Release:        1%{?dist}
Summary:        A utility to communicate with the ROM bootloader in Espressif ESP8266

License:        GPLv2+
URL:            https://github.com/themadinventor/%{name}
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%?python_enable_dependency_generator

Provides:       %{name}.py = %{version}-%{release}

%description
%{name}.py A command line utility to communicate with the ROM bootloader in
Espressif ESP8266 WiFi microcontroller. Allows flashing firmware, reading back
firmware, querying chip parameters, etc. Developed by the community, not by
Espressif Systems.


%prep
%autosetup
pathfix.py -i %{__python3} -pn esp*.py

%build
%py3_build

# Shebangs in site-packages
grep -r '^#!' build/lib/
sed -i 1d $(grep -rl '^#' build/lib/)


%install
%py3_install
for NAME in %{name} espefuse espsecure ; do
  ln -s ./$NAME.py %{buildroot}%{_bindir}/$NAME
done


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{_bindir}/espefuse
%{_bindir}/espefuse.py
%{_bindir}/espsecure
%{_bindir}/espsecure.py
%{python3_sitelib}/esp*.py*
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info
%{python3_sitelib}/__pycache__/esp*.*.pyc

%changelog
* Thu May 28 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.8-1
- Update to 2.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-1
- Updated to 2.7 (#1742098)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-1
- Updated to 2.6 (#1642062)

* Tue Jul 31 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Updated to 2.5.0 (#1609436)

* Mon Jul 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-1
- Updated to 2.4.1 (#1592835)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-2
- Rebuilt for Python 3.7

* Sat Mar 03 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-1
- Updated to 2.3.1 (#1551162)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-1
- Updated to 2.2.1 (#1539948)
- Update shebang handling
- Use automatic dependency generator

* Wed Aug 23 2017 Miro Hrončok <mhroncok@redhat.com> - 2.1-1
- New version 2.1 (#1484381)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-1
- New version 2.0.1 (#1465005)

* Thu Jun 22 2017 Miro Hrončok <mhroncok@redhat.com> - 2.0-1
- New version 2.0 (#1425422)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Miro Hrončok <mhroncok@redhat.com> - 1.3-1
- New version (#1392643)
- Use Python 3

* Tue Sep 06 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-1
- Initial package.
