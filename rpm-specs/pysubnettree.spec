Name:           pysubnettree
Version:        0.33
Release:        1%{?dist}
Summary:        Python Module for CIDR Lookups

License:        BSD
URL:            https://github.com/zeek/pysubnettree
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

%description
The PySubnetTree package provides a Python data structure SubnetTree which
maps subnets given in CIDR notation (incl. corresponding IPv6 versions) to
Python objects. Lookups are performed by longest-prefix matching.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%doc CHANGES README
%license COPYING
%{python3_sitearch}/*

%changelog
* Mon Jun 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.33-1
- Update to lastest upstream release 0.33

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.32-2
- Rebuilt for Python 3.9

* Sun Feb 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.32-1
- Update to lastest upstream release 0.32

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.30-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.30-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.30-1
- Update to lastest upstream release 0.30

* Tue Mar 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.28-1
- Update to lastest upstream release 0.28

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.27-2
- Rebuilt for Python 3.7

* Sun Jul 01 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.27-1
- Update to lastest upstream release 0.27

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.26-1
- Update to lastest upstream release 0.26

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.24-7
- Rebuild for Python 3.6

* Tue Aug 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-6
- Fix FTBFS (rhbz#1307892)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-3
- Cleanup and py3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-1
- Update to lastest upstream release 0.24

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.23-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.23-3
- Fix macro

* Sun Jun 22 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.23-2
- Use PyPI as SOURCE0 for now
- Fix permission

* Fri Jun 20 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.23-1
- Initial package
