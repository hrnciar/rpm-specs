Name:           xcat
Version:        1.0.4
Release:        2%{?dist}
Summary:        A command line tool to explore blind XPath injection vulnerabilities

License:        MIT
URL:            https://github.com/orf/xcat
Source0:        %{pypi_source %{name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
XCat is a command line program that aides in the exploitation of blind XPath
injection vulnerabilities. It can be used to retrieve the whole XML document
being processed by a vulnerable XPath query, read arbitrary files on the
hosts filesystem and utilize out of bound HTTP requests to make the server
send data directly to xcat.

%prep
%autosetup

%build
%py3_build
# Fix dep for generator
sed -i -e "s/'xpath-expressions~=1.0'/'xpath-expressions'/g" setup.py
sed -i -e "s/aiohttp~=3.0/aiohttp<4.0/g" setup.py

%install
%py3_install

%files
%doc README.md
# License file was removed: https://github.com/orf/xcat/pull/35
#%%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.4-8
- Update to latest upstream release 1.0.4

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-17
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-9
- Rebuild for Python 3.6

* Fri Nov 25 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-8
- Cleanup

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-4
- Rebuilt

* Wed Jul 22 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-3
- Rebuilt

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Initial package for Fedora
